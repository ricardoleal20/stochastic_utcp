"""
Ignite different models and constraints
"""

import random
from typing import Sequence
from deap import base, creator, tools

# Local imports
from model.chromosome import Chromosome
from model.types import Subject, Professor, Classroom, Schedule, Assignment


def is_schedule_compatible(
    schedule: Schedule, available_schedules: Sequence[Schedule]
) -> bool:
    """
    Checks if the given schedule fits within any of the available schedules.
    For each available schedule (from a professor or classroom), it verifies that:
      - The days match.
      - The schedule's start and end times are within the available time window.
    """
    for avail in available_schedules:
        # Define the conditions for the schedule to be compatible
        conditions = (
            schedule.day == avail.day,
            schedule.start >= avail.start,
            schedule.end <= avail.end,
        )
        if all(conditions):
            return True
    # If no compatible schedule is found, return False
    return False


def generate_valid_assignments(
    subjects: Sequence[Subject],
    professors: Sequence[Professor],
    classrooms: Sequence[Classroom],
    schedules: Sequence[Schedule],
) -> set[Assignment]:
    """
    Generates a list of valid Assignment objects based on the combinations of:
      - Each subject.
      - Professors that can teach the subject.
      - Classrooms that match the subject's preferred classroom.
      - Schedules that are compatible with both the professor and the classroom.

    Args:
        subjects (Sequence[Subject]): List of subjects.
        professors (Sequence[Professor]): List of professors.
        classrooms (Sequence[Classroom]): List of classrooms.
        schedules (Sequence[Schedule]): Global list of possible schedules.

    Returns:
        List[Assignment]: List of valid assignments.
    """
    valid_assignments: set[Assignment] = set()

    for subject in subjects:
        # Initialize the list of professors that can teach the subject
        profs_for_subject = filter(
            lambda prof: subject.name in prof.subjects,  # pylint: disable=W0640
            professors,
        )

        # Filter the classrooms that are compatible (by preferred name; logic can be extended)
        classrooms_for_subject = [
            room
            for room in classrooms
            # if room.name == subject.preffered_classroom
        ]

        # For each combination of professor and classroom, check global schedules
        for prof in profs_for_subject:
            for room in classrooms_for_subject:
                for sched in schedules:
                    conditions = (
                        # * Verify that the schedule is compatible with the professor and classroom
                        is_schedule_compatible(sched, prof.schedules),
                        # Also, verify that the schedule fits within the classroom's time window
                        sched.start >= room.start_hour,
                        sched.end <= room.end_hour,
                    )

                    if all(conditions):
                        # If all conditions are met, create a new assignment
                        assignment = Assignment(
                            subject=subject,
                            classroom=room,
                            professor=prof,
                            schedule=sched,
                            expected_enrollment=0,  # This is going to be modified in the solver
                        )
                        valid_assignments.add(assignment)
    return valid_assignments


def individuals_generator(
    subjects: Sequence[Subject],
    assignments: set[Assignment],
    toolbox: base.Toolbox,
) -> None:
    """Initialize the method to generate individuals"""

    # Define a function to generate a single individual (Chromosome)
    def __generate_individual() -> Chromosome:
        """Local method to generate a single individual (Chromosome)"""
        selected_assignments = []
        for subj in subjects:
            # Filter the valid assignments for the current subject
            valid_for_subj = [
                asg for asg in assignments if asg.subject.name == subj.name
            ]
            if not valid_for_subj:
                raise ValueError(f"No valid assignment found for subject: {subj.name}")
            # Select a random assignment (can be modified)
            chosen_assignment = random.choice(valid_for_subj)
            # To this assignment, we assign a random expected enrollment
            chosen_assignment = chosen_assignment._replace(
                expected_enrollment=random.randint(10, 100)
            )
            selected_assignments.append(chosen_assignment)
        # And finally, return the Chromosome
        return creator.Individual(Chromosome(selected_assignments))  # type: ignore

    # Use the `__generate_individual` function to create individuals
    toolbox.register("individual", __generate_individual)
    # Also, register the population generator
    toolbox.register(
        "population",
        tools.initRepeat,
        list,
        toolbox.individual,  # type: ignore
    )


def evaluator_generator(
    toolbox: base.Toolbox, mutation_rate: float, alpha: float
) -> None:
    """Initialize the method to evaluate each individual"""

    # Function to evaluate an individual: it should incorporate multi-scenario evaluation for the stochastic model.
    # Here is a simplified version that returns dummy values.
    def evaluate_individual(ind: Chromosome) -> tuple[float, float, float]:
        # From the chromosome, get the fitness
        # From the objective function, append a random value related to alpha
        # THIS with the idea to incorporate noise into the evaluation process
        return tuple(v + random.uniform(-alpha, alpha) for v in ind.objective_value)  # type: ignore

    toolbox.register("evaluate", evaluate_individual)
    # Registry operators of crossover and mutation
    toolbox.register("mate", tools.cxTwoPoint)
    # Mutation: we use mutShuffleIndexes to reorder assignments with a certain probability.
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=mutation_rate)
    toolbox.register("select", tools.selNSGA2)

    # Configure the classes of DEAP for multiobjective (minimization)
    creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0, -1.0))
    creator.create("Individual", Chromosome, fitness=creator.FitnessMulti)  # type: ignore
