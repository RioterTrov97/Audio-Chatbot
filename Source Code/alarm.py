import time
from playsound import playsound
import threading
from datetime import datetime

def ask_user(q):
    import recorder
    import main
    main.voice_data = recorder.record_audio("What is the time for alarm?", q)



def set_alarm(hour, minute, meridian):
    #taking input from user
    alarmH = hour
    alarmM = minute
    meridian = meridian

    print("Wating for the alarm",alarmH,alarmM,meridian)
    if alarmH == 12 and meridian == 'am':
        alarmH = 0
    elif alarmH < 12 and meridian == 'pm':
        alarmH = alarmH + 12
    else:
        pass
        

    #Current Date Time
    now = datetime.now()

    current_date = now.strftime("%Y-%m-%d")
    year, month, day = current_date.split('-')
    years, months, days = int(year), int(month), int(day)

    #desired alarm time
    later = datetime(years, months, days,alarmH,alarmM,0)

    #calculating the difference between two time
    difference = (later - now)
    print(difference)

    #difference in seconds
    total_sec=difference.total_seconds() 

    timer = threading.Timer(total_sec, alarm_func)
    timer.start()
    
def alarm_func():
        import winsound
        winsound.Beep(440, 250)