import pyautogui as pg
import time
import random
import keyboard as key

time.sleep(10)

# Click to focus on the Instagram search bar
pg.click(421, 758, 1, 3)
time.sleep(1)
pg.typewrite("www.instagram.com")
time.sleep(1)
pg.press("enter")

# Wait for the page to load
time.sleep(5)

# Click to focus on the Instagram window
pg.click(71, 124, 1, 5)

num_iterations = 50

for _ in range(num_iterations):
    pg.doubleClick(603, 414)
    time.sleep(2)

    # Efficiently scroll down within 3 seconds
    scroll_start_time = time.time()
    while time.time() - scroll_start_time < 3:
        pg.hotkey('down')  # Use the down arrow key to scroll
        time.sleep(0.1)  # Adjust sleep time as needed

    pg.doubleClick(603, 414)
    time.sleep(2)




# import pyautogui as pg
# import keyboard as key
# import time 
# import random

# time.sleep(10)
# # print(pg.position())

# pg.leftClick(421, 758, 1, 3)
# time.sleep(1)
# pg.typewrite("www.instagram.com")
# time.sleep(1)
# pg.press("enter")

# pg.leftClick(71, 124, 1, 5)

# num_iterations = 10

# for _ in range(num_iterations):
#     pg.doubleClick(603, 414)
#     time.sleep(2)

#     for _ in range(25):
#         pg.press('down') 
#         time.sleep(5)
        
#     pg.doubleClick(603, 414)
#     time.sleep(2)

