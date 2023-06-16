import pyautogui as pg
import time

time.sleep(5)
# print(pg.position())

pg.leftClick(421, 758, 1, 3)
time.sleep(1)
pg.typewrite("web.whatsapp.com/")
time.sleep(1)
pg.press("enter")

pg.leftClick(143, 267, 1, 15)
time.sleep(1)


for i in range(40):
    pg.typewrite("I love you so so much. 😍😘😘")
    pg.press("enter")
    time.sleep(1)
    
print("Done!!")    