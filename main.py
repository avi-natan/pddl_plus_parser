from datetime import datetime
from pathlib import Path

from pddl_plus_parser.lisp_parsers import DomainParser, ProblemParser
from pddl_plus_parser.multi_agent import MultiAgentTrajectoryExporter


if __name__ == '__main__':
    print(f'Hi MGSD malogistics pipeline!')
    start_time = datetime.now()

    domain_file_path = Path("benchmarks_mal/logistics_combined_benchmarks")
    problem_file_path = Path("benchmarks_mal/logistics_combined_benchmarks")
    combined_plan_file_path = Path("benchmarks_mal/logistics_combined_benchmarks")

    combined_domain = DomainParser(domain_path=domain_file_path / "logistics_combined_domain.pddl", partial_parsing=False).parse_domain()
    combined_problem = ProblemParser(problem_path=problem_file_path / "logistics_combined_problem.pddl",
                                     domain=combined_domain).parse_problem()
    trajectory_exporter = MultiAgentTrajectoryExporter(combined_domain)
    triplets = trajectory_exporter.parse_plan(problem=combined_problem, plan_path=combined_plan_file_path / "logistics_concurrent_plan.solution")
    trajectory_exporter.export_to_file(triplets, problem_file_path / f"logistics_combined_triplets.trajectory")

    end_time = datetime.now()
    delta = end_time - start_time
    print(f'time to finish: {delta}')

    print(f'Bye MGSD pipeline!')