from pyautogui import *
import pyautogui
import time
import keyboard
#import random
import win32api, win32con

#Tile 1 Position: X:  749 Y:  698 RGB: (169, 173, 223)
#Tile 2 Position: X:  908 Y:  698 RGB: ( 54, 159, 198)
#Tile 3 Position: X: 1019 Y:  698 RGB: (175, 184, 229)
#Tile 4 Position: X: 1159 Y:  698 RGB: (183, 194, 236)



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(749, 698)[0] == 0:
        click(749, 698)
    if pyautogui.pixel(908, 698)[0] == 0:
        click(908, 698)
    if pyautogui.pixel(1019, 698)[0] == 0:
        click(1019, 698)
    if pyautogui.pixel(1159, 698)[0] == 0:
        click(1159, 698)
