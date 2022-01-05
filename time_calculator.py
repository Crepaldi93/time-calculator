def add_time(start, duration, week_day=False):

    # Split the "start" string into hour, minute and am_pm parameters

    start_full = start.split()

    start_hour =  int((start_full[0]).split(":")[0])

    start_minute =  int((start_full[0]).split(":")[1])

    start_period = start_full[1]


    # Split the "duration" string into hour and minute parameters

    duration_full = duration.split()

    duration_hour =  int((duration_full[0]).split(":")[0])

    duration_minute =  int((duration_full[0]).split(":")[1])


    # Defines variables new_time, new_hour, new_minute, new_period and n

    new_time = ""

    new_hour = start_hour

    new_minute = 0

    new_period = start_period

    n = 0

    # Add up minutes

    if start_minute + duration_minute > 60:
        new_minute = start_minute + duration_minute - 60
        new_hour = start_hour + 1

        if new_hour == 12 and new_period == "AM":
            new_period = "PM"

        elif new_hour == 13 and new_period == "PM":
            new_hour = 1

        elif new_hour == 12 and new_period == "PM":
            new_period = "AM"
            n += 1

        elif new_hour == 13 and new_period == "AM":
            new_hour = 1


    else:
        new_minute = start_minute + duration_minute


    # Add up hours

    while duration_hour > 0:
        new_hour += 1

        if new_hour == 12 and new_period == "AM":
            new_period = "PM"

        elif new_hour == 13 and new_period == "PM":
            new_hour = 1

        elif new_hour == 12 and new_period == "PM":
            new_period = "AM"
            n += 1

        elif new_hour == 13 and new_period == "AM":
            new_hour = 1

        duration_hour -= 1



    # List containing the days of the week

    week_days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]


    # Define new week day

    if week_day is not False and week_day.lower() in week_days:

        ind_week_day = week_days.index(week_day.lower())
        number_of_days = n
        while number_of_days > 0:
            ind_week_day += 1

            if ind_week_day > 6:
                ind_week_day = 0

            number_of_days -= 1

        new_week_day = (week_days[ind_week_day]).capitalize()



    # Number of days later

    if n == 1:
        days_later = "(next day)"

    if n > 1:
        days_later = f"({n} days later)"


    # Format new_time

    new_hour = str(new_hour)
    new_minute = str(new_minute)

    if week_day is False:

        if n == 0:
            new_time = f"{new_hour}:{new_minute.zfill(2)} {new_period}"

        elif n >= 1:
            new_time = f"{new_hour}:{new_minute.zfill(2)} {new_period} {days_later}"

    elif week_day is not False:

        if n == 0:
            new_time = f"{new_hour}:{new_minute.zfill(2)} {new_period}, {new_week_day}"

        elif n >= 1:
            new_time = f"{new_hour}:{new_minute.zfill(2)} {new_period}, {new_week_day} {days_later}"


    return new_time


add_time("3:00 PM", "3:10")

add_time("11:30 AM", "2:32", "Monday")

add_time("11:43 AM", "00:20")

add_time("10:10 PM", "3:30")

add_time("11:43 PM", "24:20", "tueSday")

add_time("6:30 PM", "205:12")
