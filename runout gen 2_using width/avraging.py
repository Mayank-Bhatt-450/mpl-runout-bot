import pyautogui,time
from PIL import Image
import math
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
#123.69316876852982max distance
u=[0,0,0]
l=[112,194,127]
def dis(pt1):#!153.13392831113555
    #pt1=[112,186,237]#!108.54031509075327
    pt2=(198,60,174)#(228, 177, 110)#[216,0,158]#[33,124,245]
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance)

img = Image.open("wadsf.png")
g=[]
k=0
pix=[0,0,0]
pixno=0
no=[(5, 49, 82),
(1, 39, 85),
(1, 38, 85),
(2, 37, 83),
(1, 33, 80),
(1, 38, 75),
(2, 37, 72),
(4, 28, 70),
(1, 28, 60),
(1, 17, 47),]#[(153, 165, 177),(74, 83, 92),(77, 86, 95)]
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if (d[0]==d[1]==d[2])!=True and d[0]<0 :
            pixno+=1
            pix[0]+=d[0]
            pix[1]+=d[1]
            pix[2]+=d[2]
            if d not in g :
                #g.append(d)
                fr=dis(d)
                if k<fr and d not in no:
                    k=fr
                    print(d)
                    
            for i in range(3):
                if d[i]>u[i]:
                    u[i]=d[i]
                if d[i]<l[i]:
                    l[i]=d[i]
            #print('lol',d,x,y)


print(k,pix[0]/pixno,pix[1]/pixno,pix[2]/pixno)



