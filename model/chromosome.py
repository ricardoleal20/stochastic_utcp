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
            # Suppose that:
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

        # Apply the defined weights for each penalty
        weighted_CC = W1 * penalty_CC
        weighted_PH = W2 * penalty_PH
        weighted_CB = W3 * penalty_CB

        return (weighted_CC, weighted_PH, weighted_CB)
