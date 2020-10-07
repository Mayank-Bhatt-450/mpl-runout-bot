import pyautogui
import time
time.sleep(5)
for i in range(500):
    pyautogui.moveTo(100+i,477)
'''
import pyautogui,time
from pyautogui import moveRel
for i in range(0):
    time.sleep(1)
    print(i)
from pynput.mouse import Listener
import logging
from pyautogui import moveRel
import threading 
import ctypes 
import time 
print('move value: ')

def on_press(x, y, button,pressed):
    if pressed and str(button)=='Button.left':
        #t1 = thread_with_exception('Thread 1') 
        print(pyautogui.position())
    if str(button)=='Button.right':
        print('------------------------------')
    

with Listener( on_click=on_press) as listener:
    listener.join()
'''
