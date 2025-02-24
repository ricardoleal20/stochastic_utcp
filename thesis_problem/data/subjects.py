"""
Define the data subjects
"""
from model.types import Subject, SubjectType

# Map of subjects based on the provided data in the TFM
# * Note: I'm assuming that the practice is modeled as a LABORATORY
SUBJECTS = (
    Subject(
        name="Diseño por computadora",
        hours=3,
        type=SubjectType.LABORATORY,
        preffered_classroom="Sala didáctica"
    ),
    Subject(
        name="Circuitos Eléctricos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Dispositivos semiconductores",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Ingeniería de materiales",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Materiales"
    ),
    Subject(
        name="Diseño de mecanismos",
        hours=3,
        type=SubjectType.MIX,
        preffered_classroom="Mecánica"
    ),
    Subject(
        name="Mecánica de materiales",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Materiales"
    ),
    Subject(
        name="Medición e instrumentación",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Procesos de manufactura",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Taller mecánico"
    ),
    Subject(
        name="Circuitos digitales",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Diseño de componentes mecánicos",
        hours=3,
        type=SubjectType.MIX,
        preffered_classroom="Sala didáctica"
    ),
    Subject(
        name="Dinámica de sistemas mecatrónicos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Sala didáctica"
    ),
    Subject(
        name="Electrónica analógica",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Manufactura asistida por computadora",
        hours=4.5,
        type=SubjectType.LABORATORY,
        preffered_classroom="Sala didáctica"
    ),
    Subject(
        name="Sistemas electroneumáticos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Robótica"
    ),
    Subject(
        name="Diseño de interfaces analógico digital",
        hours=4.5,
        type=SubjectType.LABORATORY,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Gestión de proyecto de investigación",
        hours=3,
        type=SubjectType.THEORY,
        preffered_classroom="Salón"
    ),
    Subject(
        name="Máquinas eléctricas",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Procesamiento digital de señales",
        hours=4.5,
        type=SubjectType.THEORY,
        preffered_classroom="Sala didáctica"
    ),
    Subject(
        name="Sistemas de visión industrial",
        hours=3,
        type=SubjectType.MIX,
        preffered_classroom="Control"
    ),
    Subject(
        name="Automatización",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Control y robótica"
    ),
    Subject(
        name="Prácticum I: Metodología de diseño y gestión de proyectos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Salón"
    ),
    Subject(
        name="Control Aplicado",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Sistemas embebidos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Control y robótica"
    ),
    Subject(
        name="Ingeniería asistida por computadora",
        hours=3,
        type=SubjectType.MIX,
        preffered_classroom="Sala didáctica"
    ),
    Subject(
        name="Electrónica de potencia",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica"
    ),
    Subject(
        name="Prácticum II: Proyecto de diseño",
        hours=4.5,
        type=SubjectType.LABORATORY,
        preffered_classroom="Laboratorio"
    ),
    Subject(
        name="Robótica industrial y de servicio",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Control y robótica"
    )
)
