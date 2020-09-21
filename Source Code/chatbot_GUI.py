#import modules 
from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk, Image
import database
import tkinter.messagebox
import speaker
import respond
import queue
import threading
import main
from ttkthemes import ThemedStyle

#chat_screen GUI components
def chatbot_screen(root,q):
    import main
    global text_frame, title_label, heading_label, message_box, user_entry, send_button, clear_button, voice_button, voice_button2

    #  Creating the Menu Bar
    menuBar = Menu(root)
    root.config(menu = menuBar)

    voiceMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Chat Options", menu=voiceMenu)
    voiceMenu.add_command(label="Start Voice Chat", command =lambda : run_voice_chat(q, 1))
    voiceMenu.add_command(label="Stop Voice Chat", command = lambda: stop_voice(q))
    
    #  Cascading "Edit" from the Menu Bar and adding commands options
    editMenu= Menu(menuBar, tearoff=0)  
    menuBar.add_cascade(label="Edit", menu=editMenu)

    #  Creating the Fonts Menu
    font = Menu(editMenu, tearoff = 0)
    editMenu.add_cascade(label = "Chat Fonts", menu = font)
    font.add_command(label = "Default Font", command = lambda:default_font())
    font.add_command(label = "Verdana 10", command = lambda:verdana_font())
    font.add_command(label = "Rockwell", command = lambda:rockwell_font())
    font.add_command(label = "Stencil", command = lambda:stencil_font())
    editMenu.add_separator()

    # Creating the Themes Menu
    theme = Menu(editMenu, tearoff = 0)
    editMenu.add_cascade(label = "Themes", menu = theme)
    theme.add_command(label = "Default Theme", command = lambda:default_theme())
    theme.add_command(label = "Grey", command = lambda:grey_theme())
    theme.add_command(label = "Yellow", command = lambda:yellow_theme())
    theme.add_command(label = "Black", command = lambda:black_theme())

    #clears screen
    clearMenu = Menu(editMenu, tearoff = 0, background = '#000099')
    editMenu.add_cascade(label="Clear Screen", command = lambda: clear_screen())

    #clears audio files
    clearsAudio = Menu(editMenu, tearoff = 0, background = '#000099')
    editMenu.add_cascade(label="Clear Residual Files", command = lambda: clear_audiofiles())

    #  Cascading "About" from the Menu Bar and adding commands options
    aboutMenu= Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Info", menu=aboutMenu)    
    aboutMenu.add_command(label="Creators", command = lambda: creators())
    aboutMenu.add_command(label="Help", command = lambda: helps())

    text_frame = Frame(root, bd = 6, bg="#25DBF1")
    text_frame.pack(expand = True, fill = BOTH)

    # Adding the title on the window
    title_label = Label(text_frame, text="Chatbot Cutie", bg="#25DBF1", fg='black', font=('Helvetica', 16, "bold"))
    title_label.pack(side="top", fill="x", pady=10)
        
    #  Adding the message box heading
    heading_label = Label(text_frame, text="Message Box", bg="#25DBF1",  fg='black', font=('Helvetica', 12, "bold"))
    heading_label.place(x = 30, y = 45)

    # Creating the scrollbar for the message box 
    scrollbar = Scrollbar(text_frame, bd=5)
    scrollbar.place(x = 570, y = 70, height = 450)

    # Creating the message box that contains the conversation
    message_box = Text(text_frame, yscrollcommand=scrollbar.set, state=DISABLED,
                        bd=2, padx=10, pady=10, spacing3=8, wrap=WORD, bg=None, font=("Helvetica", "10"), relief=GROOVE,
                        width=10, height=1)
    message_box.place(x = 20, y = 70, height = 450, width = 550)
    scrollbar.config(command=message_box.yview)
        
    #  Entry field for user to input text
    user_entry = Entry(text_frame, bd=2)
    user_entry.place(x= 20, y=530, height=50, width=470)
    user_entry.bind("<Return>", (lambda event: enter_key(q)))

    # Send button 
    send_button = Button(text_frame, text="Send", width=5, bg='white',
                            bd=5, command=lambda : respond_text(q), activebackground="green",
                            font=("Helvetica", "10"), activeforeground="red")
    send_button.place(x= 500, y=530, height=50, width=90)

    clear_button = Button(text_frame, text="Clear Screen", width=5, bg='white',
                            bd=5, command=lambda : clear_screen(), activebackground="green",
                            font=("Helvetica", "10"), activeforeground="red")
    clear_button.place(x= 480, y=20, height=40, width=120)

    voice_button = Button(text_frame, text="Start Voice-Chat", width=5, bg='white',
                            bd=5, command=lambda : run_voice_chat(q, 1), activebackground="green",
                            font=("Helvetica", "10"), activeforeground="red")
    voice_button.place(x= 330, y=590, height=40, width=135)

    voice_button2 = Button(text_frame, text="Stop Voice-Chat", width=5, bg='white',
                            bd=5, command=lambda : stop_voice(q), activebackground="green",
                            font=("Helvetica", "10"), activeforeground="red")
    voice_button2.place(x= 470, y=590, height=40, width=135)

