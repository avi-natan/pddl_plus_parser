"""Module that encapsulates the functionality of grounded effects."""
import random
import copy
import logging
from typing import Set, Dict, Optional

from pddl_plus_executor.models.grounded_precondition import GroundedPrecondition
from pddl_plus_executor.models.grounding_utils import ground_predicate, ground_numeric_calculation_tree
from pddl_plus_executor.models.numerical_expression import NumericalExpressionTree, evaluate_expression, \
    set_expression_value
from pddl_plus_executor.models.pddl_action import Action
from pddl_plus_executor.models.pddl_domain import Domain
from pddl_plus_executor.models.pddl_function import PDDLFunction
from pddl_plus_executor.models.pddl_precondition import CompoundPrecondition
from pddl_plus_executor.models.pddl_predicate import Predicate, GroundedPredicate
from pddl_plus_executor.models.pddl_state import State


class GroundedEffect:
    """Class that represents the grounded version of an action's effect."""
    _lifted_discrete_effects: Set[Predicate]
    _lifted_numeric_effects: Set[NumericalExpressionTree]

    grounded_antecedents: GroundedPrecondition
    grounded_discrete_effects: Set[GroundedPredicate]
    grounded_numeric_effects: Set[NumericalExpressionTree]

    def __init__(self, lifted_antecedents: Optional[CompoundPrecondition],
                 lifted_discrete_effects: Set[Predicate], lifted_numeric_effects: Set[NumericalExpressionTree],
                 domain: Domain, action: Action):
        self.grounded_antecedents = GroundedPrecondition(lifted_antecedents, domain,
                                                         action) if lifted_antecedents is not None else None
        self._lifted_discrete_effects = lifted_discrete_effects
        self._lifted_numeric_effects = lifted_numeric_effects
        self.domain = domain
        self.action = action
        self.grounded_discrete_effects = set()
        self.grounded_numeric_effects = set()
        self.logger = logging.getLogger(__name__)

    def ground_conditional_effect(self, parameters_map: Dict[str, str]) -> None:
        """Grounds the conditional effect.

        :param parameters_map: the mapping between the lifted action's parameters and the objects using which the action
            is applied with.
        """
        if self.grounded_antecedents is not None:
            self.grounded_antecedents.ground_preconditions(parameters_map)

        for effect in self._lifted_discrete_effects:
            self.grounded_discrete_effects.add(ground_predicate(effect, parameters_map, self.domain, self.action))

        for effect in self._lifted_numeric_effects:
            self.grounded_numeric_effects.add(ground_numeric_calculation_tree(effect, parameters_map, self.domain))

    def antecedents_hold(self, state: State, allow_inapplicable_actions: bool = False) -> bool:
        """Checks whether the antecedents of the effect hold in the given state.

        :param state: the state that the effect is applied to.
        :param allow_inapplicable_actions: whether to allow inapplicable actions.
        :return: whether the antecedents hold in the given state.
        """
        if self.grounded_antecedents is None or allow_inapplicable_actions:
            return True

        return self.grounded_antecedents.is_applicable(state)

    def _apply_discrete_effects(self, next_state_predicates: Dict[str, Set[GroundedPredicate]], e_agent: str = None, e_actions: Dict = None) -> None:
        """Applies the discrete effects to the given state.

        :param next_state_predicates: the next state predicates to update with the effect's data.
        :param e_agent: the agent executing the operator.
        :param e_actions: actions of the executing agent and their fault models.
        """
        action_name = self.action.name
        prob = e_actions[action_name][0]
        rnd = random.uniform(0, 1)
        model = e_actions[action_name][1][0]

        if rnd > prob:
            grounded_discrete_effects_to_apply = copy.deepcopy(self.grounded_discrete_effects)
        else:
            if model == 'delete_all':
                self.logger.warning(f"The action '{action_name}' failed! 'delete_all' model deletes all of the effects...")
                grounded_discrete_effects_to_apply = set()
            # elif model == 'delete_some':
            else:
                grounded_discrete_effects_to_apply = set()
                for p in self.grounded_discrete_effects:
                    if p.name not in e_actions[action_name][1][1:]:
                        grounded_discrete_effects_to_apply.add(p)
            # elif model == 'postpone':
            #     # todo: to implement at some point
            #     pass
            # else:
            #     print(f'not a fault model. not doing anything')
            #     pass

        for predicate in grounded_discrete_effects_to_apply:
            lifted_predicate_str = predicate.lifted_untyped_representation
            if not predicate.is_positive:
                positive_predicate = predicate.copy()
                positive_predicate.is_positive = True
                if positive_predicate.lifted_untyped_representation not in next_state_predicates:
                    continue

                for state_predicate in next_state_predicates[positive_predicate.lifted_untyped_representation]:
                    if state_predicate.untyped_representation == positive_predicate.untyped_representation:
                        next_state_predicates[positive_predicate.lifted_untyped_representation].discard(state_predicate)
                        break

            else:
                next_state_grounded_predicates = next_state_predicates.get(lifted_predicate_str, set())
                next_state_grounded_predicates.add(predicate)
                next_state_predicates[lifted_predicate_str] = next_state_grounded_predicates

    @staticmethod
    def _update_single_numeric_expression(numeric_expression: NumericalExpressionTree,
                                          values_to_update: Dict[str, PDDLFunction]) -> None:
        """Updates the numeric value of a single numeric expression.

        :param numeric_expression: the expression that represents the change to the state.
        :param values_to_update: the previous values of the numeric expressions in the state to be updated.
        """
        set_expression_value(numeric_expression.root, values_to_update)
        new_grounded_function = evaluate_expression(numeric_expression.root)
        values_to_update[new_grounded_function.untyped_representation] = new_grounded_function

    def apply(self, state: State, e_agent: str = None, e_actions: Dict = None) -> None:
        """Applies the effect to the given state.

        :param state: the state in which the effect is applied.
        :param e_agent: the agent executing the operator.
        :param e_actions: actions of the executing agent and their fault models.
        """
        self.logger.debug("The antecedents for the effect hold so applying the effect.")
        self._apply_discrete_effects(next_state_predicates=state.state_predicates, e_agent=e_agent, e_actions=e_actions)
        for grounded_expression in self.grounded_numeric_effects:
            self._update_single_numeric_expression(grounded_expression, values_to_update=state.state_fluents)
