import random
import pyautogui as pg
import time

animal = ("Monkey", "Pig", "Baboon", "Snake")

time.sleep(8)

for i in range(500):
    a = random.choice(animal)
    pg.write("You're a " + a + "\n")
    pg.press("enter")