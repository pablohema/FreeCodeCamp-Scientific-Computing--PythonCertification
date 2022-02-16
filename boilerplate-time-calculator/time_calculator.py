def add_time(start, duration, requested_day=""):
    # List for weekdays
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    # Convert start string in start list
    clock = start.split()
    time = clock[0].split(":")
    am_pm = clock[1]

    # Calculate 24hr format
    if am_pm == "PM":
        hour = int(time[0]) + 12
        time[0] = str(hour)

    # Convert duration string in duration list
    duration_time = duration.split(":")

    # Calculate new hours and minutes
    n_hour = int(time[0]) + int(duration_time[0])
    n_minutes = int(time[1]) + int(duration_time[1])

    # Calculate extra hours and minutes
    if n_minutes >= 60:
        extra_hour = n_minutes // 60
        n_minutes -= extra_hour * 60
        n_hour += extra_hour
    # Calculate extra day/s
    extra_day = 0
    if n_hour > 24:
        extra_day = n_hour // 24
        n_hour -= extra_day * 24

    # Calculate 12hr format
    if 12 > n_hour > 0:
        am_pm = "AM"
    elif n_hour == 12:
        am_pm = "PM"    
    elif n_hour > 12:
        am_pm = "PM"
        n_hour -= 12
    else:
        am_pm = "AM"
        n_hour += 12

    # Calculate extra day/s
    if extra_day > 0:
        if extra_day == 1:
            next_day = " (next day)"
        else:
            next_day = " (" + str(extra_day) + " days later)"
    else:
        next_day = ""
    
    # Calculate day on requested_day
    if requested_day:
        week_index = extra_day // 7
        i = week_days.index(requested_day.lower().capitalize()) + (extra_day - 7 * week_index)
        if i > 6:
            i -= 7
        day = ", " + week_days[i]
    else:
        day = ""
        
    # Prepare solution
    new_time = str(n_hour) + ":" + \
        (str(n_minutes) if n_minutes > 9 else ("0" + str(n_minutes))) + \
        " " + am_pm + day + next_day    

    return new_time