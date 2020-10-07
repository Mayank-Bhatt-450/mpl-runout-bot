'''
import subprocess
#input touchscreen swipe 541 1726 608 773 2
cmd_input = """adb
adb shell
input touchscreen swipe 541 1726 608 773 2"""

process = subprocess.Popen(
    "adb shell",
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE
)
process.communicate( b"input touchscreen swipe 541 1726 608 773 2\n")
'''
'''
from PIL import ImageGrab
import win32gui

hwnd = win32gui.FindWindow(None, r'Task Manager')
win32gui.SetForegroundWindow(hwnd)
dimensions = win32gui.GetWindowRect(hwnd)

image = ImageGrab.grab(dimensions)
image.show()
'''
import pyscreenshot
import pyscreenshot as ImageGrab
im = pyscreenshot.grab(bbox=None, childprocess='Task Manager', backend=None)('Task Manager')#ImageGrab.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
im.show()
