count = 0

def game_rps():
    import speaker
    speaker.speech_output("Yay! I know a game we both can play. It is called rock paper and scissor. ")
    core()

def core():
    import main
    import speaker
    import recorder

    main.voice_data = recorder.record_audio("Choose among rock, paper or scissor:")
    moves=["rock", "paper", "scissor"]
    pmoves=["rock", "paper", "scissor", "caesar"]
    
    if main.voice_data not in pmoves:
        error()
    else:
        import random
        cmove=random.choice(moves)
        pmove=main.voice_data

        speaker.speech_output("I chose " + cmove)
        speaker.speech_output("You chose " + pmove)
    
        if pmove==cmove:
            speaker.speech_output("The match is draw. Haha. We both are out of luck today.")
        elif pmove== "rock" and cmove== "scissor":
            speaker.speech_output("The winner is " + main.person_obj.name + "! You are quite lucky today." )
        elif pmove== "rock" and cmove== "paper":
            speaker.speech_output("The winner is " + main.asis_obj.name + ". Sorry, "+ main.person_obj.name + " I am luckier than you today!")
        elif pmove== "paper" and cmove== "rock":
            speaker.speech_output("The winner is " + main.person_obj.name+ "! Looks like someone is luckier today!")
        elif pmove== "paper" and cmove== "scissor":
            speaker.speech_output("The winner is " + main.asis_obj.name + "! I hope i did not play you out. hehe.")
        elif (pmove== "scissor" or pmove== "caesar") and cmove== "paper":
            speaker.speech_output("The winner is " + main.person_obj.name + ". Aha! You're awesome.")
        elif (pmove== "scissor" or pmove== "caesar") and cmove== "rock":
            speaker.speech_output("The winner is " + main.asis_obj.name + "! I love rock and roll!")

        main.voice_data = recorder.record_audio("Do you want to play again? You can say 'quit' to quit the game. Or say 'play' to play again.")
        if main.person_says(["quit"]):
            main.main_page()
        elif main.person_says(["play"]):
            core()
        else:
            error()

def error():
    import main
    import recorder
    main.voice_data = recorder.record_audio("Sorry I did not understand you! You can say 'quit' to quit the game. Or say 'try' to try again.")
    if main.person_says(["quit"]):
        main.main_page()
    elif main.person_says(["try"]):
        core()
    else:
        count += 1
        if count < 2:
            error()
        else:
            count = 0
            main.main_page()