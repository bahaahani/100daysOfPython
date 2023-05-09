from tkinter import *
import time 
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps %8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Long thick Break", fg=PINK)
    elif reps %2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=RED)
    if reps %2 ==1:
        count_down(work_sec)
        title_label.config(text="Werk", fg=RED)
 
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <=9:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
         timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        mark =""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmarks.config(text=mark)
        
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label= Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)



canvas = Canvas(width=200, height=224, highlightthickness=0,bg=YELLOW)
photoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photoImg)
timer_text =canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
end_button = Button(text="Reset", highlightthickness=0 , command=reset_timer)
end_button.grid(column=2, row=2)

checkmarks = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()