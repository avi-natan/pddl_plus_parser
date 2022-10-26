import os
from pathlib import Path

CWD = os.getcwd()
SOKOBAN_DOMAIN_FILE_PATH = Path(CWD, "sokoban_domain.pddl")
SOKOBAN_UNPARSED_PLAN_PATH = Path(CWD, "sokoban_plan.txt")
SOKOBAN_PROBLEM_PATH = Path(CWD, "sokoban_problem.pddl")

WOODWORKING_DOMAIN_FILE_PATH = Path(CWD, "woodworking_domain.pddl")
WOODWORKING_UNPARSED_PLAN_PATH = Path(CWD, "woodworking_plan.txt")
WOODWORKING_PARSED_PLAN_PATH = Path(CWD, "woodworking_plan.solution")
WOODWORKING_SHORT_PARSED_PLAN_PATH = Path(CWD, "woodworking_short_plan.solution")

COMBINED_PROBLEM_PATH = Path(CWD, "combined_problem.pddl")
COMBINED_DOMAIN_PATH = Path(CWD, "combined_domain.pddl")

MULTI_AGENT_DATA_DIRECTORY = Path(CWD, "multi_agent_problem")

WOODWORKING_AGENT_NAMES = ["glazer0", "grinder0", "highspeed-saw0", "immersion-varnisher0", "planer0", "saw0",
                           "spray-varnisher0"]


DEPOT_MA_DOMAIN_PATH = Path(CWD, "Depots.pddl")
DEPOT_MA_PROBLEM_PATH = Path(CWD, "pfile1_depot.pddl")
DEPOT_MA_CONCURRENT_PROBLEM_PATH = Path(CWD, "pfile7_depot.pddl")
DEPOT_MA_SOLUTION_PATH = Path(CWD, "pfile1_depots.solution")