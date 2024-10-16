import pyautogui
from time import sleep

# Taking input for number of lines
n = int(input("Enter the number of lines: "))
sleep(5)  

for i in range(1, n + 1):
    for j in range(i):
        # pyautogui.write('#', interval=0)
        pyautogui.keyDown('shift')  # Hold down the Shift key
        pyautogui.press('3')        # Press the 3 key
        pyautogui.keyUp('shift')  
        

    pyautogui.press('enter')
