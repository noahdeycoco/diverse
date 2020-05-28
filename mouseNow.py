import pyautogui
import time



width, height = pyautogui.size()

print(width, height)

pyautogui.click(1767, 15)

try:
  while True:
    print(pyautogui.position(), '\b')
    print('\b')
    time.sleep(2)
except KeyboardInterrupt:
  print('Programm exit.')