def calculate(q):
        import main
        import speaker
        data_length = main.voice_data.split(" ")
        length = len(data_length)
        if length > 3:
            opr = main.voice_data.split()[-2]
            ppr = main.voice_data.split()[-4]

            if opr == '+' or opr == 'plus' or ppr == 'add':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                adding = first_num + second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " plus " + str(second_num)+ " is " + str(adding) + "\n")
                speaker.speech_output(str(first_num) + " plus " + str(second_num)+ " is " + str(adding))

            elif opr == '-' or opr == 'minus' or ppr == 'subtract':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                subtracting = first_num - second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " minus " + str(second_num)+ " is " + str(subtracting) + "\n")
                speaker.speech_output(str(first_num) + " minus " + str(second_num)+ " is " + str(subtracting))

            elif opr == 'x' or ppr == 'multiply':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                multiplying = first_num * second_num
                q.put(main.asis_obj.name + ": " + "Multiplication of " + str(first_num) + " and " + str(second_num)+ " is " + str(multiplying) + "\n")
                speaker.speech_output("Multiplication of " + str(first_num) + " and " + str(second_num)+ " is " + str(multiplying))

            elif opr == '/' or ppr == 'divide':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                dividing = first_num / second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " divided by " + str(second_num)+ " is " + str(dividing) + "\n")
                speaker.speech_output(str(first_num) + " divided by " + str(second_num)+ " is " + str(dividing))

            elif opr == 'power':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                powering = first_num ** second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " to the power of " + str(second_num)+ " is " + str(powering) + "\n")
                speaker.speech_output(str(first_num) + " to the power of " + str(second_num)+ " is " + str(powering))

            else:
                q.put(main.asis_obj.name + ": " + "Sorry, I cannot understand the way you ask. For instance, you can ask 'what is 5 + 2?' Or say 'add 5 and 2'" + "\n")
                speaker.speech_output("Sorry, I cannot understand the way you ask. For instance, you can ask 'what is 5 + 2?' Or say 'add 5 and 2'")
        
        elif length == 3:
            opr = main.voice_data.split()[-2]
            ppr = main.voice_data.split()[-3]

            if opr == '+' or opr == 'plus' or ppr == 'add':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                adding = first_num + second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " plus " + str(second_num)+ " is " + str(adding) + "\n")
                speaker.speech_output(str(first_num) + " plus " + str(second_num)+ " is " + str(adding))

            elif opr == '-' or opr == 'minus' or ppr == 'subtract':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                subtracting = first_num - second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " minus " + str(second_num)+ " is " + str(subtracting) + "\n")
                speaker.speech_output(str(first_num) + " minus " + str(second_num)+ " is " + str(subtracting))

            elif opr == 'x' or ppr == 'multiply':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                multiplying = first_num * second_num
                q.put(main.asis_obj.name + ": " + "Multiplication of " + str(first_num) + " and " + str(second_num)+ " is " + str(multiplying) + "\n")
                speaker.speech_output("Multiplication of " + str(first_num) + " and " + str(second_num)+ " is " + str(multiplying))

            elif opr == '/' or ppr == 'divide':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                dividing = first_num / second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " divided by " + str(second_num)+ " is " + str(dividing) + "\n")
                speaker.speech_output(str(first_num) + " divided by " + str(second_num)+ " is " + str(dividing))

            elif opr == 'power':
                first_num = int(main.voice_data.split()[-3])
                second_num = int(main.voice_data.split()[-1])
                powering = first_num ** second_num
                q.put(main.asis_obj.name + ": " + str(first_num) + " to the power of " + str(second_num)+ " is " + str(powering) + "\n")
                speaker.speech_output(str(first_num) + " to the power of " + str(second_num)+ " is " + str(powering))

            else:
                q.put(main.asis_obj.name + ": " + "Sorry, I cannot understand the way you ask. For instance, you can ask 'what is 5 + 2?' Or say 'add 5 and 2'" + "\n")
                speaker.speech_output("Sorry, I cannot understand the way you ask. For instance, you can ask 'what is 5 + 2?' Or say 'add 5 and 2'")
        else:
            q.put(main.asis_obj.name + ": " + "Sorry, I cannot understand the way you ask. For instance, you can ask 'what is 5 + 2?' Or say 'add 5 and 2'" + "\n")
            speaker.speech_output("Sorry, I cannot understand the way you ask. For instance, you can ask 'what is 5 + 2?' Or say 'add 5 and 2'")
