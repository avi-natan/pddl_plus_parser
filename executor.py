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
    triplets = trajectory_exporter.parse_plan(problem=c_problem, f_agents=f_agents, plan_path=c_plan_file_path, allow_inapplicable_actions=False)
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
    domain_name = f"logistics-4-0"
    # domain_name = f"warehouse2"
    problem_name = f"problem001"
    # problem_name = f"problemMinimalistic"

    # agent_names = ["apn1", "apn2", "tru1", "tru2", "tru3", "tru4", "tru5"]
    agent_names = ["apn1", "tru1", "tru2"]
    # agent_names = ["tru1", "tru2", "tru3"]

    # this is a dictionary of {'agent': {'action': ['prob', 'model']}} where:
    # 'agent': str - the agent name
    # 'action': str - the action name
    # 'prob': float - the probability of this action to fail
    # 'model': str - the fault model for a failed action. can be one of:
    #                ['delete_all']: delete all effects
    #                ['delete_some', 'e1', 'e2', ..., 'en']: delete following effects
    #                ['postpone']: postpone the action
    # we start with simplest fault model of: {'a1': {'act1': [0.3, ['delete_all]]}
    # faulty_agents = {
    #     'tru1': {
    #         'move-forward': [0.99, ['delete_all']],
    #         'rotate-right': [0.0, ['delete_all']],
    #         'rotate-left': [0.0, ['delete_all']],
    #         'lift-box': [0.0, ['delete_all']],
    #         'drop-box': [0.0, ['delete_all']]
    #     },
    #     'tru2': {
    #         'move-forward': [0.0, ['delete_all']],
    #         'rotate-right': [0.0, ['delete_all']],
    #         'rotate-left': [0.0, ['delete_all']],
    #         'lift-box': [0.0, ['delete_all']],
    #         'drop-box': [0.0, ['delete_all']]
    #     },
    #     'tru3': {
    #         'move-forward': [0.0, ['delete_all']],
    #         'rotate-right': [0.0, ['delete_all']],
    #         'rotate-left': [0.0, ['delete_all']],
    #         'lift-box': [0.0, ['delete_all']],
    #         'drop-box': [0.0, ['delete_all']]
    #     }
    # }

    faulty_agents = {
        'apn1': {
            'load-airplane': [0.0, ['delete_all']],
            'unload-airplane': [0.0, ['delete_all']],
            'fly-airplane': [0.0, ['delete_all']]
        },
        # 'apn2': {
        #     'load-airplane': [0.0, ['delete_all']],
        #     'unload-airplane': [0.0, ['delete_all']],
        #     'fly-airplane': [0.0, ['delete_all']]
        # },
        'tru1': {
            'load-truck': [0.0, ['delete_all']],
            'unload-truck': [0.0, ['delete_all']],
            'drive-truck': [0.0, ['delete_all']]
        },
        'tru2': {
            'load-truck': [0.0, ['delete_all']],
            'unload-truck': [0.99, ['delete_all']],
            'drive-truck': [0.0, ['delete_all']]
        },
        # 'tru3': {
        #     'load-truck': [0.0, ['delete_all']],
        #     'unload-truck': [0.0, ['delete_all']],
        #     'drive-truck': [0.0, ['delete_all']]
        # },
        # 'tru4': {
        #     'load-truck': [0.0, ['delete_all']],
        #     'unload-truck': [0.0, ['delete_all']],
        #     'drive-truck': [0.0, ['delete_all']]
        # },
        # 'tru5': {
        #     'load-truck': [0.0, ['delete_all']],
        #     'unload-truck': [0.0, ['delete_all']],
        #     'drive-truck': [0.0, ['delete_all']]
        # },
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