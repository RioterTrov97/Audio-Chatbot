count = 0

def game_rps(q):
    import speaker
    import main
    q.put(main.asis_obj.name + ": " + "Yay! I know a game we both can play. It is called rock paper and scissor." + "\n")
    speaker.speech_output("Yay! I know a game we both can play. It is called rock paper and scissor.")
    core(q)

def core(q):
    import main
    import speaker
    import recorder

    moves=["rock", "paper", "scissor"]
    pmoves=["rock", "paper", "scissor", "caesar", "peppa"]
    main.voice_data = recorder.record_audio("Choose among rock, paper or scissor:", q)
    
    if main.voice_data not in pmoves:
        q.put(main.asis_obj.name + ": " + "Sorry I did not understand. Would you like to try again?" + "\n")
        speaker.speech_output("Sorry I did not understand. Would you like to try again?")
        error(q)
    else:
        import random
        cmove=random.choice(moves)
        pmove=main.voice_data

        pmove = name_check(pmove)

        q.put(main.asis_obj.name + ": " + "You chose " + pmove + "\n")            
        speaker.speech_output("You chose " + pmove)

        q.put(main.asis_obj.name + ": " + "I chose " + cmove + "\n")
        speaker.speech_output("I chose " + cmove)
    
        if pmove==cmove or (pmove== "peppa" and cmove == "paper") or (pmove== "caesar" and cmove == "scissor"):
            q.put(main.asis_obj.name + ": " + "The match is draw. Haha. We both are out of luck today." + "\n")
            speaker.speech_output("The match is draw. Haha. We both are out of luck today.")
        elif pmove== "rock" and cmove== "scissor":
            q.put(main.asis_obj.name + ": " + "Scissor crushes rock. You won " + main.person_obj.name + "! You are quite lucky today." + "\n")
            speaker.speech_output("Scissor crushes rock. You won " + main.person_obj.name + "! You are quite lucky today." )
        elif pmove== "rock" and cmove== "paper":
            q.put(main.asis_obj.name + ": " + "Paper beats rock. You lost " + main.asis_obj.name + ". Sorry, "+ main.person_obj.name + ", I am luckier than you today!" + "\n")
            speaker.speech_output("Paper beats rock. You lost " + main.asis_obj.name + ". Sorry, "+ main.person_obj.name + ", I am luckier than you today!")
        elif (pmove== "paper" or pmove== "peppa") and cmove== "rock":
            q.put(main.asis_obj.name + ": " + "Paper beats rock. You won " + main.person_obj.name+ "! Looks like someone is luckier today!" + "\n")
            speaker.speech_output("Paper beats rock. You won " + main.person_obj.name+ "! Looks like someone is luckier today!")
        elif (pmove== "paper" or pmove== "peppa") and cmove== "scissor":
            q.put(main.asis_obj.name + ": " + "Scissor cuts paper. You lost " + main.asis_obj.name + "! I hope i did not play you out. hehe." + "\n")
            speaker.speech_output("Scissor cuts paper. You lost " + main.asis_obj.name + "! I hope i did not play you out. hehe.")
        elif (pmove== "scissor" or pmove== "caesar") and cmove== "paper":
            q.put(main.asis_obj.name + ": " + "Scissor cuts paper. You're the winner " + main.person_obj.name + ". Aha! You're awesome." + "\n")
            speaker.speech_output("Scissor cuts paper. You're the winner " + main.person_obj.name + ". Aha! You're awesome.")
        elif (pmove== "scissor" or pmove== "caesar") and cmove== "rock":
            q.put(main.asis_obj.name + ": " + "Scissor crushes rock. I'm the winner " + main.asis_obj.name + "! I love rock and roll! Haha" + "\n")
            speaker.speech_output("Scissor crushes rock. I'm the winner " + main.asis_obj.name + "! I love rock and roll! Haha")

        main.voice_data = recorder.records_audio("Do you want to play again?", q)
        if main.person_says(["quit", "no", "nope", "nah"]):
            main.main_page(q)
        elif main.person_says(["play", "yes", "sure", "okay", "ok"]):
            core(q)
        else:
            q.put(main.asis_obj.name + ": " + "Sorry I did not understand. Would you like to try again?" + "\n")
            speaker.speech_output("Sorry I did not understand. Would you like to try again?")
            error(q)


def name_check(pmove):
    if (pmove == "caesar"):
        pmove = "scissor"
        return (pmove)
    elif (pmove == "peppa"):
        pmove = "paper"
        return (pmove)
    else:
        pmove = pmove
        return (pmove)


def error(q):
    try:
        import main
        import recorder
        main.voice_data = recorder.records_audio("", q)
        if main.person_says(["quit", "no", "nope", "nah"]):
            count = 0
            main.main_page(q)
        elif main.person_says(["play", "yes", "sure", "okay", "ok"]):
            count = 0
            core(q)
        else:
            count += 1
            if count < 3:
                error(q)
            else:
                count = 0
                main.main_page(q)
    except Exception:
                count = 0
                main.main_page(q)
