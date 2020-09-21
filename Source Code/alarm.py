import time
from playsound import playsound
import threading
from datetime import datetime

def ask_user():
    try:
        import recorder
        import main
        import queue
        q = queue.Queue()
        main.voice_data = recorder.records_audio("What is the time for alarm?", q)
        current_time = datetime.now().strftime("%H:%M:%S")
        hour, minute, second = current_time.split(':')
        hour, minute, second = int(hour), int(minute), int(second)

        if "a.m." in main.voice_data:
            m = "am"
        elif "p.m." in main.voice_data:
            m = "pm"
        elif (hour > 11):
            m ="pm"
        else:
            m = "am"
        main.voice_data.replace("a.m.", "")
        main.voice_data.replace("p.m.", "")
        h = main.voice_data.split(":")[0]
        if h == '' or hour > 12:
            h = hour
        mi = main.voice_data.split(":")[-1]
        if mi == '' or mi > 60:
            mi = minute + 1
        print("time: "+ str(h)+":"+str(mi)+" "+str(m))
        set_alarm(h,mi,m)
    except Exception as e:
        print(e)

def set_alarm(hour, minute, meridian):
    #taking input from user
    alarmH = int(hour)
    alarmM = int(minute)
    meridian = str(meridian)

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

    #difference in seconds
    total_sec=difference.total_seconds() 

    timer = threading.Timer(total_sec, alarm_func)
    timer.start()
    
def alarm_func():
        import winsound
        winsound.Beep(1000, 1000)

ask_user()