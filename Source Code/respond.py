def response(voice_data, q, n):
    import random #used for random
    import speaker
    import main

    # 1: greeting and convos
    if main.person_says(["hey","hi","hello"]):
        counters()
        greeting = ["hey, how can I help you " + main.person_obj.name, "hey, what's up? " + main.person_obj.name, "I'm listening " + main.person_obj.name, "how can I help you? " + main.person_obj.name, "hello " + main.person_obj.name]
        greet = greeting[random.randint(0,len(greeting)-1)]
        q.put(main.asis_obj.name + ": " + greet + "\n")
        speaker.speech_output(greet)
        

    elif main.person_says(["how are you","what's up"]):
        counters()
        treating = ["I am doing great, " + main.person_obj.name + ". How are you?", "I am fine, " + main.person_obj.name + ". What about you?", "I'm listening to you, " + main.person_obj.name + ". Do you need some help?"]
        treat = treating[random.randint(0,len(treating)-1)]
        q.put(main.asis_obj.name + ": " + treat + "\n")
        speaker.speech_output(treat)

    elif main.person_says(["nice", "fine","I'm good", "thank you"]):
        counters()
        replying = ["That's nice to hear.", "I am happy to hear that.", "I am glad to hear that."]
        reply = replying[random.randint(0,len(replying)-1)]
        q.put(main.asis_obj.name + ": " + reply + "\n")
        speaker.speech_output(reply)

    elif main.person_says(["joke","jokes", "make me laugh"]):
        counters()
        replying = ["Why don't scientists trust atoms? Because........ they make up everything! hehe", "Why doesn't the sun go to college? ..... Because it has a million degrees! buhahaha", "I have many jokes about unemployed people..... sadly none of them work. lol", "What do you call a singing laptop?...... Its A Dell!", "Some people think prison is one word......... but to robbers it's the whole sentence."]
        reply = replying[random.randint(0,len(replying)-1)]
        q.put(main.asis_obj.name + ": " + reply + "\n")
        speaker.speech_output(reply)

    # 2: naming each other and name changes
    elif main.person_says(["what is your name","what's your name","tell me your name"]):
        counters()
        import names
        names.chatbot_name(q)

    elif main.person_says(["what is my name","what's my name","tell me my name"]):
        counters()
        import names
        names.user_name(q)

    elif main.person_says(["change my name"]):
        counters()
        import names
        names.change_name(q)
    
    # 3: quitting program
    elif main.person_says(["exit", "quit", "goodbye", "bye", "bye bye"]):
        counters()
        q.put(main.asis_obj.name + ": " + "Bye! I will miss you! " + main.person_obj.name)
        speaker.speech_output("Bye! I will miss you! " + main.person_obj.name)
        import sys #used for exiting the program
        try:
            sys.exit(0)
        except SystemExit as e:
            sys.exit(e)

    # 4: ask time
    elif main.person_says(["what's the time", "what is the time", "what is current time", "tell me the time","what time"]):
        counters()
        import times
        times.time_speaker(q)

    elif main.person_says(["what's the date", "what is the date", "what is today's adte", "tell me the date","what date"]):
        counters()
        import times
        times.date_speaker(q)
    
    # 5: search google
    elif main.person_says(["search for", "search"]) and 'youtube' not in main.voice_data and 'weather' not in main.voice_data and 'price' not in main.voice_data:
        counters()
        import search
        search.google_search(q)

    # 6: search youtube
    elif main.person_says(["youtube"]):
        counters()
        import search
        search.youtube_search(q)

    #7 rock paper scisorrs
    elif main.person_says(["game"]) and n == 1:
        counters()
        import game
        game.game_rps(q)

    #8 screenshot
    elif main.person_says(["capture my screen","screenshot"]):
        counters()
        import pyautogui #used for screenshot
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screen.png')
        speaker.speech_output("The screen has been captured and placed in drive D as screen.png")

    #9 calculation
    elif main.person_says(["plus","minus","multiply","divide","power","+","-", "x", "*","/", "add", "subtract"]):
        counters()
        import calc
        calc.calculate(q)

    #10: search prices of items
    elif main.person_says(["price of", "price for", "price"]):
        counters()
        import search
        search.price_search(q)

    #11 weather
    elif main.person_says(["weather"]):
        counters()
        import search
        search.weather_search(q)

    #12 definitions
    elif main.person_says(["definition", "definitions", "what is"]):
        counters()
        import search
        search.definitions(q)

    #13 Go background
    elif main.person_says(["go to background", "goto background", "go background"]):
        counters()
        import background
        import speaker
        q.put(main.asis_obj.name + ": " + "I'm going background. Call my name if you need help." + "\n")
        speaker.speech_output("I'm going background. Call my name if you need help.")
        main.brun = False
        background.background_loop(q)

    #14 opening apps
    elif main.person_says(["app", "application"]):
        counters()       
        import apps
        apps.open_app()

    elif main.person_says(["sing me a song", "play a song", "play song"]):
        from playsound import playsound
        playsound('song.mp3')        

    else:
        if main.error_count0 == main.error_count:
            main.empty_count += 1
            #print("RE Non-Related = " + str(main.empty_count))

        if main.empty_count > 2 and n == 1:
           import speaker
           q.put(main.asis_obj.name + ": " + "I'm going background. Call my name if you need help." + "\n")
           speaker.speech_output("I'm going background. Call my name if you need help.")
           import background
           main.brun = True
           background.bg_play(q)
        main.error_count0 = main.error_count

def counters():
    import main
    main.empty_count = 0
    main.error_count = 0
    main.error_count0 = 0