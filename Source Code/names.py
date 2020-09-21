counts = 0
def chatbot_name(q):
    import main
    import speaker
    q.put(main.asis_obj.name + ": " + "I am " + main.asis_obj.name + " and I am your personal digital assistant.\n")
    speaker.speech_output("I am " + main.asis_obj.name + " and I am your personal digital assistant.")

def user_name(q):
    import main
    import speaker
    speaker.speech_output("You are " + main.person_obj.name)

def change_name(q):
    import speaker
    import main
    if main.run == True:
        main.listen("What name do you want me to call you?", q)
        if main.voice_data != "":
            import database
            database.db_nickname(main.voice_data, main.uid, main.email)
            q.put(main.asis_obj.name + ": " + "Your name has been changed. I will call you by the name " + main.person_obj.name+ "\n")
            speaker.speech_output("Your name has been changed. I will call you by the name " + main.person_obj.name)
        else:
            q.put(main.asis_obj.name + ": " + "Sorry I did not get a new name from you. Do you want to try again?\n")
            speaker.speech_output("Sorry I did not get a new name from you. Do you want to try again?")
            name_error(q)
    else:
        pass

def name_error(q):
    try:
        import main
        if main.run == True:
            import recorder
            main.voice_data = recorder.records_audio("", q)
            if main.person_says(["quit", "no", "nope", "nah"]):
                counts = 0
            elif main.person_says(["play", "yes", "sure", "okay", "ok"]):
                change_name(q)
                counts = 0
            else:
                counts += 1
                if counts < 3:
                    name_error(q)
                else:
                    counts = 0
        else:
            pass

    except Exception:
                counts = 0