def clear_audiofiles():
    import os, shutil
    folder = 'audio'
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    except:
        pass

def creators():
    creator = Toplevel()
    title = """Creators:"""

    naming = """Laxmi Gurung (s4597925)\nSuman Basnet (s4597797)\nSujan Dhungana (s4601547)"""

    label1 = Label(creator, text=title, height=0, width=100)
    label1.pack()
    label2 = Label(creator, text=naming, height=0, width=100)
    label2.pack()

def default_font():
    fonty = ("Helvetica", 10)
    font1 = ("Helvetica", 16, "bold")
    font2 = ("Helvetica", 12, "bold")
    message_box.config(font=fonty)
    user_entry.config(font=fonty)
    title_label.config(font=font1)
    heading_label.config(font=font2)
    send_button.config(font=fonty)
    clear_button.config(font=fonty)
    voice_button.config(font=fonty)
    voice_button2.config(font=fonty)

def verdana_font():
    fonty = ("Verdana", 10)
    font1 = ("Verdana", 16, "bold")
    font2 = ("Verdana", 12, "bold")
    message_box.config(font=fonty)
    user_entry.config(font=fonty)
    title_label.config(font=font1)
    heading_label.config(font=font2)
    send_button.config(font=fonty)
    clear_button.config(font=fonty)
    voice_button.config(font=fonty)
    voice_button2.config(font=fonty)


def rockwell_font():
    fonty = ("Rockwell", 10)
    font1 = ("Rockwell", 16, "bold")
    font2 = ("Rockwell", 12, "bold")
    message_box.config(font=fonty)
    user_entry.config(font=fonty)
    title_label.config(font=font1)
    heading_label.config(font=font2)
    send_button.config(font=fonty)
    clear_button.config(font=fonty)
    voice_button.config(font=fonty)
    voice_button2.config(font=fonty)
    
def stencil_font():
    fonty = ("Stencil", 10)
    font1 = ("Stencil", 16)
    font2 = ("Stencil", 12)
    message_box.config(font=fonty)
    user_entry.config(font=fonty)
    title_label.config(font=font1)
    heading_label.config(font=font2)
    send_button.config(font=fonty)
    clear_button.config(font=fonty)
    voice_button.config(font=fonty)
    voice_button2.config(font=fonty)

def default_theme():
    text_frame.config(bg = "#25DBF1")
    message_box.config(bg = "white")
    title_label.config(bg = "#25DBF1", fg ="black")
    heading_label.config(bg = "#25DBF1", fg ="black")
    user_entry.config(bg = "white")
    send_button.config(bg='white')
    clear_button.config(bg='white')
    voice_button.config(bg='white')
    voice_button2.config(bg='white')
    style = ThemedStyle(root)
    style.set_theme("breeze")

def grey_theme():
    text_frame.config(bg="grey")
    title_label.config(bg="grey", fg ="white")
    heading_label.config(bg="grey", fg ="white")
    message_box.config(bg="#d3d3d3")
    user_entry.config(bg="#d3d3d3")
    send_button.config(bg='white')
    clear_button.config(bg='white')
    voice_button.config(bg='white')
    voice_button2.config(bg='white')
    style = ThemedStyle(root)
    style.set_theme("equilux")

