def add_time(start, duration, day=""):
    """Adds hours and minutes to a given 12-hour clock time (weekday optional)."""

    # Parses input into the required variables
    start = start.split(" ")
    start_time = start[0].split(":")
    hours, minutes = int(start_time[0]), int(start_time[1])
    period = start[1].upper()
    
    duration = duration.split(":")
    duration_hours, duration_minutes = int(duration[0]), int(duration[1])
    day = day.title()

    # Initializes days of the week
    week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days_later = 0

    # Pre-calculates duration days
    while duration_hours >= 24:
        duration_hours -= 24
        days_later += 1

    # Adds the times together
    for operation in ["add_minutes", "add_hours"]:

        # Stores pre-calculation validation for period toggles
        if hours >= 12:
            was_twelve = True
        else:
            was_twelve = False

        # First pass, adds minutes
        if operation == "add_minutes":
            minutes += duration_minutes
            if minutes >= 60:
                minutes -= 60
                hours += 1

        # Second pass, adds hours
        if operation == "add_hours":
            hours += duration_hours

        # Gets hour values of 24+ back into the 12-hour format
        if hours > 24:
            hours -= 24
            days_later += 1

        if hours == 24:
            hours = 12
            if period == "AM":
                period = "PM"
            elif period == "PM":
                period = "AM"
                days_later += 1

        # Stores post-calculation validation for period toggles
        if hours >= 12:
            is_twelve = True
        else:
            is_twelve = False

        # Toggles period if necessary, adds 1 day if going from PM to AM
        if was_twelve != is_twelve:
            if period == "AM":
                period = "PM"
            elif period == "PM":
                period = "AM"
                days_later += 1

        # Gets remaining hour values above 12 back into the 12-hour format
        if hours > 12:
            hours -= 12

    # Adds leading zero back into minutes
    minutes = str(minutes)
    if len(minutes) < 2:
        minutes = f"0{minutes}"

    # Calculates the resulting day of the week
    if day:
        day_index = week_days.index(day)
        for day in range(0, days_later):
            if day_index == 6:
                day_index = 0
            else:
                day_index += 1
        day = week_days[day_index]

    # Creates matching string for the amount of days passed
    if days_later == 0:
        days_later_text = ""
    elif days_later == 1:
        days_later_text = " (next day)"
    else:
        days_later_text = f" ({days_later} days later)"

    # Assembles all results into final output
    new_time = f"{hours}:{minutes} {period}"
    if day:
        new_time = f"{new_time}, {day}"
    new_time = f"{new_time}{days_later_text}"

    return new_time
