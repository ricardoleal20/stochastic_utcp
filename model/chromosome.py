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
from dataclasses import dataclass

# Local imports
from model.types import Assignment

W1 = 1.0
W2 = 1.0
W3 = 1.0
HARD_PENALTY_WEIGHT = int(1e9)


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
        # Define the penalty parameters
        penalty_CC = 0.0
        penalty_PH = 0.0
        penalty_CB = 0.0

        # Iterate over the assignments
        for assignment in self.assignments:
            # IF the classroom name does not contain a certain keyword, penalize (e.g., for CC)
            if "Salón" not in assignment.classroom:
                penalty_CC += 1.0
            # If the block duration is less than 2 hours, penalize (e.g., for PH)
            duration = assignment.schedule.end - assignment.schedule.start
            if duration < 2.0:
                penalty_PH += 2.0 - duration
            # If the classroom is small for the subject (this example is dummy; in reality compare with enrollment)
            if "Laboratorio" in assignment.classroom:
                penalty_CB += 1.0

        # Get the hard penalty from the hard cons
        hard_penalty = self.__hard_constraints()

        # Apply the defined weights for each penalty
        weighted_CC = W1 * penalty_CC
        weighted_PH = W2 * penalty_PH
        weighted_CB = W3 * penalty_CB

        return (
            weighted_CC + hard_penalty,
            weighted_PH + hard_penalty,
            weighted_CB + hard_penalty,
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

        # Return this hard penalty
        return hard_penalty
