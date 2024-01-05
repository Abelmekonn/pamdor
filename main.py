from tkinter import *
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
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    text.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    
    if reps%8==0:
        text.config(text="break",fg=PINK)
        count_down(long_break)
    elif reps%2==0:
        text.config(text="break",fg=GREEN)
        count_down(short_break)
    else:
        text.config(text="Work",fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=math.floor(count%60)
    if count_sec==0:
        count_sec="00"
    elif count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            marks+="✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
text=Label(text="Timer",font=("Courier",29,"bold"),bg=YELLOW,fg=RED)
text.grid(column=1,row=0)

canvas=Canvas(width=200,height=240,bg=YELLOW,highlightthickness=0)
image_create=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=image_create)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=("Courier",20,"bold"))
canvas.grid(column=1,row=2)


button=Button(text="Start",highlightthickness=-1,command=start_timer)
button.grid(column=0,row=3)

reset_button=Button(text="Reset",highlightthickness=-2,command=reset_time)
reset_button.grid(column=2,row=3)

check_mark=Label(bg=YELLOW,fg=GREEN,font=("Areal",20,"normal"))
check_mark.grid(column=1,row=3)
window.mainloop()
