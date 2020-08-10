def open_app():
       import speaker
       import main
       main.listen("What app do you want to open?")
       if main.voice_data != "":
            app = main.voice_data
            executing = "start " + app +".exe" 
            import os
            os.system(executing)
       else:
            speaker.speech_output("Sorry I did not get a new name from you")
            main.main_page()
