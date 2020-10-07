import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
k=0
def inthis(u,l,v):
    if ((v[0]>l[0] and v[0]<u[0] )and((v[1]>l[1] and v[1]<u[1] ))and((v[1]>l[1] and v[1]<u[1]))):
        return True
    else:
        return False
                                    
while True:
    im = pyautogui.screenshot()
    red=[(255,70,50),(190,15,0)]
    blue=[(33,127,255),(8,99,237)]
    k=[im.getpixel((722,648)),im.getpixel((679,742)),im.getpixel((767,744))]
    if ((inthis(red[0],red[1],k[0])or inthis(red[0],red[1],k[1])or inthis(red[0],red[1],k[2]))or
    (inthis(blue[0],red[1],k[0])or inthis(blue[0],red[1],k[1])or inthis(blue[0],red[1],k[2]))):
        print('started')
        pyautogui.moveTo(720,719)
        pyautogui.dragTo(720,275,duration=0.2)
        time.sleep(0.2)
