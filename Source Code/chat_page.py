import tkinter.messagebox
from tkinter import *
# import threading
# import pyttsx3
from PIL import ImageTk, Image
import speaker
import respond
import queue
import threading
import main

def chatbot_screen(root,q):
    import main
    global message_box
    global user_entry

    text_frame = Frame(root, bd = 6, bg="#25DBF1")
    text_frame.pack(expand = True, fill = BOTH)

    # Adding the title on the window
    title_label = Label(text_frame, text="Chatbot Cutie", bg="#25DBF1", fg='white', font=('Helvetica', 18, "bold", "italic"))
    title_label.pack(side="top", fill="x", pady=10)
        
    #  Adding the message box heading
    heading_label = Label(text_frame, text="Message Box", bg="#25DBF1", font=('Verdana', 12, "bold"))
    heading_label.place(x = 50, y = 45)

    # Creating the scrollbar for the message box 
    scrollbar = Scrollbar(text_frame, bd=5)
    scrollbar.place(x = 570, y = 70, height = 450)

    # Creating the message box that contains the conversation
    message_box = Text(text_frame, yscrollcommand=scrollbar.set, state=DISABLED,
                        bd=2, padx=10, pady=10, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                        width=10, height=1)
    message_box.place(x = 20, y = 70, height = 450, width = 550)
    scrollbar.config(command=message_box.yview)
        
    #  Entry field for user to input text
    user_entry = Entry(text_frame, bd=2)
    user_entry.place(x= 20, y=530, height=50, width=470)
    # self.users_message = self.entry_field.get()

    # # frame containing send button and emoji button
    # self.send_button_frame = Frame(self.master, bd=0)
    # self.send_button_frame.pack(fill=BOTH)

    # Send button  
    send_button = Button(text_frame, text="Send", width=5, bg='white',
                            bd=5, command=lambda : respond_text(q), activebackground="green",
                            activeforeground="red")
    send_button.place(x= 500, y=530, height=50, width=90)

    clear_button = Button(text_frame, text="Clear Screen", width=5, bg='white',
                            bd=5, command=lambda : clear_screen(), activebackground="green",
                            activeforeground="red")
    clear_button.place(x= 500, y=585, height=40, width=90)

def clear_screen():
    message_box.configure(state=NORMAL)
    message_box.delete('1.0', END)
    message_box.configure(state=DISABLED)


def respond_text(q):
    import time
    global user_input
    user_input = user_entry.get()    
    if user_input != '':
        main.run = False
        main.brun = False
        q.put("Loading...\n")
        check_task(q)

def check_task(q):
    if not task.is_alive():
        response_text(q, user_input)
    else:
        root.after(200, check_task, q)


def response_text(q, user_input):
    import respond
    import database
    global tasky
    q.put(main.person_obj.name + ": " + user_input + "\n")
    user_input = user_input.lower()
    main.voice_data = str(user_input)
    tasky = threading.Thread(target=respond.response, args = (user_input, q, 2))
    tasky.daemon = True
    tasky.start()
    check_tasky(q)
    

def check_tasky(q):
    if not tasky.is_alive():
        q.put("Loading...\n")
        main.run = True
        thread_create(q,0)
    else:
        root.after(200, check_tasky, q)

  
def update_text():
    if not q.empty():
        text = q.get()
        message_box.configure(state=NORMAL)
        message_box.insert('end', text)
        message_box.configure(state=DISABLED)

    root.after(200, update_text)

def user_data(e,pw):
    main.users_data(e,pw)

def thread_create(q, n):
    global task
    task = threading.Thread(target=main.initial_greeting, args = (q,n))
    task.daemon = True
    task.start()

def chat_page_loader():
    global root, q
    root = Tk()

    q = queue.Queue()

    chatbot_screen(root,q)

    update_text()
    thread_create(q,1)

    root.geometry("620x640")
    root.title("Chatbot (Cutie)")

    root.mainloop()

if __name__ == '__main__':
    chat_page_loader()
    

