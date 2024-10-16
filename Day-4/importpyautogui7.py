import pyautogui
from time import sleep

sleep(5) # 5 second wait 


for i in range(0,3):
    pyautogui.write('hello hello ', interval=0.23)
    pyautogui.press('enter')

# hello Krishna i love you 


# first install --> pip install PyAutoGUI 
# https://pypi.org/project/PyAutoGUI/  python এর package 


for i in range(0,10):
    pyautogui.write('Hello ' , interval=0.2)
    pyautogui.press('enter')


