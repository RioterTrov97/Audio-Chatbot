def time_speaker(q):
        from datetime import datetime
        import speaker
        import main
        current_time = datetime.now().strftime("%H:%M:%S")
        hour, minute, second = current_time.split(':')
        hours, minutes, seconds = int(hour), int(minute), int(second)
        if hours > 12 and hours < 24:
            meridian = "pm"
            hours = hours - 12
        elif hours == 24:
            meridian = "am"
            hours = hours - 12
        elif hours == 12:
            meridian = "pm"
        else:
            meridian ="am"

        time = "The current time is " + str(hours) + ":" + str(minutes) + meridian + "."
        #print("Current time = " + time)
        q.put(main.asis_obj.name + ": " + time + "\n")
        speaker.speech_output(time)

def date_speaker(q):
        from datetime import datetime
        import speaker
        import main

        month_name = "January"
        day_note = "st"

        current_date = datetime.now().strftime("%Y-%m-%d")
        year, month, day = current_date.split('-')
        years, months, days = int(year), int(month), int(day)
        if months == 1:
            month_name = "January"
        elif months == 2:
            month_name = "February"
        elif months == 3:
            month_name = "March"
        elif months == 4:
            month_name = "April"
        elif months == 5:
            month_name = "May"
        elif months == 6:
            month_name = "June"
        elif months == 7:
            month_name = "July"
        elif months == 8:
            month_name = "August"
        elif months == 9:
            month_name = "September"
        elif months == 10:
            month_name = "October"
        elif months == 11:
            month_name = "November"
        else:
            month_name = "December"
        
        if days == 1 or days == 11 or days == 21 or days == 31:
            day_note = "st"
        elif days == 2 or days == 12 or days == 22:
            day_note = "nd"
        elif days == 2 or days == 12 or days == 22:
            day_note = "rd"
        else:
            day_note = "th"

        date = "Today is " + str(days) + day_note + " of " + month_name + ", " + str(years)
        q.put(main.asis_obj.name + ": " + date + "\n")
        speaker.speech_output(date)

def greeter(q):
    from datetime import datetime
    import speaker
    import main
    current_time = datetime.now().strftime("%H:%M:%S")
    hour, minute, second = current_time.split(':')
    hours = int(hour)
    if (hours > 4) and (hours < 12):
        q.put(main.asis_obj.name + ":" + "Good Morning! " + main.person_obj.name +"\n")
        speaker.speech_output("Good Morning! " + main.person_obj.name)

    elif (hours == 12):
        q.put(main.asis_obj.name + ": " + "Good Noon! " + main.person_obj.name + "\n")
        speaker.speech_output("Good Noon! " + main.person_obj.name)

    elif (hours > 12) and (hours < 18):
        q.put(main.asis_obj.name + ": " + "Good Afternoon! " + main.person_obj.name + "\n")
        speaker.speech_output("Good Afternoon! " + main.person_obj.name)

    elif (hours >= 18) and (hours < 20):
        q.put(main.asis_obj.name + ": " + "Good Evening! " + main.person_obj.name + "\n")
        speaker.speech_output("Good Evening! " + main.person_obj.name)

    else:
        q.put(main.asis_obj.name + ": " + "Good Night! " + main.person_obj.name + "\n")
        speaker.speech_output("Good Night! " + main.person_obj.name)
