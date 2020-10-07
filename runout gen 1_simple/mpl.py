import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
while True:#157 562(589)
    im = pyautogui.screenshot()
    for i in range(405):
        d=im.getpixel((157+i, 589))
        if ((d[0]>82 and d[0]<156 )and(d[1]>160 and d[1]<230 )and(d[2]>190 and d[2]<255 )):
            print ('got it ',(157+i, 589))
        
'''
    if (im.getpixel((718, 761))!=(174,21,39)):
        time.sleep(1)
        pyautogui.click(718, 761)
'''