def yellow_theme():
    text_frame.config(bg="#FFFF66")
    title_label.config(bg="#FFFF66", fg ="black")
    heading_label.config(bg="#FFFF66", fg ="black")
    message_box.config(bg="#FFFF99")
    user_entry.config(bg="#FFFF99")
    send_button.config(bg='#CCCC00')
    clear_button.config(bg='#CCCC00')
    voice_button.config(bg='#CCCC00')
    voice_button2.config(bg='#CCCC00')
    style = ThemedStyle(root)
    style.set_theme("kroc")

def black_theme():
    text_frame.config(bg="black")
    title_label.config(bg="black", fg ="#a9a9a9")
    heading_label.config(bg="black", fg ="#a9a9a9")
    message_box.config(bg="#a9a9a9")
    user_entry.config(bg="#a9a9a9")
    send_button.config(bg='#a9a9a9')
    clear_button.config(bg='#a9a9a9')
    voice_button.config(bg='#a9a9a9')
    voice_button2.config(bg='#a9a9a9')
    style = ThemedStyle(root)
    style.set_theme("kroc")

def helps():
    help_window = Toplevel()
    ABOUT_TEXT = """About

    This chatbot is for everyone to feel good and nice.
    Please send us feedback to improve it more.
    Regards,
    Team"""

    DISCLAIMER = """
    Disclaimer

    Please check manual to look for
    How to run the program?
    
    Regards,
    Team"""

    label1 = Label(help_window, text=ABOUT_TEXT, height=0, width=100)
    label1.pack()
    label2 = Label(help_window, text=DISCLAIMER, height=0, width=100)
    label2.pack()


#function for clearing message_box on chat_screen
def clear_screen():
    message_box.configure(state=NORMAL)
    message_box.delete('1.0', END)
    message_box.configure(state=DISABLED)

#stop voice chat
def stop_voice_chat(q):
    main.run = False
    main.brun = False
    main.crun = False

# if enter key pressed, it sends to respond module
def enter_key(q):
    if not main.chat_check:
        respond_text(q)

#checks if user_input field is empty
def respond_text(q):
    import time
    global user_input
    user_input = user_entry.get()
    user_entry.delete(0, END)
    main.chat_check = True
    if user_input != '':
        send_button.config(state=DISABLED)
        if main.run == True or main.brun == True:
            q.put("***Loading text-chat module")
        stop_voice_chat(q)
        check_task(q)

#checks whether main thread is dead
def check_task(q):
    if not task.is_alive():
        main.crun = True
        response_text(q, user_input)
    else:
        stop_voice_chat(q)
        root.after(200, check_task, q)

def checks_task(q):
    if not task.is_alive():
        return True

#creates a new thread for user_input data
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
    voice_button.config(state=NORMAL)
    voice_button2.config(state=NORMAL)
    check_tasky(q)
    
#checks if tasky thread is dead
def check_tasky(q):
    try:
        if not tasky.is_alive():
            main.crun = False
            main.chat_check = False
            send_button.config(state=NORMAL)
            return True
        else:
            root.after(200, check_tasky, q)
    except:
        pass

def checks_tasky(q):
    try:
        if not tasky.is_alive():
            return True
    except:
        pass

def run_voice_chat(q, n):
    try:
        is_tasky_not_running = checks_tasky(q)
        is_task_not_running = checks_task(q)
        internet = internet_on()
        if n == 1 and internet:
            q.put("***Loading voice-chat module")
        if (is_tasky_not_running or is_task_not_running) and internet:
            main.run = True
            voice_button.config(state=DISABLED)
            voice_button2.config(state=NORMAL)
            thread_create(q,1)
        elif internet:
            root.after(200, run_voice_chat, q, 2)
        else:
            pass
    except:
        pass

def stop_voice(q):
    try:
        if main.irun == True:
            q.put("***Stopping voice-chat module")
        stop_voice_chat(q)
        voice_button2.config(state=DISABLED)
        voice_button.config(state=NORMAL)
    except:
        pass
    

