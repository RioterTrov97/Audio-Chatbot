def response(voice_data):
    import random #used for random
    import speaker
    import main

    # 1: greeting and convos
    if main.person_says(["hey","hi","hello"]):
        greeting = ["hey, how can I help you " + main.person_obj.name, "hey, what's up? " + main.person_obj.name, "I'm listening " + main.person_obj.name, "how can I help you? " + main.person_obj.name, "hello " + main.person_obj.name]
        greet = greeting[random.randint(0,len(greeting)-1)]
        speaker.speech_output(greet)
        counters()
        

    elif main.person_says(["how are you","what's up"]):
        treating = ["I am doing great, " + main.person_obj.name + ". How are you?", "I am fine, " + main.person_obj.name + ". What about you?", "I'm listening to you, " + main.person_obj.name + ". Do you need some help?"]
        treat = treating[random.randint(0,len(treating)-1)]
        speaker.speech_output(treat)
        counters()

    elif main.person_says(["nice", "fine","I'm good", "thank you"]):
        replying = ["That's nice to hear.", "I am happy to hear that.", "I am glad to hear that."]
        reply = replying[random.randint(0,len(replying)-1)]
        speaker.speech_output(reply)
        counters()

    elif main.person_says(["joke","jokes", "make me laugh"]):
        replying = ["Why don't scientists trust atoms? Because........ they make up everything! hehe", "Why doesn't the sun go to college? ..... Because it has a million degrees! buhahaha", "I have many jokes about unemployed people..... sadly none of them work. lol", "What do you call a singing laptop?...... Its A Dell!", "Some people think prison is one word......... but to robbers it's the whole sentence."]
        reply = replying[random.randint(0,len(replying)-1)]
        speaker.speech_output(reply)
        counters()

    # 2: naming each other and name changes
    elif main.person_says(["what is your name","what's your name","tell me your name"]):
        import names
        names.chatbot_name()
        counters()

    elif main.person_says(["what is my name","what's my name","tell me my name"]):
        import names
        names.user_name()
        counters()

    elif main.person_says(["change my name"]):
        import names
        names.change_name()
        counters()
    
    # 3: quitting program
    elif main.person_says(["exit", "quit", "goodbye", "bye", "bye bye"]):
        speaker.speech_output("Bye! I will miss you! " + main.person_obj.name)
        import sys #used for exiting the program
        try:
            sys.exit(0)
        except SystemExit as e:
            sys.exit(e)
        counters()

    # 4: ask time
    elif main.person_says(["what's the time", "what is the time", "what is current time", "tell me the time","what time"]):
        import times
        times.time_speaker()
        counters()

    elif main.person_says(["what's the date", "what is the date", "what is today's adte", "tell me the date","what date"]):
        import times
        times.date_speaker()
        counters()
    
    # 5: search google
    elif main.person_says(["search for", "search"]) and 'youtube' not in main.voice_data and 'weather' not in main.voice_data:
        import search
        search.google_search()
        counters()

    # 6: search youtube
    elif main.person_says(["youtube"]):
        import search
        search.youtube_search()
        counters()

    #7 rock paper scisorrs
    elif main.person_says(["game"]):
        import game
        game.game_rps()
        counters()

    #8 screenshot
    elif main.person_says(["capture my screen","screenshot"]):
        import pyautogui #used for screenshot
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screen.png')
        speaker.speech_output("The screen has been captured and placed in drive D as screen.png")
        counters()

    #9 calculation
    elif main.person_says(["plus","minus","multiply","divide","power","+","-","*","/", "add", "subtract"]):
       import calc
       calc.calculate()
       counters()

    #10: search prices of items
    elif main.person_says(["price of", "price for"]):
        import search
        search.price_search()
        counters()

    #11 weather
    elif main.person_says(["weather"]):
        import search
        search.weather_search()
        counters()

    #12 definitions
    elif main.person_says(["definition", "definitions", "what is"]):
        import search
        search.definitions()
        counters()

    #11 opening apps
    elif main.person_says(["app", "application"]):
       import apps
       apps.open_app()
       counters()

    else:
        if main.error_count0 == main.error_count:
            main.empty_count += 1
            #print("RE Non-Related = " + str(main.empty_count))

        if main.empty_count > 2:
            import speaker
            speaker.speech_output("I'm going background. Call my name if you need help.")
            import background
            background.bg_play()
        main.error_count0 = main.error_count

def counters():
    import main
    main.empty_count = 0
    main.error_count = 0
    main.error_count0 = 0