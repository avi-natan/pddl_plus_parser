import os
from pathlib import Path

CWD = os.getcwd()
TEST_PARSING_FILE_PATH = Path(CWD, "test_domain_format_file.pddl")
TEST_WOODWORKING_DOMAIN_PATH = Path(CWD, "woodworking_domain.pddl")
TEST_NUMERIC_DEPOT_DOMAIN_PATH = Path(CWD, "depot_numeric_domain.pddl")
TEST_NUMERIC_PROBLEM = Path(CWD, "test_agricola_problem.pddl")
TEST_NUMERIC_DOMAIN = Path(CWD, "test_agricola_domain.pddl")

TEST_NUMERIC_DEPOT_DOMAIN = Path(CWD, "depot_numeric.pddl")
TEST_NUMERIC_DEPOT_PROBLEM = Path(CWD, "pfile2.pddl")
TEST_NUMERIC_DEPOT_TRAJECTORY = Path(CWD, "test_numeric_trajectory")

FARMLAND_NUMERIC_DOMAIN = Path(CWD, "farmland.pddl")
FARMLAND_NUMERIC_PROBLEM = Path(CWD, "pfile10_10.pddl")
FARMLAND_NUMERIC_TRAJECTORY = Path(CWD, "pfile10_10.trajectory")
