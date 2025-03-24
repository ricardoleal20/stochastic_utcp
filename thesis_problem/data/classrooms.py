"""
Define the classrooms that we're going to use in the problem
"""

from typing import TypeVar
from model.types import Classroom, SubjectType

CLASSROOMS = set()  # List of classrooms

# 1. Classrooms (13 standard classrooms for theoretical subjects or high enrollment)
for i in range(1, 14):
    CLASSROOMS.add(
        Classroom(
            name=f"Salón {i}",
            capacity=30,
            start_hour=7.0,
            end_hour=22.0,
            type=SubjectType.THEORY,
        )
    )

# 2. Electronics Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Laboratorio de Electrónica",
        capacity=20,
        start_hour=7.0,
        end_hour=22.0,
        type=SubjectType.LABORATORY,
    )
)

# 3. Materials Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Laboratorio de Materiales",
        capacity=15,
        start_hour=7.0,
        end_hour=16.0,
        type=SubjectType.LABORATORY,
    )
)

# 4. Design and Control Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Laboratorio de Diseño y Control",
        capacity=20,
        start_hour=7.0,
        end_hour=16.0,
        type=SubjectType.LABORATORY,
    )
)

# 5. Mechanical Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Taller Mecánico",
        capacity=15,
        start_hour=7.0,
        end_hour=16.0,
        type=SubjectType.LABORATORY,
    )
)

# 6. Robotic Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Laboratorio de Robótica",
        capacity=15,
        start_hour=7.0,
        end_hour=13.0,
        type=SubjectType.LABORATORY,
    )
)

# 7. Automotive Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Laboratorio Automotriz",
        capacity=12,
        start_hour=7.0,
        end_hour=18.0,
        type=SubjectType.LABORATORY,
    )
)

# 8. Mechatronics and Power Laboratory
CLASSROOMS.add(  # type: ignore
    Classroom(
        name="Laboratorio de Mecánica y Potencia",
        capacity=10,
        start_hour=7.0,
        end_hour=18.0,
        type=SubjectType.LABORATORY,
    )
)

# 9. Didactic classrooms (2 units)
for i in range(1, 3):
    classroom = Classroom(
        name=f"Sala Didáctica {i}",
        capacity=20,
        start_hour=7.0,
        end_hour=22.0,
        type=SubjectType.THEORY,
    )
    CLASSROOMS.add(classroom)

# At the very end, convert the classrooms to a tuple
CLASSROOMS: tuple[Classroom] = tuple(CLASSROOMS)  # type: ignore
