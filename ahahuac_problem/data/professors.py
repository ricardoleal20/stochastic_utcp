"""
Definition of the Professors class based on the test data
"""
from model.types import Professor, Schedule

PROFESSORS = (
    Professor(
        name="Prof. 1",
        subjects=("Electrónica Analógica", "Circuitos Eléctricos", "Electrónica de Potencia"),
        schedules=(
            # Days 2 and 4 (Tuesday and Thursday) from 8:30 to 17:30
            Schedule(day=2, start=8.5, end=17.5),
            Schedule(day=4, start=8.5, end=17.5)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 2",
        subjects=("Circuitos Digitales", "Dispositivos Semiconductores"),
        schedules=(
            Schedule(day=2, start=7.0, end=16.0),
            Schedule(day=4, start=7.0, end=16.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 3",
        subjects=("Circuitos Eléctricos"),
        schedules=(
            # Days 1,2,3,4,5 (Monday to Friday) from 7:00 to 16:00
            Schedule(day=1, start=7.0, end=16.0),
            Schedule(day=2, start=7.0, end=16.0),
            Schedule(day=3, start=7.0, end=16.0),
            Schedule(day=4, start=7.0, end=16.0),
            Schedule(day=5, start=7.0, end=16.0)
        ),
        max_hours_per_week=15
    ),
    Professor(
        name="Prof. 4",
        subjects=("Diseño por Computadora"),
        schedules=(
            # Days 1 and 3 from 7:00 to 13:00
            Schedule(day=1, start=7.0, end=13.0),
            Schedule(day=3, start=7.0, end=13.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 5",
        subjects=("Ingeniería Asistida por Computadora", "Diseño por Computadora"),
        schedules=(
            # Days 2 and 4 from 16:00 to 22:00
            Schedule(day=2, start=16.0, end=22.0),
            Schedule(day=4, start=16.0, end=22.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 6",
        subjects=("Dinámica de Sistemas", "Diseño de Interfaces", "Control Aplicado"),
        schedules=(
            # Days 2 and 4 from 7:00 to 14:30
            Schedule(day=2, start=7.0, end=14.5),
            Schedule(day=4, start=7.0, end=14.5)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 7",
        subjects=("Procesos de Manufactura"),
        schedules=(
            # Days 2 and 4 from 10:00 to 13:00
            Schedule(day=2, start=10.0, end=13.0),
            Schedule(day=4, start=10.0, end=13.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 8",
        subjects=("Lab. Ingeniería de Materiales"),
        schedules=(
            # Days 1,2,3,4,5 from 7:00 to 16:00
            Schedule(day=1, start=7.0, end=16.0),
            Schedule(day=2, start=7.0, end=16.0),
            Schedule(day=3, start=7.0, end=16.0),
            Schedule(day=4, start=7.0, end=16.0),
            Schedule(day=5, start=7.0, end=16.0)
        ),
        max_hours_per_week=15
    ),
    Professor(
        name="Prof. 9",
        subjects=("Ingeniería de Materiales", "Práctica y Teoría de Procesos de Manufactura"),
        schedules=(
            # Days 1, 3 and 5 from 7:00 to 10:00
            Schedule(day=1, start=7.0, end=10.0),
            Schedule(day=3, start=7.0, end=10.0),
            Schedule(day=5, start=7.0, end=10.0)
        ),
        max_hours_per_week=15
    ),
    Professor(
        name="Prof. 10",
        subjects=("Procesos de Manufactura"),
        schedules=(
            # Days 1 and 3 from 7:00 to 16:00
            Schedule(day=1, start=7.0, end=16.0),
            Schedule(day=3, start=7.0, end=16.0)
        ),
        max_hours_per_week=1.5
    ),
    Professor(
        name="Prof. 11",
        subjects=("Procesamiento Digital de Señales"),
        schedules=(
            # Days 1, 3 and 5 from 7:00 to 8:30
            Schedule(day=1, start=7.0, end=8.5),
            Schedule(day=3, start=7.0, end=8.5),
            Schedule(day=5, start=7.0, end=8.5)
        ),
        max_hours_per_week=1.5
    ),
    Professor(
        name="Prof. 12",
        subjects=("Circuitos Eléctricos"),
        schedules=(
            # Days 1, 3 and 5 from 8:30 to 13:00
            Schedule(day=1, start=8.5, end=13.0),
            Schedule(day=3, start=8.5, end=13.0),
            Schedule(day=5, start=8.5, end=13.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 13",
        subjects=("Máquinas Eléctricas"),
        schedules=(
            # Days 2 and 4 from 13:00 to 18:00
            Schedule(day=2, start=13.0, end=18.0),
            Schedule(day=4, start=13.0, end=18.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 14",
        subjects=("Diseño de Mecanismo", "Mecánica de Materiales"),
        schedules=(
            # Days 2 and 4 from 17:30 to 22:00
            Schedule(day=2, start=17.5, end=22.0),
            Schedule(day=4, start=17.5, end=22.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 15",
        subjects=("Ingeniería de Materiales", "Prácticum I"),
        schedules=(
            # Days 1 and 3 from 8:30 to 14:30
            Schedule(day=1, start=8.5, end=14.5),
            Schedule(day=3, start=8.5, end=14.5)
        ),
        max_hours_per_week=15
    ),
    Professor(
        name="Prof. 16",
        subjects=(
            "Sistemas Electroneumáticos", "Sistemas Embebidos",
            "Robótica Industrial", "Automatización"
        ),
        schedules=(
            # Days 1, 2, 3 and 5 from 7:00 to 13:00
            Schedule(day=1, start=7.0, end=13.0),
            Schedule(day=2, start=7.0, end=13.0),
            Schedule(day=3, start=7.0, end=13.0),
            Schedule(day=5, start=7.0, end=13.0)
        ),
        max_hours_per_week=15
    ),
    Professor(
        name="Prof. 17",
        subjects=("Sistemas Integrados de Manufactura", "Mecánica de Materiales"),
        schedules=(
            # Days 2 and 4 from 13:00 to 19:00
            Schedule(day=2, start=13.0, end=19.0),
            Schedule(day=4, start=13.0, end=19.0)
        ),
        max_hours_per_week=12
    ),
    Professor(
        name="Prof. 18",
        subjects=("Vehículos Híbridos y Autónomos"),
        schedules=(
            # Days 1 and 3 from 14:30 to 18:00
            Schedule(day=1, start=14.5, end=18.0),
            Schedule(day=3, start=14.5, end=18.0)
        ),
        max_hours_per_week=12
    )
)
