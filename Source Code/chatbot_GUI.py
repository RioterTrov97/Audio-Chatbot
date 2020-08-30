#import modules
 
from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk, Image
import database


# def send(event=None):
#     global msg
#     msg = EntryBox.get("1.0",'end-1c').strip()
#     EntryBox.delete("0.0",END)
    
#     if msg != '':
#         ChatBox.config(state=NORMAL)
#         # tts = gTTS(msg)
#         # response(msg)
#         # resMsg = speaker.text_output(response(msg))
#         ChatBox.insert(END, "Master: " + msg + '\n\n')
#         ChatBox.config(foreground="#442265", font=("Verdana", 12 ))
#         chatbot_res = response(msg)
#         ChatBox.insert(END, "Rayna: " + chatbot_res + '\n\n')
#         ChatBox.config(state=DISABLED)
#         ChatBox.yview(END)

# Designing window for registration
 
def register(root):
    global register_screen
    root.title("Chatbot System: Register")
    register_screen = tk.Frame(root, bg="#25DBF1")
    register_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
 
    global firstN, middleN, lastN, eml, password1, password2, add, nk
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
    em_label = Label(register_screen, text="Email: * ", bg="#25DBF1")
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
    nk_entry.pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#1FC2D3", command = lambda : register_user()).pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    Button(register_screen, text="Back to Main Page", width=20, height=1, bg="#1FC2D3", command = lambda : backMain_register(root)).pack()

 
# Designing window for login 
 
