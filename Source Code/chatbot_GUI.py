#import modules
 
from tkinter import *
import os
import tkinter as tk
from PIL import ImageTk, Image
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen, bg="#25DBF1")
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    global name_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="#25DBF1").pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    name_lable = Label(register_screen, text="Name ", bg="#25DBF1")
    name_lable.pack()
    name_entry = Entry(register_screen, width=30)
    name_entry.pack()
    username_lable = Label(register_screen, text="Email * ", bg="#25DBF1")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, width=30)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ", bg="#25DBF1")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', width=30)
    password_entry.pack()
    password_lable = Label(register_screen, text="Confirm Password * ", bg="#25DBF1")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', width=30)
    password_entry.pack()
    Label(register_screen, text="", bg="#25DBF1").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="#1FC2D3", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen, bg="#25DBF1")
    login_screen.title("Login")
    login_screen.geometry("300x250")
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
    Button(login_screen, text="Login", width=10, height=1, command = login_verify, bg="#1FC2D3").pack()
    Label(login_screen, text="", bg="#25DBF1").pack()
    Button(login_screen, text="Forgot Password", width=20, height=1, bg="#1FC2D3", command = forgot_password).pack()

# Designing window for Chatbot application
def chatbotScreen():
    global chatbot_screen
    chatbot_screen = Toplevel(main_screen, bg="#25DBF1")
    chatbot_screen.title("CHATBOT (Rayna)")
    chatbot_screen.geometry("300x250")
    Label(chatbot_screen, text="Chatbot Rayna", fg='white', bg="#25DBF1", font=('Helvetica', 18, "bold", "italic")).pack(side="top", fill="x", pady=10)
    Label(chatbot_screen, text="", bg="#25DBF1").pack()

    img = PhotoImage(file="small.png")

    Label(chatbot_screen, image=img)
    Label(chatbot_screen, text="Message Box", bg="#25DBF1", font=('Courier', 15, "bold")).place(relx=0.05, rely=0.1, relwidth=0.25, relheight=0.1)
    Entry(chatbot_screen, bg='white').place(relx=0.05, rely=0.2, relwidth=0.7, relheight=0.4)
    Entry(chatbot_screen, bg='white').place(relx=0.05, rely=0.65, relwidth=0.7, relheight=0.1)
    Button(chatbot_screen, text="Enter", bg='red', fg='white', font=('Courier', 14, "bold")).place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.1)
    Button(chatbot_screen, image=img, bg="#25DBF1").place(relx=0.8, rely=0.35, relwidth=0.1, relheight=0.1)
    Button(chatbot_screen, text="Logout", bg="red", fg="white", font=('Courier', 14, "bold"), command = logout).place(relx=0.35, rely=0.8, relwidth=0.2, relheight=0.1)

 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    if (username_info=='' or password_info==''):
    
        Label(register_screen, text="Please enter the required information", fg="red", bg="#25DBF1", font=("calibri", 12)).pack()
    
    else:
    
      file = open(username_info, "w")
      file.write(username_info + "\n")
      file.write(password_info)
      file.close()
 
      username_entry.delete(0, END)
      password_entry.delete(0, END)
      name_entry.delete(0, END) 
      Label(register_screen, text="Registration Success!", fg="green", bg="#25DBF1", font=("calibri", 12)).pack() 
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            delete_login()
            chatbotScreen()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()

def forgot_password():

    global forgot_password_screen
    forgot_password_screen = Toplevel(main_screen, bg="#25DBF1")
    forgot_password_screen.title("Reset Password")
    forgot_password_screen.geometry("300x250")
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

    Button(forgot_password_screen, text="Send Link", width=10, height=1, bg="#1FC2D3", command=verify_username).pack()
    Label(forgot_password_screen, text="", bg="#25DBF1").pack()

def verify_username():
    username1 = username_verify.get()
    username_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        reset_link()
    else:
        Label(forgot_password_screen, text="Email not registered",fg='red', bg="#25DBF1").pack()
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

def reset_link():
    global reset_link_screen
    reset_link_screen = Toplevel(login_screen, bg="#25DBF1")
    reset_link_screen.title("Link Sent")
    reset_link_screen.geometry("150x100")
    Label(reset_link_screen, text="Reset password link sent to your email!", bg="#25DBF1", fg='green').pack()
    Label(reset_link_screen,text='', bg="#25DBF1").pack()
    Button(reset_link_screen, text="OK", command=delete_reset_link, bg="#1FC2D3").pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen, bg="#25DBF1")
    password_not_recog_screen.title("ERROR!")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password!", fg="red", bg="#25DBF1").pack()
    Label(password_not_recog_screen, text="Please try again", fg="red", bg="#25DBF1").pack()
    Label(password_not_recog_screen, text="", bg="#25DBF1").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised, bg="#1FC2D3").pack()
 
# Designing popup for user not found
 
def user_not_found():

    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen, bg="#25DBF1")
    user_not_found_screen.title("ERROR!")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found!", fg="red", bg="#25DBF1").pack()
    Label(user_not_found_screen, text="Please try again", fg="red", bg="#25DBF1").pack()
    Label(user_not_found_screen, text="", bg="#25DBF1").pack()
    
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen, bg="#1FC2D3").pack()
    Label(user_not_found_screen, text="", bg="#25DBF1").pack()


# Deleting popups
 
def delete_login():
    login_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_reset_link():
    reset_link_screen.destroy()

def logout():
    chatbot_screen.destroy()
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Chatbot System")

    canvas = tk.Canvas(height=100, width=800)
    canvas.pack()

    frame = tk.Frame(bg='#25DBF1')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    Label(frame, text="HI!", fg='white', bg="#25DBF1", font=('Helvetica', 18, "bold", "italic")).pack(side="top", fill="x", pady=10)
    Label(frame, text="Please select an option to begin", bg="#25DBF1", font=('Courier', 16, "bold")).pack()
 
    b1 = Button(frame, text="Login", command = login, bg="#2568F1", fg="white", font=('Courier', 14, "bold"))
    b1.place(relx=0.2, rely=0.3, relwidth=0.25, relheight=0.15)

    b2 = Button(frame, text="Register", command=register, bg="#2568F1", fg="white", font=('Courier', 14, "bold"))
    b2.place(relx=0.55, rely=0.3, relwidth=0.25, relheight=0.15)
 
    main_screen.mainloop()
 
 
main_account_screen()