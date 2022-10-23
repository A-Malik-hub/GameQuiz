from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from game_hard import *
from game_medium import *
from game_easy import *
#import base
import sqlite3

from game_hard import qz_hrd_starter

#username = base.id

def main_menu():
    #The Root Window of Main Menu
    menu = Tk()
    menu.title("Quizzaz - Main Menu")
    menu.configure(bg="#1a237e")
    #menu.iconbitmap('homer.ico')
    
    #This Is where user can select radio button difficulty
    difficulty_frame = LabelFrame(menu, text="Pilih Tingkat Kesulitan", padx=100, pady=60, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    difficulty_frame.pack()

    #Difficulty Choosing Button
    txt = Label(difficulty_frame, text="Pilih Tingkat Kesusahan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold')).pack(pady=10)
    btn_easy = Button(difficulty_frame, text="Pemula", command=qz_ez_starter, bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)
    btn_medium = Button(difficulty_frame, text="Sedang", command=qz_md_starter, bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)
    btn_hard = Button(difficulty_frame, text="Susah", command=qz_hrd_starter, bg="#ff3d00", fg="white", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)

    #Exit Button
    btn_exit = Button(menu, text="KELUAR", command=menu.destroy, font=('roboto', '10', 'bold'), bg="#d50000", fg="white").pack(pady=5)