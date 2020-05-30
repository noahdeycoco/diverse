import pyautogui
import time



width, height = pyautogui.size()

print(width, height)

# pyautogui.click(1767, 15)

# try:
#   while True:
#     print(pyautogui.position(), '\b')
#     print('\b')
#     time.sleep(2)
# except KeyboardInterrupt:
#   print('Programm exit.')


pyautogui.click() # click to put drawing program in focus
distance = 200
while distance > 0:
  pyautogui.dragRel(distance, 0) # move right
  distance = distance - 5
  pyautogui.dragRel(0, distance,) # move down
  pyautogui.dragRel(-distance, 0,) # move left
  distance = distance - 5
  pyautogui.dragRel(0, -distance) # move up