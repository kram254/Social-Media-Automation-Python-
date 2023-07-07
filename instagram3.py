import pyautogui as pg
import keyboard as key
import time 
import random

time.sleep(3)
# print(pg.position())

pg.leftClick(421, 758, 1, 3)
time.sleep(1)
pg.typewrite("www.instagram.com")
time.sleep(1)
pg.press("enter")

pg.leftClick(143, 267, 1, 5)
time.sleep(3)
key.write("#art")
time.sleep(3)

# locating my search suggestions and clicking
pg.leftClick(169, 257)
time.sleep(15)

# locating my search results and clicking on first post
pg.leftClick(470, 474)
time.sleep(5)

# list = ["Nice", "Awesome", "Good one ", "Great"]

# list = ["Work of art", "Nice", "Awesome", "", "Great", "Perfection"]

for i in range(1500):
    # Like button position
    pg.doubleClick(399, 395)
    time.sleep(3)
      
    # # position of the comment box
    # pg.leftClick(1011, 688, 1)
    # message = random.choice(list)
    # pg.typewrite(message)
    # time.sleep(1)      
    # pg.press("enter")
    # time.sleep(5)
      
    # locating NEXT button
    pg.leftClick(1320, 396)
    
    time.sleep(3)

print("I'm Done biiih!!")