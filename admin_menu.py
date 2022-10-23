from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from admin_cruduser import *
from admin_crudgamehard import *
from admin_crudgamemedium import *
from admin_crudgameeasy import *
from admin_uploadphotos_ez import *
from admin_uploadphotos_hrd import *
from admin_uploadphotos_md import *
import sqlite3

def menu_admin():
    #Top Level Menu, Title, and Icon
    admin_mainmenu = Toplevel()
    admin_mainmenu.title("Quizzaz - Admin Menu")
    admin_mainmenu.configure(bg="#1a237e")
    admin_mainmenu.wm_attributes("-topmost", 2)
    #Menu Frame
    menu_editquiz_frame = LabelFrame(admin_mainmenu, text="Admin Menu - Quizzaz - Edit Pertanyaan", padx=50, pady=50, bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    menu_editquiz_frame.grid(column=0, row=0, pady=15, padx=5)
    #CRUD USER
    #crud_user_btn = Button(menu_editquiz_frame, text="Kelola User", bg="#ffeb3b", font=('roboto', '10', 'bold'))
    #crud_user_btn.bind("<Button>", lambda e: UserForm(admin_mainmenu))
    #crud_user_btn.pack(pady=10)
    #CRUD QUIZ EASY
    crud_quizez_btn = Button(menu_editquiz_frame, text="Kelola Quiz Pemula", bg="#00c853", padx=5, font=('roboto', '10', 'bold')) #command=crudgame_menu)
    crud_quizez_btn.bind("<Button>", lambda e: QuizEZForm(admin_mainmenu))
    crud_quizez_btn.pack(pady=10)
    #CRUD QUIZ MEDIUM
    crud_quizmedium_btn = Button(menu_editquiz_frame, text="Kelola Quiz Sedang",  bg="#ffc400", padx=5, font=('roboto', '10', 'bold')) #command=crudgame_menu)
    crud_quizmedium_btn.bind("<Button>", lambda e: QuizMediumForm(admin_mainmenu))
    crud_quizmedium_btn.pack(pady=10)
    #CRUD QUIZ HARD
    crud_quizhard_btn = Button(menu_editquiz_frame, text="Kelola Quiz Hard", bg="#ff3d00", fg="white", padx=5, font=('roboto', '10', 'bold')) #command=crudgame_menu)
    crud_quizhard_btn.bind("<Button>", lambda e: QuizHardForm(admin_mainmenu))
    crud_quizhard_btn.pack(pady=10)
    #CHANGE PHOTOS
    menu_editphoto_frame = LabelFrame(admin_mainmenu, text="Admin Menu - Quizzaz - Edit Foto", padx=50, pady=50, bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    menu_editphoto_frame.grid(column=1, row=0, pady=15, padx=5)
    #EDIT PHOTOS EASY
    edit_ez_photos_btn = Button(menu_editphoto_frame, text="Kelola Foto Quiz Pemula", bg="#00c853", padx=5, font=('roboto', '10', 'bold'), command=ez_photoedit)
    edit_ez_photos_btn.pack(pady=10)
    #EDIT PHOTOS MEDIUM
    edit_md_photos_btn = Button(menu_editphoto_frame, text="Kelola Foto Quiz Sedang", bg="#ffc400", padx=5, font=('roboto', '10', 'bold'), command=md_photoedit)
    edit_md_photos_btn.pack(pady=10)
    #EDIT PHOTOS HARD
    edit_hrd_photos_btn = Button(menu_editphoto_frame, text="Kelola Foto Quiz Susah", bg="#ff3d00", fg="white" ,padx=5, font=('roboto', '10', 'bold'), command=hrd_photoedit)
    edit_hrd_photos_btn.pack(pady=10)

    #EXIT BUTTON
    back_btn = Button(admin_mainmenu, text="Back", command=admin_mainmenu.destroy, font=('roboto', '10', 'bold'), bg="#d50000", fg="white")
    back_btn.grid(column=0, row=1, pady=15, padx=5)

def open_crud_user():
    pass