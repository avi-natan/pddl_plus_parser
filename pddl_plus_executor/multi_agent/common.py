from collections import defaultdict
from typing import List, Dict

from pddl_plus_executor.models import Problem, State, ActionCall, Domain, Operator, GroundedPredicate, \
    NOP_ACTION


def create_initial_state(problem: Problem) -> State:
    """Create the initial state of the problem.

    :param problem: the problem object.
    :return: the initial state of the problem.
    """
    initial_state_predicates = problem.initial_state_predicates
    initial_state_numeric_fluents = problem.initial_state_fluents
    return State(predicates=initial_state_predicates, fluents=initial_state_numeric_fluents, is_init=True)


def apply_actions(domain: Domain, current_state: State, joint_action: List[ActionCall], f_agents: Dict[str, Dict] = None,
                  allow_inapplicable_actions: bool = False) -> State:
    """

    :param domain: the domain with the action scheme.
    :param current_state: the current state that the action is being applied on.
    :param joint_action: the executable actions of the agents.
    :param f_agents: a dictionary describing the faulty agents and their fault model.
    :param allow_inapplicable_actions: whether to allow inapplicable actions.
    :return: The state resulting from applying the actions.
    """
    if len(joint_action) == 1:
        action_call = joint_action[0]
        action = domain.actions[action_call.name]
        oper = Operator(action=action, domain=domain, grounded_action_call=action_call.parameters)
        st = oper.apply(previous_state=current_state, f_agents=f_agents, allow_inapplicable_actions=allow_inapplicable_actions)
        return st

    accumulative_changed_state = current_state.copy()
    for action_call in joint_action:
        if action_call.name == NOP_ACTION:
            continue

        action = domain.actions[action_call.name]
        operator = Operator(action=action, domain=domain, grounded_action_call=action_call.parameters)
        accumulative_changed_state = operator.apply(accumulative_changed_state, f_agents=f_agents, allow_inapplicable_actions=allow_inapplicable_actions)
        # if operator.is_applicable(current_state) or allow_inapplicable_actions:
        #     print(9)
        #     accumulative_changed_state = operator.apply(accumulative_changed_state, f_agents=f_agents, allow_inapplicable_actions=True)
        # else:
        #     pass
        #     print(9)
        #     # raise ValueError("Cannot apply an action when it is not applicable!")

    return accumulative_changed_state
