"""Module that represents a boolean predicate in a PDDL+ model."""
from typing import Dict, Optional

from .pddl_type import PDDLType

SignatureType = Dict[str, PDDLType]


class Predicate:
    """Class that represents a boolean predicate."""

    name: str
    signature: SignatureType

    def __init__(self, name: Optional[str] = None, signature: Optional[SignatureType] = None,
                 predicate: Optional["Predicate"] = None):
        if predicate:
            self.name = predicate.name
            self.signature = predicate.signature.copy()

        else:
            self.name = name
            self.signature = signature

    def __eq__(self, other: "Predicate") -> bool:
        """Checks whether or not two predicates are considered equal.

        Equality can be considered if a type inherits from another type as well.

        :param other: the other predicate to compare.
        :return: whether or not the predicates are equal.
        """
        if not self.name == other.name:
            return False

        for parameter_name, parameter_type in self.signature.items():
            if parameter_name not in other.signature:
                return False

            other_param_type = other.signature[parameter_name]
            if not parameter_type.is_sub_type(other_param_type):
                return False

        return True

    def __str__(self):
        signature_str_items = []
        for parameter_name, parameter_type in self.signature.items():
            signature_str_items.append(f"{parameter_name} - {str(parameter_type)}")

        signature_str = " ".join(signature_str_items)
        return f"({self.name} {signature_str})"

    def __hash__(self):
        return hash(self.__str__())
