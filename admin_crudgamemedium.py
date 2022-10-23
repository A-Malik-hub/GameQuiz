from doctest import master
from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image

import sqlite3
from turtle import width

class QuizMediumForm(Toplevel):
    # connection dir property
    db_name = 'database.db'

    def __init__(self, master = None):
        # Initializations
        super().__init__(master=master)
        self.title('Quizzaz - Kelola Quiz - Medium')
        self.configure(bg="#1a237e")
        self.wm_attributes("-topmost", 3)
        #self.iconbitmap('homer.ico')

        # Creating a Frame Container
        #frame = LabelFrame(self.wind, text = 'Tambah User')
        #frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name Input
        #Label(frame, text = 'Username: ').grid(row = 1, column = 0)
        #self.name = Entry(frame)
        #self.name.focus()
        #self.name.grid(row = 1, column = 1)

        # Price Input
        #Label(frame, text = 'Password: ').grid(row = 2, column = 0)
        #self.price = Entry(frame)
        #self.price.grid(row = 2, column = 1)

        # Button Add Product
        #ttk.Button(frame, text = 'Simpan User', command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Output Messages
        self.message = Label(self, text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = N + S)

        # Table
        self.tree = ttk.Treeview(self, height = 12, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.column("#0", width=550 ,stretch=NO)
        self.tree.column("#1", width=550 ,stretch=NO)
        self.tree.heading('#0', text = 'QUIZ', anchor = CENTER)
        self.tree.heading('#1', text = 'ANSWER(UNCHANGE) - Untuk Membantu Membuat Soal Yang Harus Dijawab Iya / Tidak', anchor = CENTER)
        
        #self.tree.heading('#2', text = 'JAWABAN', anchor = CENTER)

        # Buttons
        #ttk.Button(text = 'DELETE', command = self.delete_product).grid(row = 5, column = 0, sticky = W + E)
        ttk.Button(self, text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)

        # Filling the Rows
        self.get_products()

    # Function to Execute Database Querys
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    # Get Products from Database
    def get_products(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # getting data
        query = 'SELECT * FROM quiz_medium ORDER BY id DESC'
        db_rows = self.run_query(query)
        # filling data
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

    # User Input Validation
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0

    def add_product(self):
        if self.validation():
            query = 'INSERT INTO user VALUES(NULL, ?, ?)'
            parameters =  (self.name.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'User {} added Successfully'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)
        else:
            self.message['text'] = 'User and Password is Required'
        self.get_products()

    def delete_product(self):
        self.message['text'] = ''
        try:
           self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a Record'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM user WHERE username = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Record {} deleted Successfully'.format(name)
        self.get_products()

    def edit_product(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        quiz = self.tree.item(self.tree.selection())['text']
        answer = self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Edit Product'
        # Old Name
        Label(self.edit_wind, text = 'Deskrispi:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = quiz), state = 'readonly', width=100).grid(row = 0, column = 2)
        # New Name
        Label(self.edit_wind, text = 'Deskripsi Baru:').grid(row = 1, column = 1)
        new_quiz = Entry(self.edit_wind, width=100)
        new_quiz.grid(row = 1, column = 2)

        # Old Price
        Label(self.edit_wind, text = 'Jawaban:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = answer), state = 'readonly').grid(row = 2, column = 2)

        Button(self.edit_wind, text = 'Update', command = lambda: self.edit_records(new_quiz.get(), quiz, answer)).grid(row = 4, column = 2, sticky = W)
        self.edit_wind.mainloop()

    def edit_records(self, new_quiz, quiz, answer):
        query = "UPDATE quiz_medium SET quiz = ? WHERE quiz = ? AND answer_tohelp = ?"
        parameters = (new_quiz, quiz, answer)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Quiz updated successfully'
        self.get_products()

# if __name__ == '__main__':
#     window = Tk()
#     application = QuizForm(window)
#     window.mainloop()