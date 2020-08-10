def record_audio(ask = ""):
    import main
    import speaker
    import speech_recognition as sr # recognise speech
     
    with sr.Microphone() as source: # microphone as source
        if ask:
            speaker.speech_output(ask)
        r = sr.Recognizer() # initialise a recogniser
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout = 3, phrase_time_limit = 4)  # listen for the audio via source
            main.voice_data = ''
            try:
                main.voice_data = r.recognize_google(audio)  # convert audio to text

            except sr.UnknownValueError: # error: recognizer does not understand
                #print('UnknownValueError: I did not get you.')
                main.empty_count += 1
                main.error_count += 1
                #print("UR Non-Related = " + str(main.empty_count))
                main.voice_data = ''

            except sr.WaitTimeoutError as e:
                print("Timeout; {0}".format(e))
                print('Please say something')
                main.voice_data == ''

            except sr.RequestError:
                speaker.speech_output('Sorry, the service is down') # error: recognizer is not connected
                main.error_count += 1
                voice_data = ''

            except Exception as e:
                print (str(e))
                main.error_count += 1
                voice_data = ''

        except Exception:
            #print('Exception: Phrase not detected')
            main.empty_count += 1
            main.error_count += 1
            #print("EX Non-Related = " + str(main.empty_count))
            main.voice_data = ''
        
        main.voice_data = str(main.voice_data.lower())
        if main.voice_data != '':
            print(main.person_obj.name + ": " + str(main.voice_data)) # print what user said
        return str(main.voice_data)