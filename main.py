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



# --------------------------------------------------------------------------------------------------------------------



### DAY 27 ###

# import tkinter

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



# --------------------------------------------------------------------------------------------------------------------



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


# --------------------------------------------------------------------------------------------------------------------


### DAY 28 ###

# import tkinter
# import math

# ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Klapt"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None

# ---------------------------- TIMER RESET ------------------------------- #
# def reset():
#     global reps
#     reps = 0
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
#     checkmark.config(text="")
#     title.config(text=" Timer Project")

# ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     global reps
#     reps += 1
#     print(reps)
#     window.attributes('-topmost', 1)
#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60
#
#     if reps % 8 == 0:
#         countdown(long_break_sec)
#         title.config(text="Long Break", fg="black")
#     elif reps % 2 == 0:
#         countdown(short_break_sec)
#         title.config(text= "Short Break", fg="blue")
#     else:
#         countdown(work_sec)
#         title.config(text="Work Period", fg="red")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def countdown(count):
#     global reps
#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"
#     if count_min < 10:
#         count_min = f"0{count_min}"
#     if count_sec == 0:
#         count_sec = "00"
#     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
#     if count > 0:
#         global timer
#         timer = window.after(1000, countdown, count - 1)
#     else:
#         start_timer()
#         if reps % 2 == 0:
#             checkmark.config(text="✓")

# ---------------------------- UI SETUP ------------------------------- #
# window = tkinter.Tk()
# window.title("Timer Project")
# window.config(padx=40, pady=10, bg=YELLOW)
#
# title = tkinter.Label(text="Timer Project", fg="brown", bg=YELLOW)
# title.config(padx=10, pady=30)
# title.config(font=(FONT_NAME, 30, "bold"))
# title.grid(column=1, row=0)
#
# canvas = tkinter.Canvas(window, width=400, height=240, bg=YELLOW, highlightthickness=0)
# img = tkinter.PhotoImage(file="images/clock.png")
# canvas.create_image(200, 100, image=img)
# timer_text = canvas.create_text(200, 90, text=f"{WORK_MIN}:00", font=(FONT_NAME, 80, "bold"), fill="red")
# canvas.grid(column=1, row=2)
#
# button_1 = tkinter.Button(text="Start", font=(FONT_NAME, 20, "bold"))
# button_1.config(bg=YELLOW, padx=5, pady=2, highlightthickness=0, command=start_timer)
# button_1.grid(column=0, row=3)
#
# button_2 = tkinter.Button(text="Reset", font=(FONT_NAME, 20, "bold"))
# button_2.config(bg=YELLOW, padx=5, pady=2, highlightthickness=0, command=reset)
# button_2.grid(column=2, row=3)
#
# checkmark = tkinter.Label(text="", fg="brown", bg=YELLOW)
# checkmark.config(padx=10, pady=10)
# checkmark.config(font=(FONT_NAME, 50, "bold"))
# checkmark.grid(column=1, row=4)
#
# window.mainloop()

### DAY 30 ###

# fruits = ["Apple", "Pear", "Orange"]
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")
#
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]





def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            # If 'Likes' is missing, just skip this post
            pass
    return total_likes

# Call the function
print(count_likes(facebook_posts))



