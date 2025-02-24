"""
Define different types for the model
"""
from typing import NamedTuple, Sequence
from enum import Enum

class SubjectType(Enum, str):
    """SubjectType enum that represents the type of a subject.
    
    The subject can be theory, practice, or laboratory.
    """
    THEORY = "THEORY"
    LABORATORY = "LABORATORY"
    MIX = "MIX"


class Schedule(NamedTuple):
    """Schedule type that represents a schedule for a subject.
    
    Each day is represented by an integer from 1 to 5, where 1 is Monday and 5 is Friday.
    The start and end times are represented by integers, representing the hour of the day.
    """
    day: int
    start: float
    end: float

class _Professor(NamedTuple):
    """Professor type that represents a professor.
    
    The professor has a name and a list of subjects that they can teach.
    """
    name: str
    subjects: Sequence[str]
    schedules: Sequence[Schedule]
    max_hours_per_week: int | float

class Professor(_Professor):
    """Professor type, represents the total information about a professor.
    
    The professor has their name, the subjects they can teach, the schedules they are available,
    and the maximum hours they can teach per week.
    """
    def __new__(
            cls,
            name: str,
            subjects: Sequence[str],
            schedules: Sequence[Schedule],
            max_hours_per_week: int | float
        ):
        # Get the total hours designed for this professor
        total_hours = sum(
            (schedule.end - schedule.start).total_seconds() / 3600 for schedule in schedules
        )
        if total_hours > max_hours_per_week:
            raise ValueError(
                f"Total scheduled hours ({total_hours}) exceed the maximum"+
                f" hours per week ({max_hours_per_week})."
            )
        # Return the professor
        return super().__new__(cls, name, subjects, schedules, max_hours_per_week)

class Subject(NamedTuple):
    """Subject type that represents a subject.
    It represents how many hours the subject has to include per week,
    their name, the type of subject (theory, practice, or laboratory),
    and the preferred classroom.
    """
    name: str
    hours: int | float
    type: SubjectType
    preffered_classroom: str

class Classroom(NamedTuple):
    """Classroom type that represents a classroom.
    
    """
    name: str
    capacity: int
    start_hour: float
    end_hour: float
    type: SubjectType


class Assignment(NamedTuple):
    """Assignment type that represents an assignment for a subject.
    
    The assignment is composed of a classroom, professor, and schedule and it subject
    """
    subject: Subject
    classroom: Classroom
    professor: Professor
    schedule: Schedule
