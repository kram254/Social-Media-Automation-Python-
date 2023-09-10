import pyautogui as pg
import keyboard as key
import time 
import random

time.sleep(10)
# print(pg.position())

pg.leftClick(421, 758, 1, 3)
time.sleep(1)
pg.typewrite("www.instagram.com")
time.sleep(1)
pg.press("enter")

pg.leftClick(71, 124, 1, 5)

pg.doubleClick(578, 767)
time.sleep(2)

pg.leftClick(934, 538, 1, 5)
# pg.press('down') 
# time.sleep(4)  

for _ in range(25):
        pg.press('down') 
        time.sleep(1)
        
pg.doubleClick(578, 767)
time.sleep(2)


# for i in range(2500):
#     # Like button position
#     pg.doubleClick(399, 395)
#     time.sleep(3)

#     # # position of the comment box
#     # pg.leftClick(1011, 688, 1)
#     # message = random.choice(list)
#     # pg.typewrite(message)
#     # time.sleep(1)      
#     # pg.press("enter")
#     # time.sleep(5)
      
#     # locating NEXT button
#     pg.leftClick(1320, 396)
#     time.sleep(3)

# print("I'm Done biiih!!")