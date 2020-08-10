bg_voice = ''

def background_loop():
    import main
    main.empty_count = 0
    main.error_count = 0
    main.error_count0 = 0
    global bg_voice
    bg_voice = record_audio() # get the voice input
    if person_says(["cutie", "hey cutie"]):
        main.initial_greeting()
    else:
        background_loop()

def person_says(terms):
    global bg_voice
    for term in terms:
        if term in bg_voice:
            return True

def record_audio():
    import speech_recognition as sr # recognise speech 
    with sr.Microphone() as source: # microphone as source
        r = sr.Recognizer() # initialise a recogniser
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout = 3, phrase_time_limit = 3)  # listen for the audio via source

            global bg_voice
            bg_voice = ''
            try:
                bg_voice = r.recognize_google(audio)  # convert audio to text
            except sr.UnknownValueError: # error: recognizer does not understand
                #print('Background: I did not get what you meant.')
                bg_voice = ''
            except sr.RequestError:
                #print('Sorry, the service is down') # error: recognizer is not connected
                bg_voice = ''
            except Exception as e:
                        print (str(e))
                        bg_voice = ''
        except Exception:
            #print('Background: I cannot understand you, bruh')
            bg_voice = ''

        if bg_voice != '':
            print("Background sound detection: ", str(bg_voice.lower())) # print what user said
        return str(bg_voice.lower())

def bg_play():
    background_loop()
