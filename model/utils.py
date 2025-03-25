"""Utilities for the solver.

In the utilities, we can find funtions to plot and show a Chromosome.
"""

from model.chromosome import Chromosome

# Optional dictionary to translate numeric day to name
DAY_NAME = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}


def print_calendar_view(chromosome: Chromosome) -> None:
    """Print on the console a calendar view with the assignments contained in the chromosome.

    Args:
        chromosome: The chromosome to print the calendar view for.
    """
    # Order the assignments by (day, start)
    sorted_assignments = sorted(
        chromosome.assignments, key=lambda asg: (asg.schedule.day, asg.schedule.start)
    )

    print("=== Calendar View ===")
    current_day = None
    for asg in sorted_assignments:
        day = asg.schedule.day
        # Check if there's a change of day to print header
        if day != current_day:
            current_day = day
            day_str = DAY_NAME.get(day, f"Day {day}")
            print(f"\n--- {day_str} ---")
        start_time = asg.schedule.start
        end_time = asg.schedule.end
        subject_name = (
            asg.subject.name if hasattr(asg.subject, "name") else str(asg.subject)
        )
        print(
            f"  {start_time:4.1f}-{end_time:4.1f} | {subject_name} | {asg.classroom.name} | {asg.professor.name}"
        )


def to_latex_table(chromosome: Chromosome) -> str:
    """Returns a string with the LaTeX table containing the assignments of the chromosome.
    The table contains columns: Day, Hour, Subject, Classroom, Professor.

    Args:
        chromosome: The chromosome to convert to LaTeX table.

    Returns:
        - A string with the LaTeX table.
    """
    # Order assignments by (day, start)
    sorted_assignments = sorted(
        chromosome.assignments, key=lambda asg: (asg.schedule.day, asg.schedule.start)
    )

    # Build table content
    rows = []
    for asg in sorted_assignments:
        day = asg.schedule.day
        day_str = DAY_NAME.get(day, f"Day {day}")
        start_time = asg.schedule.start
        end_time = asg.schedule.end
        time_str = f"{start_time:4.1f}-{end_time:4.1f}"
        subject_name = (
            asg.subject.name if hasattr(asg.subject, "name") else str(asg.subject)
        )

        row = f"{day_str} & {time_str} & {subject_name} & {asg.classroom.name} & {asg.professor.name} \\\\"
        rows.append(row)

    # Basic LaTeX table template
    latex_code = r"""
\begin{table}[ht]
\centering
\begin{tabular}{l l l l l}
\hline
Day & Time & Subject & Classroom & Professor \\
\hline
"""[1:]  # [1:] to remove

    latex_code += "\n".join(rows)
    latex_code += r"""
\hline
\end{tabular}
\caption{Schedule generated by the chromosome}
\label{tab:schedule_chromosome}
\end{table}
"""[1:]  # [1:] to remove

    return latex_code
