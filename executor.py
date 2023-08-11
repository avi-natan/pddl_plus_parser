from datetime import datetime
from pathlib import Path

from pddl_plus_parser.lisp_parsers.domain_parser import DomainParser as ParseDomainParser
from pddl_plus_parser.lisp_parsers.problem_parser import ProblemParser as ParseProblemParser
from pddl_plus_parser.multi_agent import PlanConverter
from pddl_plus_executor.lisp_parsers.domain_parser import DomainParser as ExecDomainParser
from pddl_plus_executor.lisp_parsers.problem_parser import ProblemParser as ExecProblemParser
from pddl_plus_executor.multi_agent.multi_agent_trajectory_exporter import MultiAgentTrajectoryExporter


def execute_combined_plan_with_faults(c_domain, c_problem, c_plan_file_path, c_trajectory_path, f_agents):
    trajectory_exporter = MultiAgentTrajectoryExporter(c_domain)
    triplets = trajectory_exporter.parse_plan(problem=c_problem, f_agents=f_agents, plan_path=c_plan_file_path)
    trajectory_exporter.export_to_file(triplets, c_trajectory_path)

def generate_combined_plan(c_domain, c_problem, p_file_path, combined_p_file_path, a_names):
    plan_converter = PlanConverter(ma_domain=c_domain)
    plan_sequence = plan_converter.convert_plan(problem=c_problem,
                                                plan_file_path=p_file_path,
                                                agent_names=a_names,
                                                should_validate_concurrency_constraint=False)
    plan_converter.export_plan(plan_file_path=combined_p_file_path, plan_actions=plan_sequence)
    return plan_sequence


if __name__ == '__main__':
    print(f'Hi MGSD malogistics pipeline!')
    start_time = datetime.now()

    benchmarks_path = Path("benchmarks")
    domain_name = f"warehouse"
    problem_name = f"problem2"

    agent_names = ["tru1", "tru2", "tru3"]

    # this is a dictionary of {'agent': ['faulty_actions', 'model', 'prob']} where 'faulty_actions' can be one of:
    # 1. all - all actions can be faulty
    # 2. [actions] - actions in list can be faulty
    # and where 'model' can be one of:
    # 1. all - all effects are deleted
    # 2. [effects] - effects in list can be deleted
    # 3. postpone - the action is postponed and the preconditions are not consumed
    # and where 'prob' is the probability of action to be faulty
    #
    # we start with simplest fault model of: {'agent': ['all', 'all', 0.3]
    faulty_agents = {
        "tru1": ['all', 'all', 0.0],
        "tru2": ['all', 'all', 0.0],
        "tru3": ['all', 'all', 0.0]
    }
    domain_file_path = benchmarks_path / f"{domain_name}" / f"{domain_name}-domain.pddl"
    problem_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}.pddl"
    plan_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}-plan.txt"
    combined_plan_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}-combined_plan.solution"
    combined_trajectory_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}-combined_trajectory.trajectory"

    combined_parsing_domain = ParseDomainParser(domain_path=domain_file_path, partial_parsing=False).parse_domain()
    combined_parsing_problem = ParseProblemParser(problem_path=problem_file_path, domain=combined_parsing_domain).parse_problem()

    print(9)
    combined_plan = generate_combined_plan(
        combined_parsing_domain,
        combined_parsing_problem,
        plan_file_path,
        combined_plan_file_path,
        agent_names
    )

    combined_executing_domain = ExecDomainParser(domain_path=domain_file_path, partial_parsing=False).parse_domain()
    combined_executing_problem = ExecProblemParser(problem_path=problem_file_path, domain=combined_executing_domain).parse_problem()

    print(9)
    execute_combined_plan_with_faults(
        combined_executing_domain,
        combined_executing_problem,
        combined_plan_file_path,
        combined_trajectory_file_path,
        faulty_agents
    )

    end_time = datetime.now()
    delta = end_time - start_time
    print(f'time to finish: {delta}')

    print(f'Bye MGSD pipeline!')