"""
Define the data subjects
"""

from model.types import Subject, SubjectType

# Map of subjects based on the provided data in the TFM
# * Note: I'm assuming that the practice is modeled as a LABORATORY
SUBJECTS = (
    Subject(
        name="Diseño por Computadora",
        hours=3,
        type=SubjectType.LABORATORY,
        preffered_classroom="Sala didáctica",
    ),
    Subject(
        name="Circuitos Eléctricos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    Subject(
        name="Dispositivos Semiconductores",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    Subject(
        name="Ingeniería de Materiales",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Materiales",
    ),
    Subject(
        name="Diseño de Mecanismos",
        hours=3,
        type=SubjectType.MIX,
        preffered_classroom="Mecánica",
    ),
    Subject(
        name="Mecánica de Materiales",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Materiales",
    ),
    # Subject(
    #     name="Medición e Instrumentación",
    #     hours=4.5,
    #     type=SubjectType.MIX,
    #     preffered_classroom="Electrónica",
    # ),
    Subject(
        name="Procesos de Manufactura",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Taller mecánico",
    ),
    Subject(
        name="Circuitos Digitales",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    # Subject(
    #     name="Diseño de componentes mecánicos",
    #     hours=3,
    #     type=SubjectType.MIX,
    #     preffered_classroom="Sala didáctica",
    # ),
    Subject(
        name="Dinámica de Sistemas Mecatrónicos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Sala didáctica",
    ),
    Subject(
        name="Electrónica Analógica",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    Subject(
        name="Práctica y Teoría de Procesos de Manufactura",
        hours=4.5,
        type=SubjectType.LABORATORY,
        preffered_classroom="Sala didáctica",
    ),
    Subject(
        name="Sistemas Electroneumáticos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Robótica",
    ),
    Subject(
        name="Diseño de Interfaces",
        hours=4.5,
        type=SubjectType.LABORATORY,
        preffered_classroom="Electrónica",
    ),
    # Subject(
    #     name="Gestión de proyecto de investigación",
    #     hours=3,
    #     type=SubjectType.THEORY,
    #     preffered_classroom="Salón",
    # ),
    Subject(
        name="Máquinas Eléctricas",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    # Subject(
    #     name="Procesamiento Digital de Señales",
    #     hours=4.5,
    #     type=SubjectType.THEORY,
    #     preffered_classroom="Sala didáctica",
    # ),
    # Subject(
    #     name="Sistemas de visión industrial",
    #     hours=3,
    #     type=SubjectType.MIX,
    #     preffered_classroom="Control",
    # ),
    Subject(
        name="Automatización",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Control y robótica",
    ),
    # Subject(
    #     name="Prácticum I: Metodología de diseño y gestión de proyectos",
    #     hours=4.5,
    #     type=SubjectType.MIX,
    #     preffered_classroom="Salón",
    # ),
    Subject(
        name="Control Aplicado",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    Subject(
        name="Sistemas Embebidos",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Control y robótica",
    ),
    Subject(
        name="Ingeniería Asistida por Computadora",
        hours=3,
        type=SubjectType.MIX,
        preffered_classroom="Sala didáctica",
    ),
    Subject(
        name="Electrónica de Potencia",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Electrónica",
    ),
    # Subject(
    #     name="Prácticum II: Proyecto de diseño",
    #     hours=4.5,
    #     type=SubjectType.LABORATORY,
    #     preffered_classroom="Laboratorio",
    # ),
    Subject(
        name="Robótica Industrial",
        hours=4.5,
        type=SubjectType.MIX,
        preffered_classroom="Control y robótica",
    ),
)