def login(root):
    global login_screen
    root.title("Chatbot System: Login")
    login_screen = tk.Frame(root, bg="#25DBF1")
    login_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(login_screen, text="Please enter details below to login", bg="#25DBF1").pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
    
    
    Label(login_screen, text="Email * ", bg="#25DBF1").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, width=30)
    username_login_entry.pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Label(login_screen, text="Password * ", bg="#25DBF1").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', width=30)
    password_login_entry.pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Login", width=10, height=1, command = lambda : login_verify(root), bg="#1FC2D3").pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Forgot Password", width=20, height=1, bg="#1FC2D3", command = lambda : forgot_password(root)).place(x = 50, y = 220)
    # Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Back to Main Page", width=20, height=1, bg="#1FC2D3", command = lambda : backMain_login(root)).place(x = 250, y = 220)

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
        Label(register_screen, text="Please enter the required information", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()

    else:
        password_check(pw1, pw2)
        database.db_insert(fn,mn,ln,em,pw1,ad,n)
        # registered_label = Label(register_screen, text="Registration Success!", fg="green", bg="#25DBF1", font=("calibri", 12)).pack() 

# Implementing event on login button 
 
def login_verify(root):
    import main
    e = username_verify.get()
    pw = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    log = database.check_user_data(e, pw)
    
    if log:
        root.destroy()
        import chat_page
        chat_page.user_data(e,pw)
        chat_page.chat_page_loader()

    else:
        user_not_found(root)
    

def password_check(pw1, pw2):
    
    if (pw1 != pw2):
        Label(register_screen, text="Your passwords do not match. Please try again.", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()
        pw1_entry.delete(0, END)
        pw2_entry.delete(0, END)


    else:
        fn_entry.delete(0, END)
        mn_entry.delete(0, END)
        ln_entry.delete(0, END)
        em_entry.delete(0, END)
        pw1_entry.delete(0, END)
        pw2_entry.delete(0, END)
        add_entry.delete(0, END)
        nk_entry.delete(0, END)
        Label(register_screen, text="Registered!", fg="green", bg="#25DBF1", font=("calibri", 12)).pack()

def forgot_password(root):

    global forgot_password_screen
    forgot_password_screen = tk.Frame(root, bg="#25DBF1")
    forgot_password_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(forgot_password_screen, text="Please enter your registered email.", bg="#25DBF1").pack()
    Label(forgot_password_screen, text="*The link to reset your password will be sent to the email you have entered below*",fg='green', bg="#25DBF1").pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()
 
    global username_verify
    username_verify = StringVar()
    global username_reset_entry
 
    Label(forgot_password_screen, text="Email *", bg="#25DBF1").pack()
    username_reset_entry = Entry(forgot_password_screen, textvariable=username_verify, width=50)
    username_reset_entry.pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()

    Button(forgot_password_screen, text="Send Link", width=10, height=1, bg="#1FC2D3", command = lambda : backMain_login(root)).pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()

# def verify_username():
#     username1 = username_verify.get()
#     username_login_entry.delete(0, END)
 
#     list_of_files = os.listdir()
#     if username1 in list_of_files:
#         file1 = open(username1, "r")
#         verify = file1.read().splitlines()
#         reset_link()
#     else:
#         Label(forgot_password_screen, text="Email not registered",fg='red', bg="#25DBF1").pack()
# # Designing Chatbot Interface
# def chatbot_interface():

# Designing popup for login success
 
# def login_sucess():
#     global login_success_screen
#     login_success_screen = Toplevel(login_screen)
#     login_success_screen.title("Success")
#     login_success_screen.geometry("150x100")
#     Label(login_success_screen, text="Login Successful").pack()
#     Button(login_success_screen, text="OK", command=delete_login_success).pack()

def reset_link(root):
    global reset_link_screen
    reset_link_screen = tk.Frame(root, bg="#25DBF1")
    reset_link_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(reset_link_screen, text="Reset password link sent to your email!", bg="#25DBF1", fg='green').pack()
    Label(reset_link_screen,text='', bg="#25DBF1").pack()
    Button(reset_link_screen, text="OK", command=lambda : delete_reset_link(root), bg="#1FC2D3").pack()
 
# Designing popup for login invalid password
 
def password_not_recognised(root):
    global password_not_recog_screen
    root.title("ERROR!")
    password_not_recog_screen = tk.Frame(root, bg="#25DBF1")
    password_not_recog_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(password_not_recog_screen, text="Invalid Password!", fg="red", bg="#25DBF1").pack()
    Label(password_not_recog_screen, text="Please try again", fg="red", bg="#25DBF1").pack()
    Label(password_not_recog_screen, text="", bg="#25DBF1").pack()
    Button(password_not_recog_screen, text="OK", command=lambda : delete_password_not_recognised(root), bg="#1FC2D3").pack()
 
# Designing popup for user not found
 
def user_not_found(root):

    global user_not_found_screen
    root.title("ERROR!")
    user_not_found_screen = tk.Frame(root, bg="#25DBF1")
    user_not_found_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    Label(user_not_found_screen, text="Your email or password is incorrect.", fg="red", bg="#25DBF1").pack()
    Label(user_not_found_screen, text="Please try again", fg="red", bg="#25DBF1").pack()
    Label(user_not_found_screen, text="", bg="#25DBF1").pack()
    
    Button(user_not_found_screen, text="OK", command=lambda : delete_user_not_found_screen(root), bg="#1FC2D3").pack()
    Label(user_not_found_screen, text="", bg="#25DBF1").pack()


# Deleting popups
def backMain_login(root):
    main_account_screen(root)

def backMain_register(root):
    main_account_screen(root)


def delete_login(root):
    login(root)
 
 
def delete_password_not_recognised(root):
    login(root)
 
 
def delete_user_not_found_screen(root):
    login(root)

def delete_reset_link(root):
    login(root)

# def logout():
#     chatbot_screen.destroy()
 
# Designing Main(first) window
 
def main_account_screen(root):

    #canvas = tk.Canvas(height=100, width=800)
    #canvas.pack()
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
    root = Tk()
    main_account_screen(root)
    root.geometry("620x640")
    import database
    database.db_createdb()
    database.create_admin()
    root.mainloop()


main_loader()
 
 

