"""
This module defines the Solver class that integrates the generation of the population,
the running of the evolutionary optimization, and the retrieval of the result.
"""

from typing import Sequence, Optional

# DEAP imports
from deap import base, tools, algorithms

# Local imports
from model.igniters import (
    generate_valid_assignments,
    individuals_generator,
    evaluator_generator,
)
from model.types import Assignment, Subject, Classroom, Professor, Schedule
from model.chromosome import Chromosome


class Solver:
    """The Solver class integrates the generation of the population,
    the running of the evolutionary optimization, and the retrieval of the result.
    """

    _assignments: set[Assignment]
    _population_size: int
    _max_generations: int
    _mutation_rate: float
    _alpha: float
    _toolbox: base.Toolbox
    _result: Optional[list]
    __slots__ = (
        "_population_size",
        "_max_generations",
        "_mutation_rate",
        "_assignments",
        "_alpha",
        "_toolbox",
        "_result",
    )

    def __init__(
        self,
        population_size: int,
        max_generations: int,
        mutation_rate: float,
        solution_noise: float = 0.3,
    ):
        self._assignments = set()
        self._population_size = population_size
        self._max_generations = max_generations
        self._mutation_rate = mutation_rate
        self._alpha = solution_noise
        self._toolbox = base.Toolbox()
        self._result = None

    def set_inputs(
        self,
        subjects: Sequence[Subject],
        classrooms: Sequence[Classroom],
        professors: Sequence[Professor],
        schedules: Sequence[Schedule],
    ) -> None:
        """Set the inputs for the solver.

        Args:
            subjects: The subjects to be assigned.
            classrooms: The classrooms available.
            professors: The professors available.
            schedules: The schedules available.
        """
        # Using all this, create the assignments
        self._assignments = generate_valid_assignments(
            subjects, professors, classrooms, schedules
        )
        # Setup the DEAP toolbox with our individual generator and operators
        self.__setup_toolbox(subjects)

    def __setup_toolbox(self, subjects: Sequence[Subject]) -> None:
        """Configures the DEAP toolbox.
        The individual generator creates a Chromosome by, for each subject,
        selecting a valid Assignment from the global set of assignments.
        """
        # Run the individuals creator
        individuals_generator(subjects, self._assignments, self._toolbox)
        # Run the evaluation creator
        evaluator_generator(self._toolbox, self._mutation_rate, self._alpha)

    def solve(self, *, verbose: bool = False) -> None:
        """Runs the evolutionary optimization process using NSGA-II.
        Each individual is a Chromosome built from valid assignments.
        The evaluation function (incorporating scenario simulation) computes the expected penalties.
        """
        # Check if we have a valid population size
        if self._population_size <= 0:
            raise ValueError("Population size must be greater than 0")
        # Otherwise, check that we have assignments
        if not self._assignments:
            raise ValueError(
                "No assignments provided. Please create them using the set_inputs() method."
            )
        # Otherwise... run the solver
        # Generate initial population
        population = self._toolbox.population(n=self._population_size)  # type: ignore
        # Evaluate initial population
        for ind in population:
            ind.fitness.values = self._toolbox.evaluate(ind)  # type: ignore
        # Evolution loop
        for gen in range(1, self._max_generations + 1):
            offspring = algorithms.varAnd(
                population, self._toolbox, cxpb=0.7, mutpb=self._mutation_rate
            )
            for ind in offspring:
                ind.fitness.values = self._toolbox.evaluate(ind)  # type: ignore
            population = self._toolbox.select(  # type: ignore
                population + offspring, k=self._population_size
            )
            if verbose:
                print(
                    f"Generation {gen} completed. Best objective value: {min(ind.objective_value for ind in population)}"
                )
        # Extract the Pareto front (first non-dominated front)
        self._result = tools.sortNondominated(
            population, k=len(population), first_front_only=True
        )[0]

    def results(self) -> Chromosome:
        """Retrieve the results of the evolutionary optimization."""
        if self._result is None:
            raise RuntimeError(
                "Solver has not been run yet. Please call solve() first."
            )
        if not self._result:
            raise RuntimeError("No solution has been found.")
        # Get the final chromosome
        chromosome = self._result[0]
        print(f"Final Objective Value: {chromosome.objective_value}")
        return chromosome
