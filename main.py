from tkinter import *
import time

BG_COLOR = "#303841"
TEXT_BG_COLOR = "#eeeeee"
FONT_STYLE = "Courier"
TEXT_COLOR = "#00adb5"

timer = None
time_passed = 0


def check_typing(current_entry):
    global time_passed, timer
    entry = text_area.get("1.0", END)
    if len(entry) - len(current_entry) == 0:
        time_passed += 1
        if time_passed > 0 and time_passed % 5 == 0:
            text_area.delete("1.0", END)
            time_passed = 0
            timer = window.after(1000, check_typing, "")
        else:
            timer = window.after(1000, check_typing, entry)
    else:
        time_passed = 0
        timer = window.after(1000, check_typing, entry)


window = Tk()
window.title("Text Disappears")
window.geometry("1150x750")
window.config(bg=BG_COLOR, padx=45, pady=45)

canvas = Canvas(height=150, width=150, highlightthickness=0, bg=BG_COLOR)
logo_img = PhotoImage(file='note.png')
canvas.create_image(50, 50, image=logo_img)
canvas.grid(row=0, column=0)

title_label = Label(text="DisappearText", font=(FONT_STYLE, 34, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
title_label.grid(row=0, column=1)

rule_label = Label(text="DO NOT STOP WRITING MORE THAN 5 SECONDS !!!\nOTHERWISE YOU WILL LOST YOUR TEXT...",
                   font=(FONT_STYLE, 20, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
rule_label.grid(row=2, column=1)

text_area = Text(window, height=20, width=70, bg=TEXT_BG_COLOR, font=(FONT_STYLE, 14, "bold"), fg="#ff5722")
text_area.grid(row=1, column=1)

check_typing("")
window.mainloop()
