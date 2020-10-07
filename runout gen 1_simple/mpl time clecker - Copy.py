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
                                    
while True:#157 562(589)
    im = pyautogui.screenshot()
    #inthis([156,230,255],[82,160,190],d)
    red=[(255,27,21),(190,15,0)]
    k=[im.getpixel((722,648)),im.getpixel((679,742)),im.getpixel((767,744))]
    if (inthis(red[0],red[l],k[0])or red[0],red[l],k[1])or red[0],red[l],k[2])):
        print('started',clp, 541)
        pyautogui.click(clp, 541)
        k+=1
        time.sleep(1)
        break