#updates message_box on chat_screen every 200ms
def update_text():
    if not q.empty():
        text = q.get()
        message_box.tag_config('voice', background="#85a7bf", foreground="black")
        message_box.tag_config('text', background="#ad85bf", foreground="black")
        message_box.tag_config('no_internet', background="#ff9e81", foreground="black")
        message_box.tag_config('internet', background="#93bf85", foreground="black")
        message_box.configure(state=NORMAL)
        if text == "***Stopping voice-chat module" or text == "***Loading voice-chat module":
            text = text + "............\n"
            message_box.insert('end', text, 'voice')
        elif text == "***Loading text-chat module":
            text = text + "............\n"
            message_box.insert('end', text, 'text')
        elif text == "Your internet connection is down. Voice-chat is unavailable":
            text = text + "............\n"
            message_box.insert('end', text, 'no_internet')
        elif text == "Your internet connection is up. Voice-chat is now available":
            text = text + "............\n"
            message_box.insert('end', text, 'internet')
        else:
            message_box.insert('end', text)
        message_box.configure(state=DISABLED)
        message_box.see(END)

    root.after(200, update_text) 

def internet_on():
    import socket
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def display_connection(q):
    if main.irun == True and main.jrun == False:
        q.put("Your internet connection is up. Voice-chat is now available")
        internet_check = threading.Thread(target=internet_advice, args = (1,))
        internet_check.daemon = True
        internet_check.start()

        
    elif main.irun == False and main.jrun == True:
        q.put("Your internet connection is down. Voice-chat is unavailable")
        if main.crun == False:
            q.put("***Loading text-chat module")
        internet_check = threading.Thread(target=internet_advice, args = (2,))
        internet_check.daemon = True
        internet_check.start()
        
    else: pass

def internet_advice(n):
    if n == 1:
        speaker.speech_output("Your internet connection is up. Voice-chat is now available")
    elif n == 2:
        speaker.speech_output("Your internet connection is down. Voice-chat is unavailable")
    else:
        pass


def check_internet(q):
    main.irun = internet_on()
    if main.irun == False:
        display_connection(q)
        main.jrun = False
        main.run = False
    else:
        display_connection(q)
        main.jrun = True


        #speaker.offline_output('Your internet connection is down. Voice-chat is unavailable. Text-chat module is running.')
    root.after(200, check_internet, q)

#creates a new thread
def thread_create(q, n):
    global task
    task = threading.Thread(target=main.initial_greeting, args = (q,n))
    task.daemon = True

    if main.irun:
        task.start()


def chat_page_loader(root):
    global q

    q = queue.Queue()

    #style = ThemedStyle(root)
    #style.set_theme("breeze")

    chatbot_screen(root,q)

    update_text()

    check_internet(q)

    thread_create(q,1)

    root.title("Chatbot (Cutie Pie)")
 
def register(root):
    global register_screen
    root.title("Chatbot System: Register")
    register_screen = tk.Frame(root, bg="#25DBF1")
    register_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
 
    global firstN, middleN, lastN, eml, password1, password2, add, nk, error_label
    global fn_entry, mn_entry, ln_entry, em_entry, add_entry, pw1_entry, pw2_entry, nk_entry
    


    firstN = StringVar()
    middleN = StringVar()
    lastN = StringVar()
    eml = StringVar()
    password1 = StringVar()
    password2 = StringVar()
    add = StringVar()
    nk = StringVar()


    Label(register_screen, text="Please enter details below", bg="#25DBF1").pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    # First Name Entry 
    fn_label = Label(register_screen, text="First Name: *", bg="#25DBF1")
    fn_label.pack()
    fn_entry = Entry(register_screen,textvariable=firstN, width=30)
    fn_entry.pack() 
    # Middle Name Entry
    mn_label = Label(register_screen, text="Middle Name (Optional): ", bg="#25DBF1")
    mn_label.pack()
    mn_entry = Entry(register_screen, textvariable=middleN, width=30)
    mn_entry.pack()
    # Last Name Entry
    ln_label = Label(register_screen, text="Last Name: * ", bg="#25DBF1")
    ln_label.pack()
    ln_entry = Entry(register_screen, textvariable=lastN, width=30)
    ln_entry.pack()
    # Email Entry
    em_label = Label(register_screen, text="Email/Username: * ", bg="#25DBF1")
    em_label.pack()
    em_entry = Entry(register_screen, textvariable=eml, width=30)
    em_entry.pack()
    # Password Entries
    pw1_label = Label(register_screen, text="Password: * ", bg="#25DBF1")
    pw1_label.pack()
    pw1_entry = Entry(register_screen, textvariable=password1, show='*', width=30)
    pw1_entry.pack()
    pw2_label = Label(register_screen, text="Confirm Password: * ", bg="#25DBF1")
    pw2_label.pack()
    pw2_entry = Entry(register_screen, textvariable=password2, show='*', width=30)
    pw2_entry.pack()
    # Address Entry
    add_label = Label(register_screen, text="Address (Optional): ", bg="#25DBF1")
    add_label.pack()
    add_entry = Entry(register_screen, textvariable=add, width=30)
    add_entry.pack()
    # Nickname Entry
    nk_label = Label(register_screen, text="Nickname (Optional): ", bg="#25DBF1")
    nk_label.pack()
    nk_entry = Entry(register_screen, textvariable=nk, width=30)
    nk_entry.bind("<Return>", (lambda event: register_user()))
    nk_entry.pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#1FC2D3", command = lambda : register_user()).pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    Button(register_screen, text="Back to Main Page", width=20, height=1, bg="#1FC2D3", command = lambda : backMain(root)).pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    error_label = Label(register_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12))
    error_label.pack()

 
