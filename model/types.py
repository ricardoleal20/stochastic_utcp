"""
Define different types for the model
"""
from typing import NamedTuple, Sequence
from enum import Enum


class SubjectType(str, Enum):
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


class Professor(NamedTuple):
    """Professor type, represents the total information about a professor.
    
    The professor has their name, the subjects they can teach, the schedules they are available,
    and the maximum hours they can teach per week.
    """
    name: str
    subjects: Sequence[str]
    schedules: Sequence[Schedule]
    max_hours_per_week: int | float

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
