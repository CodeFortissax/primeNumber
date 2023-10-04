def add_time(start, duration, start_day=None):
    # Define the days of the week.
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time and duration.
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Convert start time to 24-hour format.
    if period == "PM" and start_hour != 12:
        start_hour += 12

    # Calculate the total minutes.
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate the new time.
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    # Determine the number of days later.
    days_later = total_minutes // (24 * 60)

    # Determine the day of the week.
    if start_day:
        start_day = start_day.capitalize()
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        days_later_text = f", {new_day}" if days_later > 0 else ""

    # Determine the period (AM/PM).
    period = "PM" if new_hour >= 12 else "AM"

    # Format the result time.
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    new_time = f"{new_hour:1}:{new_minute:02} {period}"

    # Add the day of the week.
    if start_day:
        new_time += days_later_text


    # Add days later text.
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    # Day given but unchanging
    if days_later < 1 and start_day != None:
        new_time += str(f", {start_day}")



    return new_time


print(add_time("11:43 AM", "667:20"))