# Designing window for login  
def login(root):
    global login_screen, username_verify, password_verify, username_login_entry, password_login_entry, error_label

    root.title("Chatbot System: Login")
    login_screen = tk.Frame(root, bg="#25DBF1")
    login_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(login_screen, text="Please enter details below to login", bg="#25DBF1").pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
 
    username_verify = StringVar()
    password_verify = StringVar()
     
    Label(login_screen, text="Email/Username * ", bg="#25DBF1").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, width=30)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Label(login_screen, text="Password * ", bg="#25DBF1").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', width=30)
    password_login_entry.bind("<Return>", (lambda event: login_verify(root)))
    password_login_entry.pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Login", width=10, height=1, command = lambda : login_verify(root), bg="#1FC2D3").pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Forgot Password", width=20, height=1, bg="#1FC2D3", command = lambda : forgot_password(root)).pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Back to Main Page", width=20, height=1, bg="#1FC2D3", command = lambda : backMain(root)).pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    error_label = Label(login_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12))
    error_label.pack()

# Implementing event on register button 
def register_user():
    fn = firstN.get()
    mn = middleN.get()
    ln = lastN.get()
    em = eml.get()
    pw1 = password1.get()
    pw2 = password2.get()
    ad = add.get()
    n = nk.get()
    
 
    if (fn=='' or ln=='' or pw1=='' or pw2=='' or em==''):
        error_label.config(text="Please enter the required information")

    elif (pw1 != pw2):
        error_label.config(text="Your passwords do not match!")

    else:
        database.db_insert(fn,mn,ln,em,pw1,ad,n)
        fn_entry.delete(0, END)
        mn_entry.delete(0, END)
        ln_entry.delete(0, END)
        em_entry.delete(0, END)
        pw1_entry.delete(0, END)
        pw2_entry.delete(0, END)
        add_entry.delete(0, END)
        nk_entry.delete(0, END)
        error_label.config(text="Registered!", fg="green")

# Implementing event on login button  
def login_verify(root):
    import main
    e = username_verify.get()
    pw = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    log = database.check_user_data(e, pw)
    
    if log:
        main.users_data(e,pw)
        chat_page_loader(root)
        
    else:
        error_label.config(text="Your password or email is incorrect")

def forgot_password(root):

    global forgot_password_screen, error_label
    forgot_password_screen = tk.Frame(root, bg="#25DBF1")
    forgot_password_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(forgot_password_screen, text="Please enter your registered email.", bg="#25DBF1").pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()
 
    global uname_verify, fname_verify, lname_verify
    uname_verify = StringVar()
    fname_verify = StringVar()
    lname_verify = StringVar()
    global username_reset_entry0, username_reset_entry1, username_reset_entry2
 
    Label(forgot_password_screen, text="Email/Username *", bg="#25DBF1").pack()
    username_reset_entry0 = Entry(forgot_password_screen, textvariable=uname_verify, width=30)
    username_reset_entry0.pack()
    Label(forgot_password_screen, text="First Name *", bg="#25DBF1").pack()
    username_reset_entry1 = Entry(forgot_password_screen, textvariable=fname_verify, width=30)
    username_reset_entry1.pack()
    Label(forgot_password_screen, text="Last Name *", bg="#25DBF1").pack()
    username_reset_entry2 = Entry(forgot_password_screen, textvariable=lname_verify, width=30)
    username_reset_entry2.pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()

    Button(forgot_password_screen, text="Check my details", width=20, height=1, bg="#1FC2D3", command = lambda : check_info()).pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()
    Button(forgot_password_screen, text="Back to main page", command=lambda : backMain(root), bg="#1FC2D3").pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()
    error_label = Label(forgot_password_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12))
    error_label.pack()
    
