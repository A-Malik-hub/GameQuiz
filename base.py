import re
import tkinter
import pygame
from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
import admin_login
from datetime import datetime
from PIL import ImageTk,Image
from io import BytesIO

#MUSIC 
pygame.mixer.init()

def bg_music_start():
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('audio/bg_music.ogg'))
    pygame.mixer.Channel(0).set_volume(0.20)

def bg_music_stop():
    pygame.mixer.Channel(0).stop()

def game_start():
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('audio/shapp.wav'))
    #pygame.mixer.music.play(loops=0)

def correct_sound():
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('audio/correct.wav'))

def false_sound():
    pygame.mixer.Channel(3).play(pygame.mixer.Sound('audio/wrong.wav'))

def endgame_highscore():
    pygame.mixer.Channel(4).play(pygame.mixer.Sound('audio/endgame_highscore.ogg'))

def endgame_lowscore():
    pygame.mixer.Channel(5).play(pygame.mixer.Sound('audio/endgame_lowscore.ogg'))

#This function is to disable button and entry when user inside the main menu
def enablelogin():
    login_id_input.config(state="normal")
    login_pass_input.config(state="normal")
    regis_id_input.config(state="normal")
    regis_pass_input.config(state="normal")
    login_button["state"] = NORMAL
    regis_button["state"] = NORMAL
    ext_btn["state"] = NORMAL
    adm_btn["state"] = NORMAL

def disablelogin():
    login_id_input.config(state="disabled")
    login_pass_input.config(state="disabled")
    regis_id_input.config(state="disabled")
    regis_pass_input.config(state="disabled")
    login_button["state"] = DISABLED
    regis_button["state"] = DISABLED
    ext_btn["state"] = DISABLED
    adm_btn["state"] = DISABLED

