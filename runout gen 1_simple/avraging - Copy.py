import pyautogui,time
from PIL import Image
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
u=[0,0,0]
l=[255,255,255]
img = Image.open("U.png")
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if (d[0]==d[1]==d[2])!=True:
            #print('lol',d,x,y)
            for i in range(3):
                if d[i]>u[i]:
                    u[i]=d[i]
                if d[i]<l[i]:
                    l[i]=d[i]
print(u,l)



