def chatbot_name():
    import main
    import speaker
    speaker.speech_output("I am " + main.asis_obj.name + " and I am your personal digital assistant.")

def user_name():
    import main
    import speaker
    speaker.speech_output("You are " + main.person_obj.name)

def change_name():
    import speaker
    import main
    main.listen("What name do you want me to call you?")
    if main.voice_data != "":
        import database
        database.db_nickname(main.voice_data,main.uid, main.email)
        speaker.speech_output("Your name has been changed. I will call you by the name " + main.person_obj.name + ". Need any help?")
    else:
        speaker.speech_output("Sorry I did not get a new name from you")
        change_name()