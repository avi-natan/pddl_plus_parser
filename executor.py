from datetime import datetime
from pathlib import Path

from pddl_plus_executor.lisp_parsers.domain_parser import DomainParser
from pddl_plus_executor.lisp_parsers.problem_parser import ProblemParser
from pddl_plus_executor.multi_agent.multi_agent_trajectory_exporter import MultiAgentTrajectoryExporter


def execute_combined_plan_with_faults(domain_path, problem_path, plan_path, combine_trajectory_path):
    combined_domain = DomainParser(domain_path=domain_path, partial_parsing=False).parse_domain()
    combined_problem = ProblemParser(problem_path=problem_path, domain=combined_domain).parse_problem()

    trajectory_exporter = MultiAgentTrajectoryExporter(combined_domain)
    triplets = trajectory_exporter.parse_plan(problem=combined_problem, plan_path=plan_path)
    trajectory_exporter.export_to_file(triplets, combine_trajectory_path)


if __name__ == '__main__':
    print(f'Hi MGSD malogistics pipeline!')
    start_time = datetime.now()

    benchmarks_path = Path("benchmarks")
    domain_name = f"warehouse"
    problem_name = f"problem2"

    agent_names = ["tru1", "tru2", "tru3"]
    domain_file_path = benchmarks_path / f"{domain_name}" / f"{domain_name}-domain.pddl"
    problem_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}.pddl"
    plan_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}-plan.txt"
    combined_plan_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}-combined_plan.solution"
    combined_trajectory_file_path = benchmarks_path / f"{domain_name}" / f"{problem_name}" / f"{domain_name}-{problem_name}-combined_trajectory.trajectory"

    print(9)
    execute_combined_plan_with_faults(
        domain_file_path,
        problem_file_path,
        plan_file_path,
        combined_trajectory_file_path
    )

    end_time = datetime.now()
    delta = end_time - start_time
    print(f'time to finish: {delta}')

    print(f'Bye MGSD pipeline!')