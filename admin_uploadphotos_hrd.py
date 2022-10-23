import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
from io import BytesIO
    
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def get_data_010(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_010, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_011(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_011, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_012(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_012, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_020(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_020, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_021(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_021, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_022(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_022, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_030(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_030, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_031(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_031, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def get_data_032(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_hard where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0], "Pertanyaan = ", row[1])
        photo = row[3]    # image saved in the 5th column of database
        # convert the image data to file object
        fp = BytesIO(photo)
        # load the image
        image = Image.open(fp)
        resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        render = ImageTk.PhotoImage(resized)
        img = Label(show_blank_032, image=render)
        img.image = render
        img.place(x=0, y=0)
    conn.commit()
    conn.close()

def qz_010_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_010'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_010('qz_hrd_010')

def qz_011_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_011'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_011('qz_hrd_011')

def qz_012_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_012'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_011('qz_hrd_012')

def qz_020_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_020'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_020('qz_hrd_020')

def qz_021_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_021'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_021('qz_hrd_021')

def qz_022_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_022'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_022('qz_hrd_022')

def qz_030_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_030'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_030('qz_hrd_030')

def qz_031_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_031'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_031('qz_hrd_031')

def qz_032_edit():
    #SQlite Connection
    conn = sqlite3.connect('database.db')
    #Command to open file explorer to select photos
    f_type = [('Png Files', '*.png'),('Jpg Files', '*.jpg')]
    foto = filedialog.askopenfilename(filetypes=f_type)
    #img = ImageTk.PhotoImage(file=filename)
    photo_data = convertToBinaryData(foto)
    #SQLite Cursor to execute update command
    c = conn.cursor()
    #Query
    c.execute("UPDATE quiz_hard SET qz_photo = (?) WHERE id='qz_hrd_032'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data_032('qz_hrd_032')

def hrd_photoedit():
    #Connecting to database
    conn = sqlite3.connect('database.db')
    #Creating tkinter window
    window = Toplevel()
    window.geometry("800x600")
    window.title("Admin - Edit Medium Quiz Photo")
    window.wm_attributes("-topmost", 3)
    window.configure(bg="#1a237e")

    #To call image per quiz id
    #Quiz EZ No. 1
    #Frame
    qz_010_frame = LabelFrame(window, text="Quiz_ID_010", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_010_frame.grid(column=0, row=0, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_010= ImageTk.PhotoImage(resized)
    global show_blank_010
    show_blank_010 = Label(qz_010_frame, image=show_photo_hrd_010)
    show_blank_010.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_010 = Label(qz_010_frame, image=get_data_010('qz_hrd_010')).pack
    #Edit Button
    hrd_010_edit = Button(qz_010_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_010_edit)
    hrd_010_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 2
    #Frame
    qz_011_frame = LabelFrame(window, text="Quiz_ID_011", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_011_frame.grid(column=1, row=0, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_011= ImageTk.PhotoImage(resized)
    global show_blank_011
    show_blank_011 = Label(qz_011_frame, image=show_photo_hrd_011)
    show_blank_011.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_011 = Label(qz_011_frame, image=get_data_011('qz_hrd_011')).pack
    #Edit Button
    hrd_011_edit = Button(qz_011_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_011_edit)
    hrd_011_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 3
    #Frame
    qz_012_frame = LabelFrame(window, text="Quiz_ID_012", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_012_frame.grid(column=2, row=0, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_012= ImageTk.PhotoImage(resized)
    global show_blank_012
    show_blank_012 = Label(qz_012_frame, image=show_photo_hrd_012)
    show_blank_012.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_012 = Label(qz_012_frame, image=get_data_012('qz_hrd_012')).pack
    #Edit Button
    hrd_012_edit = Button(qz_012_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_012_edit)
    hrd_012_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 4
    #Frame
    qz_020_frame = LabelFrame(window, text="Quiz_ID_020", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_020_frame.grid(column=0, row=1, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_020= ImageTk.PhotoImage(resized)
    global show_blank_020
    show_blank_020 = Label(qz_020_frame, image=show_photo_hrd_020)
    show_blank_020.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_020 = Label(qz_020_frame, image=get_data_020('qz_hrd_020')).pack
    #Edit Button
    hrd_010_edit = Button(qz_020_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_020_edit)
    hrd_010_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 5
    #Frame
    qz_021_frame = LabelFrame(window, text="Quiz_ID_021", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_021_frame.grid(column=1, row=1, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_021= ImageTk.PhotoImage(resized)
    global show_blank_021
    show_blank_021 = Label(qz_021_frame, image=show_photo_hrd_021)
    show_blank_021.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_021 = Label(qz_021_frame, image=get_data_021('qz_hrd_021')).pack
    #Edit Button
    hrd_021_edit = Button(qz_021_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_021_edit)
    hrd_021_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 6
    #Frame
    qz_022_frame = LabelFrame(window, text="Quiz_ID_022", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_022_frame.grid(column=2, row=1, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_022= ImageTk.PhotoImage(resized)
    global show_blank_022
    show_blank_022 = Label(qz_022_frame, image=show_photo_hrd_022)
    show_blank_022.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_022 = Label(qz_022_frame, image=get_data_022('qz_hrd_022')).pack
    #Edit Button
    hrd_022_edit = Button(qz_022_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_022_edit)
    hrd_022_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 7
    #Frame
    qz_030_frame = LabelFrame(window, text="Quiz_ID_030", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_030_frame.grid(column=0, row=2, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_030= ImageTk.PhotoImage(resized)
    global show_blank_030
    show_blank_030 = Label(qz_030_frame, image=show_photo_hrd_030)
    show_blank_030.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_030 = Label(qz_030_frame, image=get_data_030('qz_hrd_030')).pack
    #Edit Button
    hrd_030_edit = Button(qz_030_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_030_edit)
    hrd_030_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 8
    #Frame
    qz_031_frame = LabelFrame(window, text="Quiz_ID_031", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_031_frame.grid(column=1, row=2, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_031= ImageTk.PhotoImage(resized)
    global show_blank_031
    show_blank_031 = Label(qz_031_frame, image=show_photo_hrd_031)
    show_blank_031.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_031 = Label(qz_031_frame, image=get_data_031('qz_hrd_031')).pack
    #Edit Button
    hrd_031_edit = Button(qz_031_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_031_edit)
    hrd_031_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 9
    #Frame
    qz_032_frame = LabelFrame(window, text="Quiz_ID_032", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_032_frame.grid(column=2, row=2, padx=15, pady=15)
    img_call = Image.open("quiz_photo/blank.png")
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    show_photo_hrd_032= ImageTk.PhotoImage(resized)
    global show_blank_032
    show_blank_032 = Label(qz_032_frame, image=show_photo_hrd_032)
    show_blank_032.pack(anchor=CENTER, padx=5, pady=10)
    show_photo_032 = Label(qz_032_frame, image=get_data_032('qz_hrd_032')).pack
    #Edit Button
    hrd_032_edit = Button(qz_032_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_032_edit)
    hrd_032_edit.pack(anchor=S, padx=15)

    #EXIT BUTTON
    back_btn = Button(window, text="Back", command=window.destroy, font=('roboto', '10', 'bold'), bg="#d50000", fg="white")
    back_btn.grid(column=3, row=1, padx=5, pady=10)

    #window.mainloop()

#hrd_photoedit()