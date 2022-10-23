import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
from io import BytesIO

def up_ez_photos():
    #Tkinter edt_photos
    edt_photos = Toplevel()
    edt_photos.title("Quizzaz - Scoreboard Susah")
    edt_photos.configure(bg="#1a237e")
    edt_photos.geometry("550x300")
    edt_photos.wm_attributes("-topmost", 4)
    
    #Database calling
    conn = sqlite3.connect('database.db')
    #Cursor is kind of like a command to do programmer bidding
    c = conn.cursor()
    #Query command to retrieve the data from database
    c.execute("SELECT qz_photo, id FROM quiz_easy")
    #calling the data from database
    records = c.fetchall()

    #Treeview (Table View for tkinter)
    style = ttk.Style()
    #Treeview theme
    style.theme_use('default')
    #Treeview colour
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=100, fieldbackground="#D3D3D3")
    #Treeview frame
    tree_frame = ttk.Frame(edt_photos)
    tree_frame.pack(pady=10)
    #Treeview scrollbar (incase needed)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    #Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", columns=['ID Quiz'])
    my_tree.pack()
    #Treeview Scrollbar
    tree_scroll.config(command=my_tree.yview)
    #Headings
    my_tree.heading("#0", text="Image", anchor=CENTER)
    my_tree.heading("ID Quiz", text="ID Quiz", anchor=CENTER)
    #Stripped Row
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #Back Button
    btn_back = Button(edt_photos, text="Back", command=edt_photos.destroy, bg="#ffc400", padx=5, font=('roboto', '10', 'bold'))
    btn_back.pack(pady=5)

    #Add data to screen
    count = 0
    imglist = []

    for record in records:
        if count % 2 == 0:
            img_byte = BytesIO(record[0])
            img_call = Image.open(img_byte)
            resized = img_call.resize((150, 75), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(resized)
            my_tree.insert('', 'end', image=img, values=record[1:])
            imglist.append(img)
        else:
            img_byte = BytesIO(record[0])
            img_call = Image.open(img_byte)
            resized = img_call.resize((150, 75), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(resized)
            my_tree.insert('', 'end', image=img, values=record[1:])
            imglist.append(img)
        count+=1

    #edt_photos.mainloop()

#up_ez_photos()