def check_info():
    u = uname_verify.get()
    fn = fname_verify.get()
    ln = lname_verify.get()
    username_reset_entry0.delete(0, END)
    username_reset_entry1.delete(0, END)
    username_reset_entry2.delete(0, END)
    import database
    checking = database.check_users_data(u, fn, ln)
    if checking:
        reset_password(root)
    else:
        error_label.config(text = "Your details are not correct. Please try again.")



def reset_password(root):
    global reset_pw_screen, error_label
    reset_pw_screen = tk.Frame(root, bg="#25DBF1")
    reset_pw_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(reset_pw_screen, text="Type your new password:", bg="#25DBF1", fg='green').pack()
    Label(reset_pw_screen,text='', bg="#25DBF1").pack()

    global pw1, pw2, pw1_entry, pw2_entry
    pw1 = StringVar()
    pw2 = StringVar()

    Label(reset_pw_screen, text="New Password: *", bg="#25DBF1").pack()
    pw1_entry = Entry(reset_pw_screen, textvariable=pw1, width=30)
    pw1_entry.pack()
    Label(reset_pw_screen, text="Confirm Password *", bg="#25DBF1").pack()
    pw2_entry = Entry(reset_pw_screen, textvariable=pw2, width=30)
    pw2_entry.pack()
    Label(reset_pw_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()
    Button(reset_pw_screen, text="Reset Password", command=lambda : reset_new_password(), bg="#1FC2D3").pack()
    Label(reset_pw_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()
    Button(reset_pw_screen, text="Back to main page", command=lambda : backMain(root), bg="#1FC2D3").pack()
    Label(reset_pw_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()
    error_label = Label(reset_pw_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12))
    error_label.pack()

def reset_new_password():
    p1 = pw1.get()
    p2 = pw2.get()
    pw1_entry.delete(0, END)
    pw2_entry.delete(0, END)

    if (p1 == p2) and (p1 != ""):
        import database
        database.db_password(p1)
        Label(reset_pw_screen, text="Passwords changed!", fg="green", bg="#25DBF1", font=("calibri", 12)).pack()
        Label(reset_pw_screen, text="", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()
        backMain(root)
    else:
        error_label.config(text = "Passwords do not match")


# back to main page
def backMain(root):
    main_account_screen(root)

def main_account_screen(root):
    global main_screen
    root.title("Chatbot System")
    main_screen = tk.Frame(root, bg='#25DBF1')
    main_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    Label(main_screen, text="HI!", fg='white', bg="#25DBF1", font=('Helvetica', 18, "bold", "italic")).pack(side="top", fill="x", pady=10)
    Label(main_screen, text="Please select an option to begin", bg="#25DBF1", font=('Courier', 16, "bold")).pack()
 
    b1 = Button(main_screen, text="Login", command = lambda : login(root), bg="#2568F1", fg="white", font=('Courier', 14, "bold"))
    b1.place(relx=0.2, rely=0.3, relwidth=0.25, relheight=0.15)

    b2 = Button(main_screen, text="Register", command= lambda : register(root), bg="#2568F1", fg="white", font=('Courier', 14, "bold"))
    b2.place(relx=0.55, rely=0.3, relwidth=0.25, relheight=0.15)


def main_loader():
    global root
    root = Tk()
    main_account_screen(root)
    root.geometry("620x640")
    root.resizable(False, False)
    root.iconbitmap('pics/icon.ico')
    import database
    database.db_createdb()
    database.create_admin()
    root.mainloop()

if __name__ == '__main__':
    main_loader()


    


 
 

