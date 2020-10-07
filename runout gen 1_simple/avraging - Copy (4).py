import pyautogui,time
from PIL import Image
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
u=[0,0,0]
l=[255,255,255]
img = Image.open("aas.png")
g=[]
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if (d[0]==d[1]==d[2])!=True:
            if d not in g:
                g.append(d)
            #print('lol',d,x,y)

print(u,l)



