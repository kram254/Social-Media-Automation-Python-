import pyautogui as pg
import keyboard as key
import time
import random

time.sleep(3)
search_topics = ["#midjourneyart", "aiart", "midjorney" ]
for _ in range(10):  # Loop 10 times, adjust as desired
    pg.leftClick(421, 758, 1, 3)
    time.sleep(1)
    pg.typewrite("www.instagram.com")
    time.sleep(1)
    pg.press("enter")

    pg.leftClick(143, 267, 1, 10)
    time.sleep(2)
    
    search_topic = random.choice(search_topics)
    key.write(search_topic)
    
    time.sleep(3)

    pg.leftClick(169, 257)
    time.sleep(15)

    pg.leftClick(470, 474)
    time.sleep(5)

    comment_list = ["Work of art", "Nice", "Awesome", "Excellent", "Great", "Perfection", "Elegant", "Stylish", "Stunning", "Radiant"]

    for i in range(2000):
        pg.doubleClick(399, 395)
        time.sleep(3)

        # pg.leftClick(1011, 688, 1)
        # message = random.choice(comment_list)
        # pg.typewrite(message)
        # time.sleep(1)
        # pg.press("enter")
        # time.sleep(5)

        pg.leftClick(1320, 396)

        time.sleep(3)

    # print("Search for topic '{}' completed.".format(search_topic))

# print("All searches completed.")
