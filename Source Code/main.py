#class for a person/user
class person:
    name = ''
    def setName(self, name):
        self.name = name

#class for Rayna
class asis:
    name = ''
    def setName(self, name):
        self.name = name


#default values
person_obj = person()
asis_obj = asis()
asis_obj.name = 'Cutie pie'
person_obj.name = 'Master'
uid = 0
email = ''
voice_data = ''
voice_data1 = ''
empty_count = 0
error_count = 0
error_count0 = 0

#to check terms in a sentence
def person_says(terms):
    for term in terms:
        if term in voice_data:
            return True

#initial run
def main_page():
    import time
    import respond
    while(1):
        listen()
        #logging()
        respond.response(voice_data) # respond

def initial_greeting():
    import speaker
    speaker.speech_output("Hi " + person_obj.name + ", How can I help you?")
    main_page()

def listen(ask = ""):
    import recorder
    voice_data = recorder.record_audio(ask) # get the voice input

#def logging():
    #print("Log 2: Text output from google API received. Responding process begins.....")
    #print(person_obj.name + ": ", voice_data)
