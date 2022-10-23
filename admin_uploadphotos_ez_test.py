import sqlite3
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
from io import BytesIO
import PIL
import requests
    
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def get_data(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_fetch_blob_query = "SELECT * from quiz_easy where id = ?"
    c.execute(sql_fetch_blob_query, (id,))
    record = c.fetchall()
    for row in record:
        print("id = ", row[0])
        photo = row[3]    # image saved in the 5th column of database

        # convert the image data to file object
        BytesIO(photo)
        # load the image
        #image = Image.open(fp)
        #resized = image.resize((150, 100), Image.ANTIALIAS)
        # drawing image to top window
        #render = ImageTk.PhotoImage(resized)
        #img = Label(image=render)
        #img.image = render
        #img.place(bordermode=INSIDE)
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
    c.execute("UPDATE quiz_easy SET qz_photo = (?) WHERE id='qz_ez_010'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()
    get_data('qz_ez_010')

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
    c.execute("UPDATE quiz_easy SET qz_photo = (?) WHERE id='qz_ez_011'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()

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
    c.execute("UPDATE quiz_easy SET qz_photo = (?) WHERE id='qz_ez_012'", (photo_data,))
    #Convert Image data to binary data
    #Cursor execute
    #Connection commit
    conn.commit()
    #connection close
    conn.close()

def ez_photoedit():
    #Connecting to database
    conn = sqlite3.connect('database.db')
    #Creating tkinter window
    window = Tk()
    window.geometry("800x600")
    window.title("Admin - Edit Easy Quiz Photo")
    window.wm_attributes("-topmost", 3)
    window.configure(bg="#1a237e")

    #To call image per quiz id
    #Quiz EZ No. 1
    #Frame
    qz_010_frame = LabelFrame(window, text="Quiz No. 1", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_010_frame.grid(column=0, row=0, padx=15, pady=15)
    #DB Cursor to call the image data from database
    #qz_ez_010 = conn.cursor()
    #qz_ez_010.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_010'")
    #photo_ez_010 = qz_ez_010.fetchall()[0][0]
    #Command to show
    #img = get_data('qz_ez_010')
    #img_byte = BytesIO(img)
    r = requests.get(get_data('qz_ez_010'), stream=True)
    img_call = Image.open(BytesIO(r.content))
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_010
    show_image = Label(qz_011_frame, image=show_photo_ez_010)
    show_image = Label(qz_010_frame, image=show_photo_ez_010)#image=show_photo_ez_010)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_010_edit = Button(qz_010_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_010_edit)
    ez_010_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 2
    #Frame
    qz_011_frame = LabelFrame(window, text="Quiz No. 2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_011_frame.grid(column=1, row=0, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_011 = conn.cursor()
    qz_ez_011.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_011'")
    photo_ez_011 = qz_ez_011.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_011)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_011
    show_photo_ez_011 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_011_frame, image=show_photo_ez_011)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_011_edit = Button(qz_011_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_011_edit)
    ez_011_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 3
    #Frame
    qz_012_frame = LabelFrame(window, text="Quiz No. 3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_012_frame.grid(column=2, row=0, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_012 = conn.cursor()
    qz_ez_012.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_012'")
    photo_ez_012 = qz_ez_012.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_012)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_012
    show_photo_ez_012 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_012_frame, image=show_photo_ez_012)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_012_edit = Button(qz_012_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'), command=qz_012_edit)
    ez_012_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 4
    #Frame
    qz_020_frame = LabelFrame(window, text="Quiz No. 4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_020_frame.grid(column=0, row=1, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_020 = conn.cursor()
    qz_ez_020.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_020'")
    photo_ez_020 = qz_ez_020.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_020)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_020
    show_photo_ez_020 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_020_frame, image=show_photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_020_edit = Button(qz_020_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'))
    ez_020_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 5
    #Frame
    qz_021_frame = LabelFrame(window, text="Quiz No. 5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_021_frame.grid(column=1, row=1, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_021 = conn.cursor()
    qz_ez_021.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_021'")
    photo_ez_021 = qz_ez_021.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_021)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_021
    show_photo_ez_021 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_021_frame, image=show_photo_ez_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_021_edit = Button(qz_021_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'))
    ez_021_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 6
    #Frame
    qz_022_frame = LabelFrame(window, text="Quiz No. 6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_022_frame.grid(column=2, row=1, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_022 = conn.cursor()
    qz_ez_022.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_022'")
    photo_ez_022 = qz_ez_022.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_022)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_022
    show_photo_ez_022 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_022_frame, image=show_photo_ez_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_022_edit = Button(qz_022_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'))
    ez_022_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 7
    #Frame
    qz_030_frame = LabelFrame(window, text="Quiz No. 7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_030_frame.grid(column=0, row=2, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_030 = conn.cursor()
    qz_ez_030.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    photo_ez_030 = qz_ez_030.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_030)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_030
    show_photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_030_frame, image=show_photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_030_edit = Button(qz_030_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'))
    ez_030_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 8
    #Frame
    qz_031_frame = LabelFrame(window, text="Quiz No. 8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_031_frame.grid(column=1, row=2, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_031 = conn.cursor()
    qz_ez_031.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    photo_ez_031 = qz_ez_031.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_031)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_031
    show_photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_031_frame, image=show_photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_031_edit = Button(qz_031_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'))
    ez_031_edit.pack(anchor=S, padx=15)

    #Quiz EZ No. 9
    #Frame
    qz_032_frame = LabelFrame(window, text="Quiz No. 9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    qz_032_frame.grid(column=2, row=2, padx=15, pady=15)
    #DB Cursor to call the image data from database
    qz_ez_032 = conn.cursor()
    qz_ez_032.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    photo_ez_032 = qz_ez_032.fetchall()[0][0]
    #Command to show
    img_byte = BytesIO(photo_ez_032)
    img_call = Image.open(img_byte)
    resized = img_call.resize((150, 100), Image.ANTIALIAS)
    global show_photo_ez_032
    show_photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(qz_032_frame, image=show_photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)
    #Edit Button
    ez_032_edit = Button(qz_032_frame, text="Edit Foto", bg="#ffeb3b", padx=5, font=('roboto', '10', 'bold'))
    ez_032_edit.pack(anchor=S, padx=15)

    #EXIT BUTTON
    back_btn = Button(window, text="Back", command=window.destroy, font=('roboto', '10', 'bold'), bg="#d50000", fg="white")
    back_btn.grid(column=3, row=1, padx=5, pady=10)

    window.mainloop()

ez_photoedit()