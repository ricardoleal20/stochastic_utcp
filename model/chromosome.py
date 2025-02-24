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

@dataclass(slots=True)
class Chromosome:
    """Chromosome that represents a chromosome in the scheduling problem.
    Each chromosome is a list of assignments, where each assignment is a tuple:
    (classroom, professor, schedule) for a subject.
    """
    assignments: tp.Sequence[Assignment]

    def __str__(self):
        # Define the output format for the chromosome
        output = []

        for idx, assignment in enumerate(self.assignments):
            output.append(
                f"Subject {idx + 1}: Classroom: {assignment.classroom},"+
                f" Professor: {assignment.professor}, Schedule: {assignment.schedule}"
            )
        return "\n".join(output)

    def get_gene(self, index: int):
        """Returns the assignment (gene) of the subject at the given position.
        Args:
            index (int): Index of the subject.
        Returns:
            Assignment: NamedTuple of (classroom, professor, schedule).
        """
        return self.assignments[index]

    def set_gene(self, index: int, gene: Assignment):
        """Updates the assignment (gene) of the subject at the given position.
        Args:
            index (int): Index of the subject.
            gene (Assignment): NamedTuple of (classroom, professor, schedule).
        """
        self.assignments[index] = gene
