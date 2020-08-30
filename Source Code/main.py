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
run = True
brun = True
import respond
import speaker
import recorder

#to check terms in a sentence
def person_says(terms):
    for term in terms:
        if term in voice_data:
            return True

#initial run
def main_page(q):
    while run:
        voice_data = recorder.record_audio("",q) # get the voice input
        #logging()
        respond.response(voice_data, q, 1)
    

def initial_greeting(q,n):
    if n == 1:
        q.put(asis_obj.name+ ": Hi " + person_obj.name + ", How can I help you?\n")
        speaker.speech_output("Hi " + person_obj.name + ", How can I help you?")
    print("\n***Please speak after i finish speaking. I am still learning to hear you as soon as i can.***\n")
    main_page(q)

def listen(ask,q):
    voice_data = recorder.record_audio(ask,q) # get the voice input

def users_data(e,pw):
    import database
    database.get_user_data(e,pw)

#def logging():
    #print("Log 2: Text output from google API received. Responding process begins.....")
    #print(person_obj.name + ": ", voice_data)
