### DAY 26 ###

# import random
import tkinter
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

window = tkinter.Tk()

window.title("D  A  Y    2 7")
window.minsize(width = 500, height = 500) 

my_label = tkinter.Label(window, text = "New Text", width = 20)
my_label.pack()

def reset_label():
    my_label["text"] = "New Text"

def buttonAction():
    my_label["text"] = "YOU GOT HACKED!!!"
    window.after(2000, reset_label)


button = tkinter.Button(window, text = "CLICK ME", command = buttonAction)
button.pack()


window.mainloop()

