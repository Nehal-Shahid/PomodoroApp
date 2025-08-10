import math
import tkinter as tk
from tkinter import Label, Canvas, Button , PhotoImage


# Constants
WORK_MINS = 25
SHORT_BREAK = 5
LONG_BREAK = 10
sessions = 0
timer = None
timer_running = False
time_left = 0

#COUNTDOWN FUNCTION
def count_down(count):
    global sessions, timer, timer_running, time_left
    time_left = count
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f'0{seconds}'
    if minutes < 10:
        minutes = f'0{minutes}'
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0 and timer_running:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        timer_running = False
        Start_Timer()

#START TIMER
def Start_Timer():
    global sessions, timer_running
    if timer_running:
        return
    sessions += 1
    timer_running = True

    if sessions % 8 == 0:
        count = LONG_BREAK * 60
        title_label.config(text="Long Break", fg="brown")
    elif sessions % 2 == 0:
        count = SHORT_BREAK * 60
        title_label.config(text="Short Break", fg="brown")
    else:
        count = WORK_MINS * 60
        title_label.config(text="Work", fg="brown")

    count_down(count)

#RESET TIMER 
def Reset_Timer():
    global timer_running, timer, sessions, time_left
    if timer:
        window.after_cancel(timer)
    sessions = 0
    timer_running = False
    time_left = 0
    title_label.config(text="Pomodoro Timer", fg="#333")
    canvas.itemconfig(timer_text, text="00:00")

#PAUSE TIMER
def Pause_Button():
    global timer_running, timer
    if timer_running:
        window.after_cancel(timer)
        timer_running = False

#RESUME TIMER
def Resume_Button():
    global timer_running
    if not timer_running and time_left > 0:
        timer_running = True
        count_down(time_left)

# ----------------- GUI SETUP -----------------
window = tk.Tk()
window.title('Pomodoro Timer')
window.config(padx=150, pady=100, bg="#FCE1E4")

title_label = Label(window, text='Pomodoro Timer', fg="#333", bg="#FCE1E4", font=('Comic Sans MS', 32, 'bold'))
title_label.grid(row=0, column=1)


# O
canvas = Canvas(width=300, height=300, bg="#FCE1E4", highlightthickness=0)
timer_text = canvas.create_text(150, 150, text='00:00', fill="#333", font=("Courier", 35 , "bold"))
canvas.grid(row=1, column=1)

start_button = Button(command=Start_Timer, text='Start Time', bg="#2C6450", font=('Arial', 12),relief="flat")
start_button.grid(column=0, row=2 , pady=5)

reset_button = Button(command=Reset_Timer, text='Reset', bg="#2C6450", font=('Arial', 12),relief="flat")
reset_button.grid(column=2, row=2 , pady=5)

pause_button = Button(command=Pause_Button, text='Pause', bg="#1D7956", font=('Arial', 12), relief='flat')
pause_button.grid(row=3, column=0, pady=5)

resume_button = Button(command=Resume_Button, text='Resume', bg="#1D7956", font=('Arial', 12) , relief="flat")
resume_button.grid(row=3, column=2 , pady=5)

window.mainloop()