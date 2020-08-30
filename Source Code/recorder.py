def record_audio(ask, q):
    import main
    import speaker
    import speech_recognition as sr # recognise speech
     
    with sr.Microphone() as source: # microphone as source
        if ask:
            q.put(main.asis_obj.name + ": " + ask + "\n")
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
                main.error_count += 1
                main.voice_data == ''

            except sr.RequestError:
                q.put('Sorry, the service is down. Please connect to the internet and try again.')
                speaker.offline_output('Sorry, the service is down. Please connect to the internet and try again.') # error: recognizer is not connected
                main.error_count += 1
                voice_data = ''
                import database
                database.join()

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
        text = main.voice_data
        if main.voice_data != '':
            print(main.person_obj.name + ": " + main.voice_data) # print what user said
            q.put(main.person_obj.name + ": " + main.voice_data + "\n")
        return str(main.voice_data)

def records_audio(ask, q):
    import main
    import speaker
    import speech_recognition as sr # recognise speech
     
    with sr.Microphone() as source: # microphone as source
        if ask:
            q.put(main.asis_obj.name + ": " + ask + "\n")
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
                #print("UR Non-Related = " + str(main.empty_count))
                main.voice_data = ''

            except sr.WaitTimeoutError as e:
                print("Timeout; {0}".format(e))
                print('Please say something')
                main.voice_data == ''

            except sr.RequestError:
                q.put('Sorry, the service is down. Please connect to the internet and try again.')
                speaker.offline_output('Sorry, the service is down. Please connect to the internet and try again.') # error: recognizer is not connected1
                voice_data = ''
                import database
                database.join()

            except Exception as e:
                print (str(e))
                voice_data = ''

        except Exception:
            #print('Exception: Phrase not detected')
            #print("EX Non-Related = " + str(main.empty_count))
            main.voice_data = ''
        
        main.voice_data = str(main.voice_data.lower())
        if main.voice_data != '':
            print(main.person_obj.name + ": " + str(main.voice_data)) # print what user said
            q.put(main.person_obj.name + ": " + main.voice_data + "\n")
        return str(main.voice_data)