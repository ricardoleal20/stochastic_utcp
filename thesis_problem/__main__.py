"""Run the thesis scenario into the solver"""

from model.solver import Solver
from model.utils import print_calendar_view

# Local imports
from thesis_problem.data.subjects import SUBJECTS
from thesis_problem.data.professors import PROFESSORS
from thesis_problem.data.classrooms import CLASSROOMS
from thesis_problem.data.schedules import ALL_SCHEDULES

if __name__ == "__main__":
    # Step 1: Initialize the solver with parameters
    solver = Solver(population_size=50, max_generations=50, mutation_rate=0.1)
    # Step 2: Add the data from the Thesis problem
    solver.set_inputs(SUBJECTS, CLASSROOMS, PROFESSORS, ALL_SCHEDULES)
    # Step 3: Run the solver
    solver.solve(verbose=True)
    # Step 4: Get and process the results
    result = solver.results()
    print("Final Pareto Front")
    print_calendar_view(result)
