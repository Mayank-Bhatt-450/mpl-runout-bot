import pyautogui,time
from PIL import Image
import math
'''
img = pyautogui.screenshot()
img.save('new.jpg')
k=time.time()'''
#123.69316876852982max distance
def dis(pt1):#!153.13392831113555
    #pt1=[112,186,237]#!108.54031509075327
    pt2=(46,109,205)#(228, 177, 110)#[216,0,158]#[33,124,245]
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance)

img = Image.open("blue.png")
g=[]
k=0
pix=[0,0,0]
pixno=0
no=[(123, 136, 142) ,
(113, 109, 88) ,
(115, 119, 113) ,
(54, 76, 76) ,]#[(153, 165, 177),(74, 83, 92),(77, 86, 95)]
for y in range(900):
    for x in range(1440):
        d=img.getpixel((x,y))
        if (d[0]==d[1]==d[2])!=True and (d[0]!=255 and d[1]!=0 and d[2]!=0)and (d not in no) :
            pixno+=1
            pix[0]+=d[0]
            pix[1]+=d[1]
            pix[2]+=d[2]
            if d not in g :
                #g.append(d)
                fr=dis(d)
                if k<fr and d not in no:
                    k=fr
                    print(d,',')

print('max_distance=',k,
      '\navrage_pts=',pix[0]/pixno,pix[1]/pixno,pix[2]/pixno)