#Game Hard[
def qz_hrd_starter():
    #The main window 
    quiz01 = Toplevel()
    quiz01.geometry("860x480")
    quiz01.title("Quizzaz - No. 1")
    quiz01.configure(bg="#1a237e")
    quiz01.wm_attributes("-fullscreen", 3)
    #quiz01.iconbitmap('homer.ico')

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz01, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #the command to call quiz
    txt_quiz = Label(quiz01, text="Pertanyaan No.1", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)

    #The Question
    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_010'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz01, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz01, text="Iya", command=lambda: [qz_user_hrd_outcome_t(), correct_sound(), quiz01.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz01, text="Tidak", command=lambda: [qz_user_hrd_outcome_f(), false_sound(), quiz01.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_010'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_010
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_010 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz01, image=photo_hrd_010)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

    #reset score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = 0, hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_t():
    #The main window 
    quiz02_t = Toplevel()
    quiz02_t.geometry("860x480")
    quiz02_t.title("Quizzaz - No. 2")
    quiz02_t.configure(bg="#1a237e")
    quiz02_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz02_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    #the command to call quiz
    txt_quiz = Label(quiz02_t, text="Pertanyaan No.2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor = conn.cursor()
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_011'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz02_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz02_t, text="Iya", command=lambda: [qz_user_hrd_outcome_tf(), false_sound(), quiz02_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz02_t, text="Tidak", command=lambda: [qz_user_hrd_outcome_tt(), correct_sound(), quiz02_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_011'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_011
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_011 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz02_t, image=photo_hrd_011)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tf():
    #The main window 
    quiz03_f = Toplevel()
    quiz03_f.geometry("860x480")
    quiz03_f.title("Quizzaz - No. 3")
    quiz03_f.configure(bg="#1a237e")
    quiz03_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_f, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_f, text="Iya", command=lambda:[qz_user_hrd_outcome_tff(), false_sound(), quiz03_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_f, text="Tidak", command=lambda:[qz_user_hrd_outcome_tft(), correct_sound(), quiz03_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_f, image=photo_hrd_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tft():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda:[qz_user_hrd_outcome_tftt(), correct_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_tftf(), false_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_hrd_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tftt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_hrd_outcome_tfttf(), false_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_tfttt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tfttf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_hrd_outcome_tfttft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[hrd_over_tfttf(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tfttft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_hrd_outcome_tfttftt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_tfttftf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tfttftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_tfttfttt(), endgame_highscore(),  quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[hrd_over_tfttfttf(), endgame_lowscore(), quiz08_t .destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tfttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tfttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tfttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tfttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_hrd_outcome_tftttt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[hrd_over_tftttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    global photo_hrd_030
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tftttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_hrd_outcome_tfttttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_tfttttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tfttttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_tftttttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[hrd_over_tftttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tfttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tftf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_hrd_outcome_tftft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[hrd_over_tftff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tftft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_hrd_outcome_tftftt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[hrd_over_tftftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tftftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_tftfttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_tftfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tftftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tff():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_hrd_outcome_tfft(), correct_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[hrd_over_tfff(), endgame_lowscore(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tfft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[hrd_over_tfftf(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_tfftt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tfftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[hrd_over_tffttt(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[hrd_over_tffttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tffttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tffttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tfftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tfff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr1'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_f():
    #The main window 
    quiz02_f = Toplevel()
    quiz02_f.geometry("860x480")
    quiz02_f.title("Quizzaz - No. 2")
    quiz02_f.configure(bg="#1a237e")
    quiz02_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz02_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz02_f, text="Pertanyaan No.2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz02_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz02_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ff(), false_sound(), quiz02_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz02_f, text="Tidak", command=lambda:[qz_user_hrd_outcome_ft(), correct_sound(), quiz02_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz02_f, image=photo_hrd_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ft():
    #The main window 
    quiz03_t = Toplevel()
    quiz03_t.geometry("860x480")
    quiz03_t.title("Quizzaz - No. 3")
    quiz03_t.configure(bg="#1a237e")
    quiz03_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_t, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ftt(), correct_sound(), quiz03_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ftf(), false_sound(), quiz03_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_t, image=photo_hrd_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ftt():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda:[qz_user_hrd_outcome_fttf(), false_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_fttt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_hrd_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_fttt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ftttt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[hrd_over_ftttf(), endgame_lowscore(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ftttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[hrd_over_fttttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_fttttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_fttttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_ftttttt(), endgame_highscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_ftttttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_fttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_fttf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_hrd_outcome_fttft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[hrd_over_fttff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_fttft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[hrd_over_fttftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_fttftt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_fttftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_fttfttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_fttfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_fttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_fttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_fttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_fttff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ftf():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ftft(), correct_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[hrd_over_ftff(), endgame_lowscore(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_hrd_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ftft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[hrd_over_ftftf(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ftftt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ftftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[hrd_over_ftfttt(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[hrd_over_ftfttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ftftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tt():
    #The main window 
    quiz03_t = Toplevel()
    quiz03_t.geometry("860x480")
    quiz03_t.title("Quizzaz - No. 3")
    quiz03_t.configure(bg="#1a237e")
    quiz03_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_t, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_012'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_t, text="Iya", command=lambda: [qz_user_hrd_outcome_ttt(), correct_sound(), quiz03_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_t, text="Tidak", command=lambda: [qz_user_hrd_outcome_ttf(), false_sound(), quiz03_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_012'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_012
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_012 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_t, image=photo_hrd_012)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttt():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda: [qz_user_hrd_outcome_tttf(), false_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda: [qz_user_hrd_outcome_tttt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_hrd_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttf():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ttff(), false_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttft(), correct_sound(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_hrd_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ttftt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttftf(), false_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttftf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ttftft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[hrd_over_ttftff(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_hrd_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttftft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_ttftft(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttftftt(), correct_sound(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttftftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_ttftfttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[hrd_over_ttftfttf(), endgame_lowscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttftft():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ttfttf(), false_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttfttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttfttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ttftttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_ttftttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttftttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_ttfttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttfttttt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttfttttt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[hrd_over_ttftttttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[hrd_over_ttftttttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttfttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttfttf():
    #The main window 
    quiz07_f = Toplevel()
    quiz07_f.geometry("860x480")
    quiz07_f.title("Quizzaz - No. 7")
    quiz07_f.configure(bg="#1a237e")
    quiz07_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_f, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ttfttft(), correct_sound(), quiz07_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_f, text="Tidak", command=lambda:[hrd_over_ttfttff(), endgame_lowscore(), quiz07_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttfttff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttfttft():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_ttfttftf(), endgame_lowscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttfttftt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttfttftt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[hrd_over_ttfttfttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[hrd_over_ttfttfttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttfttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttfttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttfttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttff():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ttfft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[hrd_over_ttfff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttfft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ttfftt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[hrd_over_ttfftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttfftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_ttffttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_ttffttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttffttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttffttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()


def hrd_over_ttfftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttfff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tttt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ttttt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttttf(), false_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttttf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_hrd_outcome_ttttft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[hrd_over_ttttff(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttttft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_ttttftf(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_ttttftt(), correct_sound(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_ttttftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_ttttfttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[hrd_over_ttttfttf(), endgame_lowscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tttf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_hrd_outcome_tttft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[hrd_over_tttff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tttft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[hrd_over_tttftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_tttftt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tttftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[hrd_over_tttfttt(), endgame_highscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_tttfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda: [qz_user_hrd_outcome_tttttf(), false_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda: [qz_user_hrd_outcome_tttttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_hrd_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tttttf():
    #The main window 
    quiz07_f = Toplevel()
    quiz07_f.geometry("860x480")
    quiz07_f.title("Quizzaz - No. 7")
    quiz07_f.configure(bg="#1a237e")
    quiz07_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_f, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_f, text="Iya", command=lambda:[qz_user_hrd_outcome_tttttft(), correct_sound(), quiz07_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_f, text="Tidak", command=lambda:[hrd_over_tttttff(), endgame_lowscore(), quiz07_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tttttft():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[hrd_over_tttttftf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_hrd_outcome_tttttftt(), endgame_highscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_tttttftt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[hrd_over_tttttfttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[hrd_over_tttttfttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tttttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tttttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tttttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_tttttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tttttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_hrd_outcome_ttttttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[hrd_over_ttttttf(), endgame_highscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ttttttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda: [hrd_over_tttttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda: [qz_user_hrd_outcome_tttttttt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_tttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_tttttttt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr8'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda: [hrd_over_ttttttttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda: [hrd_over_ttttttttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ttttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ttttttttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr10'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_hrd_outcome_ff():
    #The main window 
    quiz03_f = Toplevel()
    quiz03_f.geometry("860x480")
    quiz03_f.title("Quizzaz - No. 3")
    quiz03_f.configure(bg="#1a237e")
    quiz03_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_f, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_f, text="Iya", command=lambda: [qz_user_hrd_outcome_fft(), correct_sound(), quiz03_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_f, text="Tidak", command=lambda: [hrd_over_fff(), endgame_lowscore(), quiz03_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_f, image=photo_hrd_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_fft():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda: [hrd_over_fftf(), endgame_lowscore(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda: [qz_user_hrd_outcome_fftt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_hrd_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_hrd_outcome_fftt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_hard WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_hard WHERE id='qz_hrd_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda: [hrd_over_ffttt(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda: [hrd_over_ffttf(), endgame_lowscore(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_hard WHERE id='qz_hrd_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_hrd_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_hrd_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_hrd_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def hrd_over_ffttf():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr2'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ffttt():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr3'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_fftf():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr1'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_fff():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scrbase'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = 0, hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def hrd_over_ftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_hard WHERE id='scr1'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack() 

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_hrd = "+call_score+", hrd_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()
 

# ]

#Game Medium[
def qz_md_starter():
    #The main window 
    quiz01 = Toplevel()
    quiz01.geometry("860x480")
    quiz01.title("Quizzaz - No. 1")
    quiz01.configure(bg="#1a237e")
    quiz01.wm_attributes("-fullscreen", 3)
    #quiz01.iconbitmap('homer.ico')

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz01, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #the command to call quiz
    txt_quiz = Label(quiz01, text="Pertanyaan No.1", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)

    #The Question
    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_010'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz01, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz01, text="Iya", command=lambda: [qz_user_md_outcome_t(), correct_sound(), quiz01.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz01, text="Tidak", command=lambda: [qz_user_md_outcome_f(), false_sound(), quiz01.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_010'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_010
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_010 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz01, image=photo_md_010)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

    #reset score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = 0, md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_t():
    #The main window 
    quiz02_t = Toplevel()
    quiz02_t.geometry("860x480")
    quiz02_t.title("Quizzaz - No. 2")
    quiz02_t.configure(bg="#1a237e")
    quiz02_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz02_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    #the command to call quiz
    txt_quiz = Label(quiz02_t, text="Pertanyaan No.2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor = conn.cursor()
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_011'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz02_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz02_t, text="Iya", command=lambda: [qz_user_md_outcome_tf(), false_sound(), quiz02_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz02_t, text="Tidak", command=lambda: [qz_user_md_outcome_tt(), correct_sound(), quiz02_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_011'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_011
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_011 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz02_t, image=photo_md_011)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tf():
    #The main window 
    quiz03_f = Toplevel()
    quiz03_f.geometry("860x480")
    quiz03_f.title("Quizzaz - No. 3")
    quiz03_f.configure(bg="#1a237e")
    quiz03_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_f, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_f, text="Iya", command=lambda:[qz_user_md_outcome_tff(), false_sound(), quiz03_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_f, text="Tidak", command=lambda:[qz_user_md_outcome_tft(), correct_sound(), quiz03_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_f, image=photo_md_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tft():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda:[qz_user_md_outcome_tftt(), correct_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda:[qz_user_md_outcome_tftf(), false_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_md_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tftt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_md_outcome_tfttf(), false_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_md_outcome_tfttt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tfttf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_md_outcome_tfttft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[md_over_tfttf(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tfttft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_md_outcome_tfttftt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_tfttftf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tfttftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_tfttfttt(), endgame_highscore(),  quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[md_over_tfttfttf(), endgame_lowscore(), quiz08_t .destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tfttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tfttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tfttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tfttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_md_outcome_tftttt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[md_over_tftttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    global photo_md_030
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tftttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_md_outcome_tfttttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_tfttttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tfttttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_tftttttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[md_over_tftttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tfttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tftf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_md_outcome_tftft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[md_over_tftff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tftft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_md_outcome_tftftt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[md_over_tftftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tftftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_tftfttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_tftfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tftftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tff():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_md_outcome_tfft(), correct_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[md_over_tfff(), endgame_lowscore(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tfft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[md_over_tfftf(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_md_outcome_tfftt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tfftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[md_over_tffttt(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[md_over_tffttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tffttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tffttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tfftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tfff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr1'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_f():
    #The main window 
    quiz02_f = Toplevel()
    quiz02_f.geometry("860x480")
    quiz02_f.title("Quizzaz - No. 2")
    quiz02_f.configure(bg="#1a237e")
    quiz02_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz02_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz02_f, text="Pertanyaan No.2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz02_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz02_f, text="Iya", command=lambda:[qz_user_md_outcome_ff(), false_sound(), quiz02_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz02_f, text="Tidak", command=lambda:[qz_user_md_outcome_ft(), correct_sound(), quiz02_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz02_f, image=photo_md_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ft():
    #The main window 
    quiz03_t = Toplevel()
    quiz03_t.geometry("860x480")
    quiz03_t.title("Quizzaz - No. 3")
    quiz03_t.configure(bg="#1a237e")
    quiz03_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_t, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_t, text="Iya", command=lambda:[qz_user_md_outcome_ftt(), correct_sound(), quiz03_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_t, text="Tidak", command=lambda:[qz_user_md_outcome_ftf(), false_sound(), quiz03_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_t, image=photo_md_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ftt():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda:[qz_user_md_outcome_fttf(), false_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda:[qz_user_md_outcome_fttt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_md_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_fttt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_md_outcome_ftttt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[md_over_ftttf(), endgame_lowscore(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ftttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[md_over_fttttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_md_outcome_fttttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_fttttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_ftttttt(), endgame_highscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_ftttttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_fttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_fttf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_md_outcome_fttft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[md_over_fttff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_fttft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[md_over_fttftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_md_outcome_fttftt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_fttftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_fttfttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_fttfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_fttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_fttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_fttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_fttff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ftf():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_md_outcome_ftft(), correct_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[md_over_ftff(), endgame_lowscore(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_md_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ftft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[md_over_ftftf(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_md_outcome_ftftt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ftftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[md_over_ftfttt(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[md_over_ftfttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ftftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tt():
    #The main window 
    quiz03_t = Toplevel()
    quiz03_t.geometry("860x480")
    quiz03_t.title("Quizzaz - No. 3")
    quiz03_t.configure(bg="#1a237e")
    quiz03_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_t, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_012'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_t, text="Iya", command=lambda: [qz_user_md_outcome_ttt(), correct_sound(), quiz03_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_t, text="Tidak", command=lambda: [qz_user_md_outcome_ttf(), false_sound(), quiz03_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_012'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_012
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_012 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_t, image=photo_md_012)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttt():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda: [qz_user_md_outcome_tttf(), false_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda: [qz_user_md_outcome_tttt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_md_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttf():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_md_outcome_ttff(), false_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[qz_user_md_outcome_ttft(), correct_sound(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_md_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_md_outcome_ttftt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttftf(), false_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttftf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_md_outcome_ttftft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[md_over_ttftff(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_md_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttftft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_ttftft(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttftftt(), correct_sound(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttftftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_ttftfttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[md_over_ttftfttf(), endgame_lowscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttftft():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_md_outcome_ttfttf(), false_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttfttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttfttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_md_outcome_ttftttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_ttftttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttftttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_ttfttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttfttttt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttfttttt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[md_over_ttftttttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[md_over_ttftttttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttfttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttfttf():
    #The main window 
    quiz07_f = Toplevel()
    quiz07_f.geometry("860x480")
    quiz07_f.title("Quizzaz - No. 7")
    quiz07_f.configure(bg="#1a237e")
    quiz07_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_f, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_f, text="Iya", command=lambda:[qz_user_md_outcome_ttfttft(), correct_sound(), quiz07_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_f, text="Tidak", command=lambda:[md_over_ttfttff(), endgame_lowscore(), quiz07_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttfttff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttfttft():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_ttfttftf(), endgame_lowscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttfttftt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttfttftt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[md_over_ttfttfttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[md_over_ttfttfttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttfttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttfttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttfttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttff():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_md_outcome_ttfft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[md_over_ttfff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttfft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_md_outcome_ttfftt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[md_over_ttfftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttfftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_ttffttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_ttffttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttffttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttffttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()


def md_over_ttfftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttfff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tttt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_md_outcome_ttttt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttttf(), false_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttttf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_md_outcome_ttttft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[md_over_ttttff(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttttft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_ttttftf(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[qz_user_md_outcome_ttttftt(), correct_sound(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_ttttftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_ttttfttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[md_over_ttttfttf(), endgame_lowscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tttf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_md_outcome_tttft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[md_over_tttff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tttft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[md_over_tttftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_md_outcome_tttftt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tttftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[md_over_tttfttt(), endgame_highscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_tttfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda: [qz_user_md_outcome_tttttf(), false_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda: [qz_user_md_outcome_tttttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_md_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tttttf():
    #The main window 
    quiz07_f = Toplevel()
    quiz07_f.geometry("860x480")
    quiz07_f.title("Quizzaz - No. 7")
    quiz07_f.configure(bg="#1a237e")
    quiz07_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_f, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_f, text="Iya", command=lambda:[qz_user_md_outcome_tttttft(), correct_sound(), quiz07_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_f, text="Tidak", command=lambda:[md_over_tttttff(), endgame_lowscore(), quiz07_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tttttft():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[md_over_tttttftf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_md_outcome_tttttftt(), endgame_highscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_tttttftt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[md_over_tttttfttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[md_over_tttttfttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tttttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tttttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tttttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_tttttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tttttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_md_outcome_ttttttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[md_over_ttttttf(), endgame_highscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ttttttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda: [md_over_tttttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda: [qz_user_md_outcome_tttttttt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_tttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_tttttttt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr8'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda: [md_over_ttttttttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda: [md_over_ttttttttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ttttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ttttttttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr10'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_md_outcome_ff():
    #The main window 
    quiz03_f = Toplevel()
    quiz03_f.geometry("860x480")
    quiz03_f.title("Quizzaz - No. 3")
    quiz03_f.configure(bg="#1a237e")
    quiz03_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_f, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_f, text="Iya", command=lambda: [qz_user_md_outcome_fft(), correct_sound(), quiz03_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_f, text="Tidak", command=lambda: [md_over_fff(), endgame_lowscore(), quiz03_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_f, image=photo_md_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_fft():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda: [md_over_fftf(), endgame_lowscore(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda: [qz_user_md_outcome_fftt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_md_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_md_outcome_fftt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_medium WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_medium WHERE id='qz_md_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda: [md_over_ffttt(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda: [md_over_ffttf(), endgame_lowscore(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_medium WHERE id='qz_md_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_md_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_md_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_md_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def md_over_ffttf():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr2'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ffttt():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr3'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_fftf():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr1'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_fff():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scrbase'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = 0, md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def md_over_ftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_medium WHERE id='scr1'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack() 

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_md = "+call_score+", md_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()
 

# ]

#Game Easy[
def qz_ez_starter():
    #The main window 
    quiz01 = Toplevel()
    quiz01.geometry("860x480")
    quiz01.title("Quizzaz - No. 1")
    quiz01.configure(bg="#1a237e")
    quiz01.wm_attributes("-fullscreen", 3)
    #quiz01.iconbitmap('homer.ico')

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz01, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #the command to call quiz
    txt_quiz = Label(quiz01, text="Pertanyaan No.1", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)

    #The Question
    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_010'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz01, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz01, text="Iya", command=lambda: [qz_user_ez_outcome_t(), correct_sound(), quiz01.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz01, text="Tidak", command=lambda: [qz_user_ez_outcome_f(), false_sound(), quiz01.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_010'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_010
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_010 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz01, image=photo_ez_010)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

    #reset score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = 0, ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_t():
    #The main window 
    quiz02_t = Toplevel()
    quiz02_t.geometry("860x480")
    quiz02_t.title("Quizzaz - No. 2")
    quiz02_t.configure(bg="#1a237e")
    quiz02_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz02_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    #the command to call quiz
    txt_quiz = Label(quiz02_t, text="Pertanyaan No.2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor = conn.cursor()
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_011'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz02_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz02_t, text="Iya", command=lambda: [qz_user_ez_outcome_tf(), false_sound(), quiz02_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz02_t, text="Tidak", command=lambda: [qz_user_ez_outcome_tt(), correct_sound(), quiz02_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_011'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_011
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_011 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz02_t, image=photo_ez_011)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tf():
    #The main window 
    quiz03_f = Toplevel()
    quiz03_f.geometry("860x480")
    quiz03_f.title("Quizzaz - No. 3")
    quiz03_f.configure(bg="#1a237e")
    quiz03_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_f, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_f, text="Iya", command=lambda:[qz_user_ez_outcome_tff(), false_sound(), quiz03_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_f, text="Tidak", command=lambda:[qz_user_ez_outcome_tft(), correct_sound(), quiz03_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_f, image=photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tft():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda:[qz_user_ez_outcome_tftt(), correct_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda:[qz_user_ez_outcome_tftf(), false_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_ez_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tftt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_ez_outcome_tfttf(), false_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_ez_outcome_tfttt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tfttf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_ez_outcome_tfttft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[ez_over_tfttf(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tfttft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_ez_outcome_tfttftt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_tfttftf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tfttftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_tfttfttt(), endgame_highscore(),  quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[ez_over_tfttfttf(), endgame_lowscore(), quiz08_t .destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tfttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tfttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tfttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tfttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_ez_outcome_tftttt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[ez_over_tftttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    global photo_ez_030
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tftttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_ez_outcome_tfttttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_tfttttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tfttttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_tftttttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[ez_over_tftttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tfttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tftf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_ez_outcome_tftft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[ez_over_tftff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tftft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_ez_outcome_tftftt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[ez_over_tftftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tftftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_tftfttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_tftfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tftftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tff():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_ez_outcome_tfft(), correct_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[ez_over_tfff(), endgame_lowscore(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tfft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[ez_over_tfftf(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_ez_outcome_tfftt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tfftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[ez_over_tffttt(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[ez_over_tffttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tffttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tffttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tfftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tfff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr1'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_f():
    #The main window 
    quiz02_f = Toplevel()
    quiz02_f.geometry("860x480")
    quiz02_f.title("Quizzaz - No. 2")
    quiz02_f.configure(bg="#1a237e")
    quiz02_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz02_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz02_f, text="Pertanyaan No.2", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz02_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz02_f, text="Iya", command=lambda:[qz_user_ez_outcome_ff(), false_sound(), quiz02_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz02_f, text="Tidak", command=lambda:[qz_user_ez_outcome_ft(), correct_sound(), quiz02_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz02_f, image=photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ft():
    #The main window 
    quiz03_t = Toplevel()
    quiz03_t.geometry("860x480")
    quiz03_t.title("Quizzaz - No. 3")
    quiz03_t.configure(bg="#1a237e")
    quiz03_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_t, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_t, text="Iya", command=lambda:[qz_user_ez_outcome_ftt(), correct_sound(), quiz03_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ftf(), false_sound(), quiz03_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_t, image=photo_ez_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ftt():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda:[qz_user_ez_outcome_fttf(), false_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda:[qz_user_ez_outcome_fttt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_ez_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_fttt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_ez_outcome_ftttt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[ez_over_ftttf(), endgame_lowscore(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ftttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[ez_over_fttttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_ez_outcome_fttttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_fttttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_ftttttt(), endgame_highscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_ftttttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_fttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_fttf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_ez_outcome_fttft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[ez_over_fttff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_fttft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[ez_over_fttftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_ez_outcome_fttftt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_fttftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_fttfttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_fttfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_fttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_fttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_fttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_fttff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ftf():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_ez_outcome_ftft(), correct_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[ez_over_ftff(), endgame_lowscore(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ftft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[ez_over_ftftf(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ftftt(), correct_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ftftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[ez_over_ftfttt(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[ez_over_ftfttf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ftftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tt():
    #The main window 
    quiz03_t = Toplevel()
    quiz03_t.geometry("860x480")
    quiz03_t.title("Quizzaz - No. 3")
    quiz03_t.configure(bg="#1a237e")
    quiz03_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_t, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_012'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_t, text="Iya", command=lambda: [qz_user_ez_outcome_ttt(), correct_sound(), quiz03_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_t, text="Tidak", command=lambda: [qz_user_ez_outcome_ttf(), false_sound(), quiz03_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_012'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_012
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_012 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_t, image=photo_ez_012)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttt():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda: [qz_user_ez_outcome_tttf(), false_sound(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda: [qz_user_ez_outcome_tttt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttf():
    #The main window 
    quiz04_f = Toplevel()
    quiz04_f.geometry("860x480")
    quiz04_f.title("Quizzaz - No. 4")
    quiz04_f.configure(bg="#1a237e")
    quiz04_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_f, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_020'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_f, text="Iya", command=lambda:[qz_user_ez_outcome_ttff(), false_sound(), quiz04_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_f, text="Tidak", command=lambda:[qz_user_ez_outcome_ttft(), correct_sound(), quiz04_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_020'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_020
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_020 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_f, image=photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttft():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_ez_outcome_ttftt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttftf(), false_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttftf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_ez_outcome_ttftft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[ez_over_ttftff(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_ez_020)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttftft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_ttftft(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttftftt(), correct_sound(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttftftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_ttftfttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[ez_over_ttftfttf(), endgame_lowscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttftfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttftfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttftft():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttftt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_ez_outcome_ttfttf(), false_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttfttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttfttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_ez_outcome_ttftttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_ttftttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttftttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_ttfttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttfttttt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttfttttt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[ez_over_ttftttttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[ez_over_ttftttttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttftttttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttftttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttfttttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttftttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttfttf():
    #The main window 
    quiz07_f = Toplevel()
    quiz07_f.geometry("860x480")
    quiz07_f.title("Quizzaz - No. 7")
    quiz07_f.configure(bg="#1a237e")
    quiz07_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_f, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_f, text="Iya", command=lambda:[qz_user_ez_outcome_ttfttft(), correct_sound(), quiz07_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_f, text="Tidak", command=lambda:[ez_over_ttfttff(), endgame_lowscore(), quiz07_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttfttff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttfttft():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_ttfttftf(), endgame_lowscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttfttftt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttfttftt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[ez_over_ttfttfttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[ez_over_ttfttfttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttfttfttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttfttfttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttfttftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttff():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_ez_outcome_ttfft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[ez_over_ttfff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttfft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[qz_user_ez_outcome_ttfftt(), correct_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[ez_over_ttfftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttfftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_ttffttt(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_ttffttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttffttt():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttffttf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()


def ez_over_ttfftf():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttfff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr2'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tttt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_021'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda:[qz_user_ez_outcome_ttttt(), correct_sound(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttttf(), false_sound(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_021'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_021
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_021 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_021)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttttf():
    #The main window 
    quiz06_f = Toplevel()
    quiz06_f.geometry("860x480")
    quiz06_f.title("Quizzaz - No. 6")
    quiz06_f.configure(bg="#1a237e")
    quiz06_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_f, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_f, text="Iya", command=lambda:[qz_user_ez_outcome_ttttft(), correct_sound(), quiz06_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_f, text="Tidak", command=lambda:[ez_over_ttttff(), endgame_lowscore(), quiz06_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttttft():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_ttttftf(), endgame_lowscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[qz_user_ez_outcome_ttttftt(), correct_sound(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_ttttftt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_ttttfttt(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[ez_over_ttttfttf(), endgame_lowscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tttf():
    #The main window 
    quiz05_f = Toplevel()
    quiz05_f.geometry("860x480")
    quiz05_f.title("Quizzaz - No. 5")
    quiz05_f.configure(bg="#1a237e")
    quiz05_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr3'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_f, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_f, text="Iya", command=lambda:[qz_user_ez_outcome_tttft(), correct_sound(), quiz05_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_f, text="Tidak", command=lambda:[ez_over_tttff(), endgame_lowscore(), quiz05_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tttft():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr4'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda:[ez_over_tttftf(), endgame_lowscore(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda:[qz_user_ez_outcome_tttftt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tttftt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[ez_over_tttfttt(), endgame_highscore(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_tttfttf(), endgame_lowscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr4'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttttt():
    #The main window 
    quiz06_t = Toplevel()
    quiz06_t.geometry("860x480")
    quiz06_t.title("Quizzaz - No. 6")
    quiz06_t.configure(bg="#1a237e")
    quiz06_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz06_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz06_t, text="Pertanyaan No.6", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_022'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz06_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz06_t, text="Iya", command=lambda: [qz_user_ez_outcome_tttttf(), false_sound(), quiz06_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz06_t, text="Tidak", command=lambda: [qz_user_ez_outcome_tttttt(), correct_sound(), quiz06_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_022'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_022
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_022 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz06_t, image=photo_ez_022)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tttttf():
    #The main window 
    quiz07_f = Toplevel()
    quiz07_f.geometry("860x480")
    quiz07_f.title("Quizzaz - No. 7")
    quiz07_f.configure(bg="#1a237e")
    quiz07_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr5'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_f, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_f, text="Iya", command=lambda:[qz_user_ez_outcome_tttttft(), correct_sound(), quiz07_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_f, text="Tidak", command=lambda:[ez_over_tttttff(), endgame_lowscore(), quiz07_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tttttft():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda:[ez_over_tttttftf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda:[qz_user_ez_outcome_tttttftt(), endgame_highscore(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_tttttftt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda:[ez_over_tttttfttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda:[ez_over_tttttfttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tttttfttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tttttfttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tttttftf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr6'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_tttttff():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr5'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="Ayo Main Lagi !!!", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tttttt():
    #The main window 
    quiz07_t = Toplevel()
    quiz07_t.geometry("860x480")
    quiz07_t.title("Quizzaz - No. 7")
    quiz07_t.configure(bg="#1a237e")
    quiz07_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz07_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr6'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz07_t, text="Pertanyaan No.7", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz07_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz07_t, text="Iya", command=lambda:[qz_user_ez_outcome_ttttttt(), correct_sound(), quiz07_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz07_t, text="Tidak", command=lambda:[ez_over_ttttttf(), endgame_highscore(), quiz07_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz07_t, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ttttttt():
    #The main window 
    quiz08_t = Toplevel()
    quiz08_t.geometry("860x480")
    quiz08_t.title("Quizzaz - No. 8")
    quiz08_t.configure(bg="#1a237e")
    quiz08_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz08_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr7'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz08_t, text="Pertanyaan No.8", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz08_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz08_t, text="Iya", command=lambda: [ez_over_tttttttf(), endgame_highscore(), quiz08_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz08_t, text="Tidak", command=lambda: [qz_user_ez_outcome_tttttttt(), correct_sound(), quiz08_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz08_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_tttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr7'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_tttttttt():
    #The main window 
    quiz09_t = Toplevel()
    quiz09_t.geometry("860x480")
    quiz09_t.title("Quizzaz - No. 9")
    quiz09_t.configure(bg="#1a237e")
    quiz09_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz0
    conn = sqlite3.connect('database.db')
    #cursor of score
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz09_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr8'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz09_t, text="Pertanyaan No.9", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz09_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz09_t, text="Iya", command=lambda: [ez_over_ttttttttt(), endgame_highscore(), quiz09_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz09_t, text="Tidak", command=lambda: [ez_over_ttttttttf(), endgame_highscore(), quiz09_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz09_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ttttttttf():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr8'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ttttttttt():
    #Showing the final score that user get (for this case when user answer all the question correctly)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr10'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="MAIN LAGI", command=total_score.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def qz_user_ez_outcome_ff():
    #The main window 
    quiz03_f = Toplevel()
    quiz03_f.geometry("860x480")
    quiz03_f.title("Quizzaz - No. 3")
    quiz03_f.configure(bg="#1a237e")
    quiz03_f.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz03_f, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scrbase'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz03_f, text="Pertanyaan No.3", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_030'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz03_f, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz03_f, text="Iya", command=lambda: [qz_user_ez_outcome_fft(), correct_sound(), quiz03_f.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz03_f, text="Tidak", command=lambda: [ez_over_fff(), endgame_lowscore(), quiz03_f.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_030'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_030
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_030 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz03_f, image=photo_ez_030)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_fft():
    #The main window 
    quiz04_t = Toplevel()
    quiz04_t.geometry("860x480")
    quiz04_t.title("Quizzaz - No. 4")
    quiz04_t.configure(bg="#1a237e")
    quiz04_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz04_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr1'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz04_t, text="Pertanyaan No.4", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_031'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz04_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz04_t, text="Iya", command=lambda: [ez_over_fftf(), endgame_lowscore(), quiz04_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz04_t, text="Tidak", command=lambda: [qz_user_ez_outcome_fftt(), correct_sound(), quiz04_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_031'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_031
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_031 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz04_t, image=photo_ez_031)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def qz_user_ez_outcome_fftt():
    #The main window 
    quiz05_t = Toplevel()
    quiz05_t.geometry("860x480")
    quiz05_t.title("Quizzaz - No. 5")
    quiz05_t.configure(bg="#1a237e")
    quiz05_t.wm_attributes("-fullscreen", 3)

    #Database connection of quiz01
    conn = sqlite3.connect('database.db')
    #cursor of score base which is 0
    score_cursor = conn.cursor()
    #The score frame
    score_frame = LabelFrame(quiz05_t, text="TOTAL SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_frame.pack(padx=50)
    txt_score = Label(score_frame, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack()
    score_cursor.execute("SELECT score FROM score_easy WHERE id='scr2'")
    score = score_cursor.fetchone()
    score_label = Label(score_frame, text=score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    score_label.pack()

    #cursor of quiz so it can call a quiz from database
    quiz_cursor = conn.cursor()
    #the command to call quiz
    txt_quiz = Label(quiz05_t, text="Pertanyaan No.5", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_quiz.pack(pady=15)
    quiz_cursor.execute("SELECT quiz FROM quiz_easy WHERE id='qz_ez_032'")
    quiz = quiz_cursor.fetchone()[0]
    quiz_label = Label(quiz05_t, text=quiz, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quiz_label.pack()

    #Button to answer which is Yes and No
    btn_yes = Button(quiz05_t, text="Iya", command=lambda: [ez_over_ffttt(), endgame_lowscore(), quiz05_t.destroy()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=10)
    btn_no = Button(quiz05_t, text="Tidak", command=lambda: [ez_over_ffttf(), endgame_lowscore(), quiz05_t.destroy()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=3)

    #Quiz photo
    #Database to call photos
    photo_cursor = conn.cursor()
    photo_cursor.execute("SELECT qz_photo FROM quiz_easy WHERE id='qz_ez_032'")
    quizphoto = photo_cursor.fetchone()[0]
    #Command to show photo
    global photo_ez_032
    img_byte = BytesIO(quizphoto)
    img_call = Image.open(img_byte)
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    photo_ez_032 = ImageTk.PhotoImage(resized)
    show_image = Label(quiz05_t, image=photo_ez_032)
    show_image.pack(anchor=CENTER, padx=5, pady=10)

def ez_over_ffttf():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr2'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ffttt():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr3'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_fftf():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr1'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()
    
    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_fff():
    #Showing the final score that user get (for this case when user failed to answer all of the correct question)
    total_score_fail = Tk()
    total_score_fail.geometry("330x240")
    total_score_fail.title("Total Score")
    total_score_fail.configure(bg="#1a237e")
    total_score_fail.wm_attributes("-fullscreen",3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score_fail, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scrbase'")
    call_score = c.fetchone()[0]
    total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    total_score.pack(pady=10)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score_fail, text="COBA LAGI", command=total_score_fail.destroy, bg="#00e5ff", font=('roboto', '10', 'bold'))
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score_fail, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score_fail, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score_fail, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack()

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = 0, ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()

def ez_over_ftff():
    #Showing the final score that user get (for this case when user answer false, correct, then 2 times false)
    total_score = Toplevel()
    total_score.geometry("420x280")
    total_score.title("Total Score")
    total_score.configure(bg="#1a237e")
    total_score.wm_attributes("-fullscreen", 3)

    #The Frame to show how many user get
    ttl_score_frame = LabelFrame(total_score, text="SCORE", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    ttl_score_frame.pack()
    txt_score = Label(ttl_score_frame, text="Total Score Yang Anda Dapatkan adalah: ", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_score.pack(pady=5)
    #This is where the database wizardy comes in to call a defined score
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT score FROM score_easy WHERE id='scr1'")
    call_score = c.fetchone()[0]
    txt_total_score = Label(ttl_score_frame, text=call_score, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    txt_total_score.pack(pady=10)
    #Congratulate the user
    #txt_congrats = Label(total_score, text="SELAMAT !!! Ayo Main Lagi !", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    #txt_congrats.pack(pady=5)
    #Button to try again which trying to go back to the user menu
    btn_tryagain = Button(total_score, text="COBA LAGI", command=total_score.destroy)
    btn_tryagain.pack(pady=15)
    #A motivational quote to support the user
    quote_label_1 = Label(total_score, text="Keberhasilan adalah kemampuan untuk melewati", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_1.pack()
    quote_label_2 = Label(total_score, text="dan mengatasi dari satu kegagalan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_2.pack()
    quote_label_3 = Label(total_score, text="ke kegagalan berikutnya tanpa kehilangan semangat.", bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    quote_label_3.pack() 

    #insert score query
    user = login_id.get()
    score_insert = conn.cursor()
    score_insert.execute("UPDATE user SET scr_ez = "+call_score+", ez_datetime = '"+date_time+"' WHERE username='"+user+"'")

    #conn commit
    conn.commit()
    #close db connection
    conn.close()
 

# ]

#SCOREBOARD CODING YAY
def scoreboard_ez():
    #Tkinter window
    scrbrd_window = Tk()
    scrbrd_window.title("Quizzaz - Scoreboard Pemula")
    scrbrd_window.configure(bg="#1a237e")
    scrbrd_window.wm_attributes("-fullscreen", 2)
    #scrbrd_window.geometry("550x300")
    
    #Database calling
    conn = sqlite3.connect('database.db')
    #Cursor is kind of like a command to do programmer bidding
    c = conn.cursor()
    #Query command to retrieve the data from database
    c.execute("SELECT username, scr_ez, ez_datetime FROM user ORDER BY scr_ez DESC, ez_datetime ASC")
    #calling the data from database
    records = c.fetchall()

    #Treeview (Table View for tkinter)
    style = ttk.Style()
    #Treeview theme
    style.theme_use('default')
    #Treeview colour
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    #Treeview frame
    tree_frame = ttk.Frame(scrbrd_window)
    tree_frame.pack(pady=10)
    #Treeview scrollbar (incase needed)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    #Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()
    #Treeview Scrollbar
    tree_scroll.config(command=my_tree.yview)
    #Treeview Define Columns
    my_tree['columns'] = ("Nama", "Score","Pada Tanggal & Jam")
    #Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Nama", anchor=CENTER, width=100)
    my_tree.column("Score", anchor=CENTER, width=100)
    my_tree.column("Pada Tanggal & Jam", anchor=CENTER, width=200)
    #Headings
    my_tree.heading("#0", text="", anchor=CENTER)
    my_tree.heading("Nama", text="Nama", anchor=CENTER)
    my_tree.heading("Score", text="Score", anchor=CENTER)
    my_tree.heading("Pada Tanggal & Jam", text="Pada Tanggal & Jam" ,anchor=CENTER)
    #Stripped Row
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #Back Button
    btn_back = Button(scrbrd_window, text="Back", command=scrbrd_window.destroy, bg="#ffc400", padx=5, font=('roboto', '10', 'bold'))
    btn_back.pack(pady=5)

    #Add data to screen
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        count+=1
        
def scoreboard_md():
    #Tkinter window
    scrbrd_window = Tk()
    scrbrd_window.title("Quizzaz - Scoreboard Sedang")
    scrbrd_window.configure(bg="#1a237e")
    scrbrd_window.wm_attributes("-fullscreen", 2)
    #scrbrd_window.geometry("550x300")
    
    #Database calling
    conn = sqlite3.connect('database.db')
    #Cursor is kind of like a command to do programmer bidding
    c = conn.cursor()
    #Query command to retrieve the data from database
    c.execute("SELECT username, scr_md, md_datetime FROM user ORDER BY scr_md DESC, md_datetime ASC")
    #calling the data from database
    records = c.fetchall()

    #Treeview (Table View for tkinter)
    style = ttk.Style()
    #Treeview theme
    style.theme_use('default')
    #Treeview colour
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    #Treeview frame
    tree_frame = ttk.Frame(scrbrd_window)
    tree_frame.pack(pady=10)
    #Treeview scrollbar (incase needed)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    #Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()
    #Treeview Scrollbar
    tree_scroll.config(command=my_tree.yview)
    #Treeview Define Columns
    my_tree['columns'] = ("Nama", "Score","Pada Tanggal & Jam")
    #Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Nama", anchor=CENTER, width=100)
    my_tree.column("Score", anchor=CENTER, width=100)
    my_tree.column("Pada Tanggal & Jam", anchor=CENTER, width=200)
    #Headings
    my_tree.heading("#0", text="", anchor=CENTER)
    my_tree.heading("Nama", text="Nama", anchor=CENTER)
    my_tree.heading("Score", text="Score", anchor=CENTER)
    my_tree.heading("Pada Tanggal & Jam", text="Pada Tanggal & Jam" ,anchor=CENTER)
    #Stripped Row
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #Back Button
    btn_back = Button(scrbrd_window, text="Back", command=scrbrd_window.destroy, bg="#ffc400", padx=5, font=('roboto', '10', 'bold'))
    btn_back.pack(pady=5)

    #Add data to screen
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        count+=1

def scoreboard_hrd():
    #Tkinter window
    scrbrd_window = Tk()
    scrbrd_window.title("Quizzaz - Scoreboard Susah")
    scrbrd_window.configure(bg="#1a237e")
    scrbrd_window.wm_attributes("-fullscreen", 2)
    #scrbrd_window.geometry("550x300")
    
    #Database calling
    conn = sqlite3.connect('database.db')
    #Cursor is kind of like a command to do programmer bidding
    c = conn.cursor()
    #Query command to retrieve the data from database
    c.execute("SELECT username, scr_hrd, hrd_datetime FROM user ORDER BY scr_hrd DESC, hrd_datetime ASC")
    #calling the data from database
    records = c.fetchall()

    #Treeview (Table View for tkinter)
    style = ttk.Style()
    #Treeview theme
    style.theme_use('default')
    #Treeview colour
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground="#D3D3D3")
    #Treeview frame
    tree_frame = ttk.Frame(scrbrd_window)
    tree_frame.pack(pady=10)
    #Treeview scrollbar (incase needed)
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    #Create Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
    my_tree.pack()
    #Treeview Scrollbar
    tree_scroll.config(command=my_tree.yview)
    #Treeview Define Columns
    my_tree['columns'] = ("Nama", "Score","Pada Tanggal & Jam")
    #Format Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("Nama", anchor=CENTER, width=100)
    my_tree.column("Score", anchor=CENTER, width=100)
    my_tree.column("Pada Tanggal & Jam", anchor=CENTER, width=200)
    #Headings
    my_tree.heading("#0", text="", anchor=CENTER)
    my_tree.heading("Nama", text="Nama", anchor=CENTER)
    my_tree.heading("Score", text="Score", anchor=CENTER)
    my_tree.heading("Pada Tanggal & Jam", text="Pada Tanggal & Jam" ,anchor=CENTER)
    #Stripped Row
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="lightblue")

    #Back Button
    btn_back = Button(scrbrd_window, text="Back", command=scrbrd_window.destroy, bg="#ffc400", padx=5, font=('roboto', '10', 'bold'))
    btn_back.pack(pady=5)

    #Add data to screen
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        count+=1

# Function Login & Register
def login():
    #Calling (get) data from user input (Entry)
    uname = login_id.get()
    pwd = login_pass.get()
    # Databases
    # Create a database or connect to one
    conn = sqlite3.connect('database.db')
    # Create cursor
    c = conn.cursor()
    # Query command to select (login) data from database
    c.execute("SELECT * FROM user WHERE username=? AND password=?",(uname, pwd))
    #fetch one data from database
    row=c.fetchone()
    if row:
        messagebox.showinfo('Login', 'Selamat Datang '+uname)
        disablelogin()
        main_menu()
    else:
        messagebox.showinfo('Warning', 'Login Gagal, Pastikan Password atau Username Benar atau Registrasi jika belum punya akun')
    #Commit changes
    conn.commit()
    #Close Connection
    conn.close()

    # Clear Text Box
    #login_id_input.delete(0, END)
    #login_pass_input.delete(0, END)
    
def register():
    #Calling (get) data from user input (Entry)
    uname = regis_id.get()
    pwd = regis_pass.get()
    # Databases
    # Create a database or connect to one
    conn = sqlite3.connect('database.db')
    #Query Command to check if any duplicate data
    # Create cursor
    c = conn.cursor()
    #user_data = conn.cursor()
    #Check data
    #check_user = c.execute("SELECT username FROM user WHERE username = ?",(uname, ))
    #check_data = check_user.fetchall()
    #print(check_data)
    #Query command to insert (register) data to database
    #insert = c.execute("INSERT INTO user(username, password) VALUES (?,?)",(uname,pwd, ))
    #insert_data = insert.fetchall()
    try:
        c.execute('INSERT INTO user(username,password) VALUES(?,?)', (uname,pwd))
        messagebox.showinfo('Register', 'Registrasi Berhasil, Silahkan Gunakan Untuk Login')
        regis_id.set('')
        regis_pass.set('')
    except sqlite3.IntegrityError as e:
        if re.match(r'UNIQUE constraint failed', e.args[0]):
            messagebox.showinfo('Error', 'Username sudah dipakai')
            regis_id.set('')
            regis_pass.set('')
        else:
            raise e
    conn.commit()
    #fetch data from database
    #if uname == "" and pwd == "":
    #    messagebox.showinfo('info', 'Isi Username dan Password')
    #else:
    #    if uname == check_data[0][0]:
    #        messagebox.showinfo('info', 'Nama tersebut sudah terpakai')
    #        regis_id.set('')
    #        regis_pass.set('')
    #    elif uname is not check
    #        insert_data[0][0]
    #        messagebox.showinfo('info', 'Akun terdaftar, silahkan login')
    #        regis_id.set('')
    #        regis_pass.set('')
    #        conn.commit()

def main_menu():
    bg_music_start()
    #uname is to call username duh
    uname = login_id.get()
    #down here is the command to call time now using datetime lib
    time_now = datetime.now()
    #so down here is a callout to call time with time format so let's put it global so other function can call it
    global date_time
    date_time = time_now.strftime("%d/%m/%Y, %H:%M:%S")
    
    #The Root Window of Main Menu
    menu = Toplevel()
    menu.title("Quizzaz - Main Menu")
    menu.configure(bg="#1a237e")
    menu.wm_attributes("-fullscreen", 1)
    #menu.iconbitmap('homer.ico')

    #Welcoming User
    txt_welcome = Label(menu, text="Selamat Datang di Quizzaz, "+uname+". Good Luck!", bg="#1a237e", fg="white", font=('roboto', '15', 'bold')).pack(pady=20, anchor=CENTER)

    #Image Command, I'm going to show chris tucker face to you
    img_call = Image.open("profile/logo.png")
    resized = img_call.resize((200, 150), Image.ANTIALIAS)
    profile = ImageTk.PhotoImage(resized)
    show_image = Label(menu, image=profile, borderwidth=0, highlightthickness=0)
    show_image.pack(pady=20,anchor=CENTER)

    #Show time, it's showing time when user open the application this actually not showing the real ticking clock, so it's kind of a experimental to test the date time
    #txt_time = Label(menu, text=date_time, bg="#1a237e", fg="white", font=('roboto', '10', 'bold')).pack(pady=5)

    #This Is where user can select radio button difficulty
    difficulty_frame = LabelFrame(menu, text="Main Menu Game", padx=100, pady=60, bg="#1a237e", fg="white", font=('roboto', '10', 'bold'))
    difficulty_frame.pack(pady=0, anchor=CENTER)

    #Difficulty Choosing Button
    txt_difficulty = Label(difficulty_frame, text="Main Game - Pilih Tingkat Kesusahan", bg="#1a237e", fg="white", font=('roboto', '10', 'bold')).pack(pady=3)
    global btn_easy
    global btn_medium
    global btn_hard
    btn_easy = Button(difficulty_frame, text="Pemula", command=lambda: [qz_ez_starter(), game_start()], bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)
    btn_medium = Button(difficulty_frame, text="Sedang", command=lambda: [qz_md_starter(), game_start()], bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)
    btn_hard = Button(difficulty_frame, text="Susah", command=lambda: [qz_hrd_starter(), game_start()], bg="#ff3d00", fg="white", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)

    #Scoreboard menu
    txt_scoreboard = Label(difficulty_frame, text="Scoreboard", bg="#1a237e", fg="white", font=('roboto', '10', 'bold')).pack(pady=3)
    global btn_scoreboard_ez
    global btn_scoreboard_md
    global btn_scoreboard_hrd
    btn_scoreboard_ez = Button(difficulty_frame, text="Scoreboard Pemula", command=scoreboard_ez, bg="#00c853", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)
    btn_scoreboard_md = Button(difficulty_frame, text="Scoreboard Sedang", command=scoreboard_md, bg="#ffc400", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)
    btn_scoreboard_hrd = Button(difficulty_frame, text="Scoreboard Susah", command=scoreboard_hrd, bg="#ff3d00", fg="white", padx=5, font=('roboto', '10', 'bold')).pack(pady=5)

    #Exit Button
    global btn_exit
    btn_exit = Button(menu, text="LOG OUT", command=lambda: [menu.destroy(), enablelogin() ,login_id.set(''), login_pass.set(''), bg_music_stop()], font=('roboto', '10', 'bold'), bg="#d50000", fg="white").pack(pady=5)
    menu.mainloop()

def LoginForm():
    window = Tk()
    window.title('Quizzaz - Login Form')
    window.configure(bg="#1a237e")
    #Settings things global so other function can access it
    global login_id
    global login_pass
    global regis_id
    global regis_pass
    login_id = tkinter.StringVar()
    login_pass = tkinter.StringVar()
    regis_id = tkinter.StringVar()
    regis_pass = tkinter.StringVar()
    #Login Entry Widget
    login_frame = LabelFrame(window, text="Login Form", padx=80, pady=30, bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    login_frame.grid(column=0, row=0, padx=15, pady=15, sticky=W)
    text_id_login = Label(login_frame, text="Enter Your ID: ", bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    text_id_login.pack()
    global login_id_input
    login_id_input = Entry(login_frame, textvariable=login_id)
    login_id_input.pack()
    text_pass_login = Label(login_frame, text="Enter Your Password: ", bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    text_pass_login.pack(pady=10)
    global login_pass_input
    login_pass_input = Entry(login_frame, show="*", textvariable=login_pass)
    login_pass_input.pack()
    global login_button
    login_button = Button(login_frame, text="Log In", command=login, bg="#00acc1", fg="white", font=('roboto', '10', 'bold'))
    login_button.pack(pady=10)

    #Register Entry Widget
    regis_frame = LabelFrame(window, text="Register Form", padx=80, pady=30, bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    regis_frame.grid(column=1, row=0, padx=15, pady=5, sticky=E)
    text_id_regis = Label(regis_frame, text="Enter Your ID: ", bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    text_id_regis.pack()
    global regis_id_input
    regis_id_input = Entry(regis_frame, textvariable=regis_id)
    regis_id_input.pack()
    text_pass_regis = Label(regis_frame, text="Enter Your Password: ", bg="#1a237e", fg ="white", font=('roboto', '10', 'bold'))
    text_pass_regis.pack(pady=10)
    global regis_pass_input
    regis_pass_input = Entry(regis_frame, show="*", textvariable=regis_pass)
    regis_pass_input.pack()
    global regis_button
    regis_button = Button(regis_frame, text="Register", command=register, bg="#388e3c", fg="white", font=('roboto', '10', 'bold'))
    regis_button.pack(pady=10)

    #Exit Button
    global ext_btn
    ext_btn = Button(window, text="Exit", command=quit, bg="#d50000", fg="white", font=('roboto', '10', 'bold'))
    ext_btn.grid(column=0, row=1,pady=10)
    #Admin Button
    global adm_btn
    adm_btn = Button(window, text="Log In As Admin", command=admin_login.window_login_admin, bg="#ffeb3b", font=('roboto', '10', 'bold'))
    adm_btn.grid(column=1, row=1, pady=10)
    window.mainloop()

LoginForm()