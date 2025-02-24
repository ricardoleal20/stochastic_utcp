"""
Generate the possible schedules for the problem
"""
from model.types import Schedule

def generate_schedules(
        block_size: int = 2
    ):
    """Generate an array of possible schedules for the problem.

    Args:
        block_size (int): Size of the block for the schedules.
        For example, if the block size is 2, the schedules will be generated
        from 7:00 to 9:00, 9:00 to 11:00, and so on.

    Returns:
        list: List of Schedule objects
    """
    possible_schedules = []
    for day in range(1, 6):  # Monday (1) to Friday (5)
        start_hour = 7 # Start at 7:00 AM
        while start_hour < 22:
            end_hour = start_hour + block_size
            if end_hour <= 22:
                possible_schedules.append(Schedule(
                    day=day,
                    start=start_hour,
                    end=end_hour
                ))
            start_hour += block_size
    return possible_schedules

ALL_SCHEDULES = generate_schedules()
