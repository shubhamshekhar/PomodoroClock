import tkinter
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
timer = None

"""
    Pomodoro Technique:
        25 min Work
        5 min Break
        
        25 min Work
        5 min Break
        
        25 min Work
        5 min Break
        
        25 min Work
        20 min Break
"""
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer, reps
    if reps != 0:
        window.after_cancel(timer)
        tick_label.config(text="")
        text_label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text=f"0:00")
        reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """
    calls call down timer
    :return:
    """
    global reps
    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN*60)
        text_label.config(text="Work", fg=GREEN)
    elif reps % 8:
        count_down(LONG_BREAK_MIN*60)
        text_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN*60)
        text_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    """
    Performs count down operation
    :param count:
    :return:
    """
    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps//2
        for _ in range(work_sessions):
            marks += "✅ "
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro Clock")
window.config(padx= 100, pady= 50, bg= YELLOW)

canvas = tkinter.Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image= tomato_img)

timer_text = canvas.create_text(100, 130, text= "0:00", fill= "white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

text_label = tkinter.Label(text="Timer", font= (FONT_NAME, 40, "bold"))
text_label.config(bg=YELLOW, fg= GREEN)
text_label.grid(row=0, column=1)

start_button = tkinter.Button(window, text="Start", highlightthickness=0, command=start_timer)
#img_start = tkinter.PhotoImage(file="start2.png") # make sure to add "/" not "\"
#start_button.config(image=img_start)
start_button.grid(row=2, column=0) # Displaying the button

reset_button = tkinter.Button(window, text="Reset", highlightthickness=0, command=reset_timer)
#img = tkinter.PhotoImage(file="start2.png") # make sure to add "/" not "\"
#reset_button.config(width=20, height=5)
reset_button.grid(row=2, column=2) # Displaying the button

tick_label = tkinter.Label()
tick_label.config(text="", bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column= 1)


window.mainloop()