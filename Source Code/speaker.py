def speech_output(audio_string):
    online_output(audio_string)
    

def online_output(audio_string):
    import playsound # to play an audio file
    from gtts import gTTS # google text to speech
    import random
    import os # to remove created audio files
    import main
    audio_string = str(audio_string)
    if audio_string != "":
        tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
        r = random.randint(1,20000000)
        audio_file = 'audio' + str(r) + '.mp3'
        tts.save('audio/'+ audio_file) # save as mp3
        playsound.playsound('audio/' + audio_file) # play the audio file
        spoken_text =   str(main.asis_obj.name) + ": " + str(audio_string)
        #GUI_update(spoken_text)
        print(main.asis_obj.name + ": ", audio_string) # print what app said
        os.remove('audio/' + audio_file) # remove audio file
    else:
        #import speaker
        #speaker.speech_output("Beep")
        main.main_page()
         
def GUI_update(strin):
    import chatbot_GUI
    chat = chatbot_GUI.Chat_Window()
    chat.update_text(strin)

def offline_output(audio_data):
    import pyttsx3
    engine = pyttsx3.init() # object creation driverName='sapi5'

    """ RATE"""
    #rate = engine.getProperty('rate')   # getting details of current speaking rate
    #engine.setProperty('rate', 175)     # setting up new voice rate

    """VOLUME"""
    #volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    #engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(audio_data)
    engine.runAndWait()
    engine.stop()