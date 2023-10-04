def add_time(start_time, duration, start_day=None):
    # Split the start time into hours, minutes, and AM/PM
    start_time_parts = start_time.split()
    start_hours, start_minutes = map(int, start_time_parts[0].split(':'))
    period = start_time_parts[1]

    # Split the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate the total minutes for start time and duration
    total_start_minutes = start_hours * 60 + start_minutes
    total_duration_minutes = duration_hours * 60 + duration_minutes

    # Calculate the total minutes for the result
    total_minutes = total_start_minutes + total_duration_minutes

    # Calculate the new time in 24-hour format
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60

    # Calculate the number of days later
    days_later = new_hours // 24

    # Convert the time back to 12-hour format
    new_hours %= 12
    if new_hours == 0:
        new_hours = 12

    # Determine the new period (AM or PM)
    new_period = 'PM' if new_hours < 12 else 'AM'

    # Create the result string
    #
    new_time= f"{new_hours:2d}:{new_minutes:02d} {new_period}"

    # Handle the day of the week if provided
    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]

        if days_later == 1:
            new_time += f", {new_day} (next day)"
        elif days_later > 1:
            new_time += f", {new_day} ({days_later} days later)"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


print(add_time("6:30 PM", "205:12"))