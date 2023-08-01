from datetime import datetime
from pathlib import Path

from pddl_plus_parser.lisp_parsers import DomainParser, ProblemParser
from pddl_plus_parser.multi_agent import MultiAgentTrajectoryExporter, PlanConverter


def do_logistics_test():
    domain_file_path = Path("benchmarks_mal/logistics_combined_benchmarks/logistics_combined_domain.pddl")
    problem_file_path = Path("benchmarks_mal/logistics_combined_benchmarks/logistics_combined_problem.pddl")
    combined_plan_file_path = Path("benchmarks_mal/logistics_combined_benchmarks/logistics_combined_plan.solution")
    combined_trajectory_file_path = Path("benchmarks_mal/logistics_combined_benchmarks/logistics_combined_triplets.trajectory")

    combined_domain = DomainParser(domain_path=domain_file_path, partial_parsing=False).parse_domain()
    combined_problem = ProblemParser(problem_path=problem_file_path, domain=combined_domain).parse_problem()
    trajectory_exporter = MultiAgentTrajectoryExporter(combined_domain)
    triplets = trajectory_exporter.parse_plan(problem=combined_problem, plan_path=combined_plan_file_path)
    trajectory_exporter.export_to_file(triplets, combined_trajectory_file_path)

def do_moving_test():
    domain_file_path = Path("benchmarks_mal/logistics_combined_benchmarks/warehouse-domain.pddl")
    problem_file_path = Path("benchmarks_mal/logistics_combined_benchmarks/warehouse-problem2.pddl")

    agent_names = ["tru1", "tru2", "tru3"]

    combined_domain = DomainParser(domain_path=domain_file_path, partial_parsing=False).parse_domain()
    combined_problem = ProblemParser(problem_path=problem_file_path, domain=combined_domain).parse_problem()
    plan_converter = PlanConverter(ma_domain=combined_domain)
    plan_folder_path = Path("benchmarks_mal/logistics_combined_benchmarks")
    plan_sequence = plan_converter.convert_plan(problem=combined_problem,
                                                plan_file_path=plan_folder_path / "warehouse-problem2-plan.txt",
                                                agent_names=agent_names,
                                                should_validate_concurrency_constraint=False)
    combined_plan_path = plan_folder_path / f"warehouse-combined-plan2.solution"
    plan_converter.export_plan(plan_file_path=combined_plan_path, plan_actions=plan_sequence)
    trajectory_exporter = MultiAgentTrajectoryExporter(combined_domain)
    triplets = trajectory_exporter.parse_plan(problem=combined_problem, plan_path=plan_folder_path / "warehouse-problem2-plan.txt")
    trajectory_exporter.export_to_file(triplets, plan_folder_path / "warehouse-problem2-combined_trajectory.trajectory")

if __name__ == '__main__':
    print(f'Hi MGSD malogistics pipeline!')
    start_time = datetime.now()

    # do_logistics_test()
    do_moving_test()

    end_time = datetime.now()
    delta = end_time - start_time
    print(f'time to finish: {delta}')

    print(f'Bye MGSD pipeline!')