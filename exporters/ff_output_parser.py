"""Parse the output of the mtericFF planner so that the algorithms will be able to use it."""
import logging
import re

from pathlib import Path
from typing import NoReturn

PLAN_COMPONENT_REGEX = "\d: ([\w+\s?]+)\n"


class MetricFFParser:
    """Parse metricFF plans and exports then into standard output file."""

    logger: logging.Logger

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _open_plan_file(self, input_path: Path) -> str:
        """Safely open the file and returns its content.

        :param input_path: the path to the log file.
        :return: the file content.
        """
        with open(input_path, "rt") as interm_plan_file:
            return interm_plan_file.read()

    def parse_plan(self, input_path: Path, output_path: Path) -> NoReturn:
        """Parse the output file and exports a plan if exists.

        :param input_path: the path to the output log of metricFF planner.
        :param output_path: the path to the output plan file.
        """
        planner_output = self._open_plan_file(input_path)
        matches = re.finditer(PLAN_COMPONENT_REGEX, planner_output, re.MULTILINE)
        plan_seq = []
        for match in matches:
            action_sequence = match.group(1)
            self.logger.debug(f"action sequence - {action_sequence}")
            plan_seq.append(f"({action_sequence.lower().strip()})\n")

        with open(output_path, "wt") as output_file:
            output_file.writelines(plan_seq)


if __name__ == '__main__':
    plan_path = Path("C:\\Users\owner\Documents\GitHub\pddl_plus_parser\\tests\exporters_tests\output.out")
    output_path = Path("C:\\Users\owner\Documents\GitHub\pddl_plus_parser\\tests\exporters_tests\\test_output.out")
    ff_parser = MetricFFParser()
    ff_parser.parse_plan(plan_path, output_path)