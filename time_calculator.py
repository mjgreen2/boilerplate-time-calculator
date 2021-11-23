def add_time(start, duration, day = None):

    """Divide "start" into Hour, Minute, Meridian"""
    starting_time = start.split(":")
    second_half = starting_time[1].split()
    del starting_time[1]
    starting_time.extend(second_half)
    start_hour = int(starting_time[0])
    start_minute = int(starting_time[1])
    start_meridiem = starting_time[2]

    """Divide "duration" into Hours, Minutes"""
    elapsed_time = duration.split(":")
    hours_elapsed = int(elapsed_time[0])
    minutes_elapsed = int(elapsed_time[1])

    """Grab day from input"""
    start_day = day
    
    meridiem_from_hour = {1:"AM", 2:"AM", 3:"AM", 4:"AM", 5:"AM", 6:"AM", 7:"AM", 8:"AM", 9:"AM", 
    10:"AM", 11:"AM", 12:"PM", 13:"PM", 14:"PM", 15:"PM", 16:"PM", 17:"PM", 18:"PM", 19:"PM", 
    20:"PM", 21:"PM", 22:"PM", 23:"PM", 0: "AM"}
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    military_hour = 0

    """Get minutes of final time value. Convert sum of start and elapsed minutes
    for additional hours"""
    finished_minutes = (start_minute + minutes_elapsed) % 60
    minutes_to_hours_conversion = int((start_minute + minutes_elapsed) / 60)
    if (finished_minutes < 10) :
        minutes_string = "0" + str(finished_minutes)
    else :
        minutes_string = str(finished_minutes)

    """Use meridiem (AM or PM) to get military time for access to create key for 'meridiem_from_hour' dict"""
    if (start_meridiem == "PM"):
        military_hour = start_hour + 12
    else:
        military_hour = start_hour

    """Calculate hours and meridiem for final time value."""
    total_hours = (military_hour + hours_elapsed + minutes_to_hours_conversion) % 24
    finished_meridiem = meridiem_from_hour.get(total_hours, "Unknown")
    finished_hours = (start_hour + hours_elapsed + minutes_to_hours_conversion) % 12
    if (finished_hours == 0):
        finished_hours += 12

    """If requested, calculate day for final time value"""
    days_elapsed = int((hours_elapsed + minutes_to_hours_conversion) / 24)
    if ((start_meridiem == "PM") & (finished_meridiem == "AM")):
            days_elapsed += 1

    if (start_day != None) :   
        day_key = day_of_week.index(start_day.capitalize())
        day_key += days_elapsed
        day_key %= 7
        finished_day = day_of_week[day_key]

    """Create string for final time output"""
    new_time = str(finished_hours) + ":" + minutes_string + " " + finished_meridiem

    if (start_day != None):
        new_time += ", " + finished_day

    if (days_elapsed > 1):
        new_time += " (" + str(days_elapsed) + " days later)"
    elif (days_elapsed == 1):
        new_time += " (next day)"


    return new_time