import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
Timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(Timer)
    canvas.itemconfig(timer, text="00:00")
    Label1.config(text="Timer")
    Label2.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        countdown(long_break_sec)
        Label1.config(text="Break", foreground=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        Label1.config(text="Break", foreground=PINK)
    else:
        countdown(work_sec)
        Label1.config(text="Work", foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global  Timer
    count_munite = math.floor(count/60)
    count_second = count%60

    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer, text=f"{count_munite}:{count_second}")
    if count > 0:
        Timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/4)):
            mark += "✔"
        Label2.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

Label1 = Label(text="Time Table", foreground= GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW, highlightthickness=0)
Label1.grid(row=0, column=1)

# CHECK MARK
Label2 = Label(foreground=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW, highlightthickness=0)
Label2.grid(row=3, column=1)

button1 = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=PINK, highlightthickness=0, command=start_timer)
button1.grid(row=2, column=0)

button2 = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=PINK, highlightthickness=0, command=reset_timer)
button2.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
