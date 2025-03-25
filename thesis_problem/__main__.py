"""Run the thesis scenario into the solver"""

import numpy as np
from model.solver import Solver
# from model.utils import print_calendar_view, to_latex_table

# Local imports
from thesis_problem.data.subjects import SUBJECTS
from thesis_problem.data.professors import PROFESSORS
from thesis_problem.data.classrooms import CLASSROOMS
from thesis_problem.data.schedules import ALL_SCHEDULES


def __get_mean(data: list[tuple[float, float, float]]) -> float:
    return np.mean([x[0] for x in data])  # type: ignore


def __get_std(data: list[tuple[float, float, float]]) -> float:
    return np.std([x[0] for x in data])  # type: ignore


if __name__ == "__main__":
    solutions = []
    valid_solutions: int = 0
    # Repeat the experiment 30 times to have a good statistical analysis
    for i in range(0, 30):
        print(f"Running experiment {i + 1}...")
        # Step 1: Initialize the solver with parameters
        solver = Solver(population_size=50, max_generations=200, mutation_rate=0.1)
        # Step 2: Add the data from the Thesis problem
        solver.set_inputs(SUBJECTS, CLASSROOMS, PROFESSORS, ALL_SCHEDULES)
        # Step 3: Run the solver
        solver.solve(verbose=False)
        # Step 4: Get and process the results
        result = solver.results()
        # Append the objective result to the solutions list
        solutions.append(solver.objective_value_result)
        # Check if the solution is valid
        if all(x < 1e9 for x in solutions[-1]):
            valid_solutions += 1
        # print("Final Pareto Front")
        # print_calendar_view(result)
        # print("\n")
        # print(to_latex_table(result))
    # Print the mean and standard deviation of the objective values
    print(f"Mean: {__get_mean(solutions)}")
    print(f"Std: {__get_std(solutions)}")
    # Print the number of valid solutions
    print(f"Valid solutions: {valid_solutions}")
    # Print the number of invalid solutions
    print(f"Invalid solutions: {30 - valid_solutions}")
