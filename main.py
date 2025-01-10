### DAY 26 ###

# import random
# import time

### LIST COMPREHENSION ###

# numbers = [1, 2, 3, 4, 5]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [n for n in name]
# print(new_list)

# initial_range = range(1, 9) # Will only print from 1 to 8
# new_range = [n + n for n in initial_range]
# print(new_range)

### CONDITIONAL LIST COMPREHENSION ###

# names = ["Dave", "Ken", "Joshua", "Kane", "Abiola", "Tope", "Diddy", "Chosen", "Cristiano", "Emmanuel", "Kimmich", "Alex", "Ben", "Martins"]
# new_names = [n.upper() for n in names if len(n) > 5]
# print(new_names)

### DICTIONARY COMPREHENSION ###

# scores = {student:random.randint(1, 100) for student in names}
# passed_students = {student:score for (student, score) in scores.items() if score >= 60}
# print(scores)
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words = sentence.split()
# lengths = [len(word) for word in words]
# result = {word: length for word, length in zip(words, lengths)}

# print(words)
# print(lengths)
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# temp_c = [temp for temp in weather_c.values()]
# days = [day for day in weather_c.keys()]
#
# def fahrenheit(temp_c):
#     return (temp_c * 9/5) + 32
#
# weather_f = {day:fahrenheit(temp_c) for day, temp_c in zip(days, temp_c)}

# print(temp_c)
# print(weather_f)




### DAY 27 ###

import tkinter

# window = tkinter.Tk()
#
# window.title("D  A  Y    2 7")
# window.minsize(width = 500, height = 500)
#
# my_label = tkinter.Label(window, text = "New Text", width = 20)
# my_label.pack()
#
# def reset_label():
#     my_label["text"] = "New Text"
#
# def buttonAction():
#     my_label["text"] = "YOU GOT HACKED!!!"
#     window.after(2000, reset_label)
#
#
# button = tkinter.Button(window, text = "CLICK ME", command = buttonAction)
# button.pack()



# window = tkinter.Tk()
# window.title("Miles to Kilometres Converter")
# window.minsize(400, 300)
# window.config(padx=100, pady=100)
#
# label = tkinter.Label(window, text="Miles")
# label.pack()
#
# entry = tkinter.Entry(width=8)
# entry.insert(0, "")
# entry.pack()
#
# label_01 = tkinter.Label(window, text="is equal to")
# label_01.pack()
#
# label_02 = tkinter.Label(window, text=" ")
# label_02.pack()
#
# label_03 = tkinter.Label(window, text="Kilometres")
# label_03.pack()
#
# def action():
#     x = round(float(entry.get()) * 1.60934)
#     label_02.config(text=f"{x}")
#
# button = tkinter.Button(text="Calculate", command=action)
# button.pack()
#
#
#
# window.mainloop()

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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Timer Project")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(window, width=400, height=240, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="images/clock.png")
canvas.create_image(200, 100, image=img)
canvas.create_text(200, 100, text="00:00", font=(FONT_NAME, 80, "bold"), fill="red")
canvas.pack()



window.mainloop()