import pyautogui,time
from PIL import Image
import math
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
#123.69316876852982max distance
u=[0,0,0]
l=[255,255,255]
def dis(pt1):
    #pt1=[255,0,255]
    pt2=[76,255,0]
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance)

img = Image.open("UntitledD.png")
g=[]
k=0
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if (d[0]==d[1]==d[2])!=True:
            if d not in g:
                g.append(d)
                fr=dis(d)
                if k<fr:
                    k=fr
                    print(d)
                    
            for i in range(3):
                if d[i]>u[i]:
                    u[i]=d[i]
                if d[i]<l[i]:
                    l[i]=d[i]
            #print('lol',d,x,y)

print(u,l,g,k)



