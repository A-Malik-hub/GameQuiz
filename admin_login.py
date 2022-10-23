from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from admin_menu import *
import sqlite3

# Function Login & Register
#def login():
#    # Databases
#    id = StringVar("admin").get()
#    pasw = StringVar("admin").get()
#    # Create a database or connect to one
#    conn = sqlite3.connect('database.db')
#    # Create cursor
#    c = conn.cursor()
#    # Query command to select (login) data from database
#    c.execute("SELECT * FROM admin WHERE username=? AND password=?",(id, pasw))
#    #fetch one data from database
#    row=c.fetchone()
#    if row:
#        menu_admin()
#    else:
#        messagebox.showinfo('info', 'login gagal')
#    #Commit changes
#    conn.commit()
#    #Close Connection
#    conn.close()

def login():
    #getting form data from user input
    uname=id.get()
    pwd=pasw.get()
    #create database connection
    conn = sqlite3.connect('database.db')
    #create cursor to execute command
    c = conn.cursor()
    #Query command to select login data from database
    c.execute("SELECT * FROM admin WHERE username=? AND password=?",(uname, pwd))
    #fetch one data from database
    row = c.fetchone()
    if row:
        messagebox.showinfo('info', 'selamat datang '+uname)
        menu_admin()
    else:
        messagebox.showinfo('info', 'login gagal')
    #commit changes
    conn.commit()
    #close connection
    conn.close()
    #if else if else for checking the id 
    #if uname=='' or pwd=='':
    #    messagebox.showinfo('info', 'Lengkapi data entry !!!')
    #else:
    #    if uname=="admin" and pwd=="admin":
    #        menu_admin() 
    #    else:
    #        messagebox.showinfo('info', 'salah username atau password')


#Creating a Top Level (On Top) of main window
def window_login_admin():
    #Calling (get) data from user input (Entry)
    #Top Level Command
    top_login_admin = Toplevel()
    top_login_admin.title('Quizzaz - Login As Admin')
    top_login_admin.configure(bg="#1a237e")
    #top_login_admin.wm_attributes("-topmost", 1)
    #top_login_admin.iconbitmap('homer.ico')
    #The password database kindof
    global id
    global pasw
    id = StringVar()
    pasw = StringVar()
    #Login Entry
    admin_frame = LabelFrame(top_login_admin, text="Login As Admin", padx=50, pady=30, bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    admin_frame.pack(padx=15, pady=15)
    txt_admin_id = Label(admin_frame, text="Enter Your ID:", bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    txt_admin_id.pack(pady=5)
    admin_id_input = Entry(admin_frame, textvariable=id)
    admin_id_input.pack()
    txt_admin_pass = Label(admin_frame, text="Enter Your Password:", bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    txt_admin_pass.pack(pady=5)
    admin_pass_input = Entry(admin_frame, show="*", textvariable=pasw)
    admin_pass_input.pack()
    admin_login_btn = Button(admin_frame, text="Log In", command=login, bg="#00acc1", fg="white", font=('roboto', '10', 'bold'))
    admin_login_btn.pack(pady=10)
    admin_ext_btn = Button(admin_frame, text="Back", command=top_login_admin.destroy, bg="#d50000", fg="white", font=('roboto', '10', 'bold'))
    admin_ext_btn.pack(pady=15)
