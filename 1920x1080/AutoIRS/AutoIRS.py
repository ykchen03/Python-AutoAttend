import pyautogui
import keyboard
import time

print("Time:",time.strftime("%H:%M:%S", time.localtime()))
print("Start in 5 sec...")
time.sleep(5)
print('Start')

while True:
    cord=pyautogui.locateOnScreen("target.PNG",region=(870,870,1030,945),grayscale=True,confidence=0.5)
    
    if cord!=None:
        print("Found at",time.strftime("%H:%M:%S", time.localtime()))
        pyautogui.click(cord)
        break
        
    else:
        print("Not Found Next Check in 30 sec")
        keyboard.send("F5")
    time.sleep(30)


