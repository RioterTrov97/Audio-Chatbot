def background_loop(q):
    import main
    import speaker
    main.empty_count = 0
    main.error_count = 0
    main.error_count0 = 0
    global bg_voice
    while main.brun:
        bg_voice = record_audio(q) # get the voice input
        if person_says(["cutie", "hey cutie", "qt"]) and main.brun == True:
             q.put(main.asis_obj.name + ": " + "Hi! "+ main.person_obj.name + ", how can I help you?" + "\n")
             speaker.speech_output("Hi! "+ main.person_obj.name + ", how can I help you?")
             main.brun = False
        if main.run == False:
            main.brun == False

def person_says(terms):
    import main
    if main.brun == True:
        for term in terms:
            if term in bg_voice:
                return True

def record_audio(q):
    import main
    if main.brun == True and main.run == True:
        import speech_recognition as sr # recognise speech 
        with sr.Microphone() as source: # microphone as source
            r = sr.Recognizer() # initialise a recogniser
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
                    #if main.run == True or main.brun == True:
                        #q.put("Your internet connection is down. Voice-chat is unavailable")
                        #q.put("***Loading text-chat module")
                        #speaker.offline_output('Your internet connection is down. Voice-chat is unavailable. Text-chat module is running.') # error: recognizer is not connected # error: recognizer is not connected
                    main.run = False
                    main.brun = False

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
    import main
    if main.brun == True and main.run == True:
        background_loop(q)