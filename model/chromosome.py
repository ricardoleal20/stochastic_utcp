"""
Let's create the Chromosome for the NSGA-II algorithm.
This class will be used to represent the chromosome of the population
based on the variables:

- subjects
- classrooms
- professors
- schedules
"""

import typing as tp
import random
from dataclasses import dataclass
from itertools import repeat

# Local imports
from model.types import Assignment

# Weight constants
W1 = 1.0
W2 = 1.0
W3 = 1.0
HARD_PENALTY_WEIGHT = int(1e9)
# Other constants as the number of scenarios to test
NUM_SCENARIOS: int = 10
NOISE_MEAN = 1.0
NOISE_STD = 0.1


@dataclass(slots=True)
class Chromosome:
    """Chromosome that represents a chromosome in the scheduling problem.
    Each chromosome is a list of assignments, where each assignment is a tuple:
    (classroom, professor, schedule) for a subject.
    """

    assignments: tp.List[Assignment]

    def __str__(self):
        # Define the output format for the chromosome
        output = []

        for idx, assignment in enumerate(self.assignments):
            output.append(
                f"Subject {idx + 1}: Classroom: {assignment.classroom},"
                + f" Professor: {assignment.professor}, Schedule: {assignment.schedule}"
            )
        return "\n".join(output)

    def __getitem__(self, index: int) -> Assignment:
        """Allow indexing to get a gene."""
        return self.assignments[index]

    def __setitem__(self, index: int, value: Assignment) -> None:
        """Allow indexing to set a gene."""
        self.assignments[index] = value

    def __len__(self):
        """Returns the number of subjects in the chromosome."""
        return len(self.assignments)

    # Add the methods to calculate the fitness of the chromosome
    # ========================================================== #
    @property
    def objective_value(self) -> tp.Tuple[float, float, float]:
        """Calculates the fitness of the chromosome. This is using the objective function.

        Its assumptions are:
            - CC: Penalización por cambios consecutivos de salones para el mismo profesor.
            - PH: Penalización por incumplimiento de horas consecutivas para la misma materia.
            - CB: Penalización por baja selección de salones grandes para materias con alta matrícula.

        Returns:
            tuple: (penalty_CC, penalty_PH, penalty_CB)
        """
        # Define the multiple scenarios here
        scenarios_result = []
        # Then, iterate over the number of scenarios provided
        for _ in repeat(None, NUM_SCENARIOS):
            # Get the penalties
            penalty_CC = self.__calculate_CC()
            penalty_PH = self.__calculate_PH()
            penalty_CB = self.__calculate_CB()

            # Get the hard penalty from the hard cons
            hard_penalty = self.__hard_constraints()

            # Apply the defined weights for each penalty
            weighted_CC = W1 * penalty_CC
            weighted_PH = W2 * penalty_PH
            weighted_CB = W3 * penalty_CB
            # Add it on the scenario
            scenarios_result.append(
                (
                    weighted_CC + hard_penalty,
                    weighted_PH + hard_penalty,
                    weighted_CB + hard_penalty,
                )
            )
        # At the end, return the average of the scenarios
        return (
            sum([scenario[0] for scenario in scenarios_result]) / NUM_SCENARIOS,
            sum([scenario[1] for scenario in scenarios_result]) / NUM_SCENARIOS,
            sum([scenario[2] for scenario in scenarios_result]) / NUM_SCENARIOS,
        )

    def __hard_constraints(self) -> float:
        """Add the hard constraints to the chromosome.

        Returns:
            float: The total penalty for the hard constraints.
        """
        # Dictionaries for grouping by (classroom, day, time) and (professor, day, time)
        classroom_usage = {}
        professor_usage = {}

        for assignment in self.assignments:
            # Key for classroom: (classroom, day, start, end)
            key_room = (
                assignment.classroom,
                assignment.schedule.day,
                assignment.schedule.start,
                assignment.schedule.end,
            )
            classroom_usage[key_room] = classroom_usage.get(key_room, 0) + 1

            # Key for professor: (professor, day, start, end)
            key_prof = (
                assignment.professor,
                assignment.schedule.day,
                assignment.schedule.start,
                assignment.schedule.end,
            )
            professor_usage[key_prof] = professor_usage.get(key_prof, 0) + 1

        # Penalize if the same classroom is used in the same time slot more than once
        hard_penalty = 0.0
        for count in classroom_usage.values():
            if count > 1:
                hard_penalty += (count - 1) * HARD_PENALTY_WEIGHT

        # Penalize if a professor is assigned to more than one class in the same time slot
        for count in professor_usage.values():
            if count > 1:
                hard_penalty += (count - 1) * HARD_PENALTY_WEIGHT

        # Penalize if the capacity of the classroom is insufficient for the subject's enrollment
        for assignment in self.assignments:
            if assignment.expected_enrollment > assignment.classroom.capacity:
                hard_penalty += (
                    assignment.expected_enrollment - assignment.classroom.capacity
                ) * HARD_PENALTY_WEIGHT
            # Penalize if the classroom is too large for the subject's enrollment
            elif assignment.expected_enrollment < assignment.classroom.capacity * 0.5:
                hard_penalty += (
                    assignment.classroom.capacity - assignment.expected_enrollment
                ) * HARD_PENALTY_WEIGHT
            # Penalize if the classroom type is different from the subject's type
            if (
                assignment.classroom.type != assignment.subject.type
                and assignment.subject.type.value != "MIX"
            ):
                hard_penalty += HARD_PENALTY_WEIGHT

        # Return this hard penalty
        return hard_penalty

    def __stochastic_factor(self) -> float:
        """Generate a stochastic factor with a normal distribution (mean 1, std NOISE_STD)."""
        return random.gauss(NOISE_MEAN, NOISE_STD)

    def __calculate_CC(self) -> float:
        """CC Penalization: Penalize the consecutive changes of classroom for the same professor.
        For example, if a professor teaches two consecutive classes and they are assigned to different classrooms,
        a penalty is added. A stochastic factor is added.
        """
        cc_penalty = 0.0
        # Group assignments by professor and day
        prof_day = {}
        for assignment in self.assignments:
            key = (assignment.professor, assignment.schedule.day)
            prof_day.setdefault(key, []).append(assignment)
        for assignments in prof_day.values():
            # Sort by start time
            assignments.sort(key=lambda a: a.schedule.start)
            for i in range(1, len(assignments)):
                prev = assignments[i - 1]
                curr = assignments[i]
                # If the same professor has consecutive assignments on the same day
                # and uses different classrooms, penalize.
                if prev.classroom != curr.classroom:
                    cc_penalty += 1.0 * self.__stochastic_factor()
        return cc_penalty

    def __calculate_PH(self) -> float:
        """PH Penalty: Penalizes if the required consecutive hours for the subject are not met.
        For example, if the block of the subject does not reach 2 consecutive hours.
        A stochastic factor is added.
        """
        ph_penalty = 0.0
        # Iterate over the assignments to check the duration of the class
        for assignment in self.assignments:
            duration = assignment.schedule.end - assignment.schedule.start
            # If the duration is less than 2 hours, penalize
            if duration < 2.0:
                ph_penalty += (2.0 - duration) * self.__stochastic_factor()
        return ph_penalty

    def __calculate_CB(self) -> float:
        """CB penalty: Penalizes the low selection of large classrooms for subjects with high enrollment.
        For example, if a large classroom is assigned to a subject with high demand.
        """
        cb_penalty = 0.0
        for assignment in self.assignments:
            # Based on the capacity of the classroom and the time of enrollment
            # for this assignment, penalize if the classroom is too small
            if assignment.classroom.capacity < assignment.expected_enrollment:
                cb_penalty += (
                    assignment.expected_enrollment / assignment.classroom.capacity
                ) * self.__stochastic_factor()
        return cb_penalty
