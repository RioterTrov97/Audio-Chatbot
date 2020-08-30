def background_loop(q):
    import main
    import speaker
    main.empty_count = 0
    main.error_count = 0
    main.error_count0 = 0
    global bg_voice
    bg_voice = record_audio(q) # get the voice input

    while main.brun:
        if person_says(["cutie", "hey cutie", "qt"]):
             q.put(main.asis_obj.name + ": " + "Hi! "+ main.person_obj.name + ", how can I help you?" + "\n")
             speaker.speech_output("Hi! "+ main.person_obj.name + ", how can I help you?")
             main.brun = False

def person_says(terms):
    global bg_voice
    for term in terms:
        if term in bg_voice:
            return True

def record_audio(q):
    import speech_recognition as sr # recognise speech 
    with sr.Microphone() as source: # microphone as source
        r = sr.Recognizer() # initialise a recogniser
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout = 3, phrase_time_limit = 3)  # listen for the audio via source
            bg_voice = ''
            try:
                bg_voice = r.recognize_google(audio)  # convert audio to text
            except sr.UnknownValueError: # error: recognizer does not understand
                bg_voice = ''
                #print('Background: I did not get what you meant.')

            except sr.RequestError:
                #print('Sorry, the service is down') # error: recognizer is not connected
                bg_voice = ''
                import speaker
                q.put(main.asis_obj.name + ": " + 'Sorry, the service is down. Please connect to the internet and try again.' + "\n")
                speaker.offline_output('Sorry, the service is down. Please connect to the internet and try again.')
                import database
                database.join()

            except Exception as e:
                        print (str(e))
                        bg_voice = ''
        except Exception:
            #print('Background: I cannot understand you, bruh')
            bg_voice = ''

        if bg_voice != '':
            print("Background sound detection: ", str(bg_voice.lower())) # print what user said
        return str(bg_voice.lower())

def bg_play(q):
    background_loop(q)