import pyautogui
import time
import math
import subprocess

#print('lol{}'.format(input('enter')))
print('move value: ')

def inthis(u,l,v):
    if ((v[0]>=l[0] and v[0]<=u[0] )and((v[1]>=l[1] and v[1]<=u[1] ))and((v[2]>=l[2] and v[2]<=u[2]))):
        return True
    else:
        return False
def inthis2(u,l,v):
    if ((v[0]>=l[0] and v[0]<=u[0] )and((v[1]>=l[1] and v[1]<=u[1] ))and((v[2]>=l[2] and v[2]<=u[2]))):
        return True
    else:
        return False
def wc(img,white,x,y):
    y1=y-3
    g=1
    for i in range(5):
        pyautogui.moveTo(x,y1+i)
        print((x,y+i))
        #print((x,y+i),inthis(white[0],white[1],im.getpixel((x,y+i))),inthis(white[0],white[1],im.getpixel((x-1,y+i))))
        if (inthis(white[0],white[1],im.getpixel((x,y1+i)))and
            inthis(white[0],white[1],im.getpixel((x-1,y1+i))))==False:
            if y==477:
                pass
                #print(x,y+i)
            return (False)
    return (True)

def dis(pt1):
    #pt1=[255,0,255]
    pt2=[76,255,0]
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=187.11761007451972)
def check_dis(k):
    for i in range(len(k)):
        if dis(k[i]):
            return True
    return False
flag=0
direction=''
f=1
wind=1
flag2=0
center=0
def tell_color_dis(pt1,pt2,h=134.74791278531924):
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=h)#v25.495097567963924#h134.74791278531924
def check_color(k,color,m=1):
    for i in range(len(k)):
        if(inthis(color[0],color[1],k[i])==True):

            if color[0]==[195, 181, 124] and m==0:
                print(k[i],i,len(k))

            return True
    return False
def wc2(img,white,x,y):
    #print(x,y)
    y=y-1
    x=x-1
    g=1
    for i in range(2):
        for fd in range(2):
            #print((x+fd,y+i))
            if (tell_color_dis(im.getpixel((x+i,y+fd)),(254,235,237),70.71774883294857 )==False):
                return (False)
    return (True)
def endtoend(l):
    k=[]
    for i in range(len(l)-1):
        if (l[i+1]-l[i])>2:
            return i
    return len(l)-1
def calculate_stumps(j,b):
    stumps=2
    for i in range(len(j)-1):
        if (j[i+1]-j[i])>1:
            stumps+=1
            #print('blue',(j[i+1],j[i]),(j[i+1]-j[i]),'stumps=',stumps)
    for i in range(len(b)-1):
        if (b[i+1]-b[i])>1:
            stumps+=1
            #print('black',(j[i+1],j[i]),(j[i+1]-j[i]),'stumps=',stumps)
    if len(j)<(len(b)*2)-3:
        stumps=4
    #print (len(j),(len(b)*2)-3)
    #print(stumps)
    return stumps
def lengths(im):
    color=[[195, 181, 124],[31, 39, 31]]
    p=688
    j=[]
    b=[]
    pos=''
    width=0
    bp=0
    bt=50
    center=0
    for i in range(70):
        pix_val=im.getpixel((p+i,441))
        if tell_color_dis(pix_val,(46,109,205),110.9414259868693 ):
            j.append(p+i)
        if (tell_color_dis(pix_val,[0,00,0],bt)or tell_color_dis(pix_val,[173,173,173],200.00)or True) :
            for hk in range(16):
                if tell_color_dis(im.getpixel((p+i,441-hk)),[0,00,0],bt):
                    b.append(p+i)
                    if bp==0:
                        bp=1
                        bt=100
                    break
    #print('in con=',b !=[] , j!=[] , calculate_stumps(j,b)==3)
    if b !=[] and j!=[] and (calculate_stumps(j,b)==3 or calculate_stumps(j,b)==2):
        if b[0]<j[0]:#left
            pos='left'
            oi=j[len(j)-1 ]-j[endtoend(j)]
            if (oi==0):
                width=j[len(j)-1]-b[0]
            else:
                width=j[len(j)-1]-b[0]
            center=b[0]+int(width/2)

        if b[0]<j[len(j)-1] and b[0]>j[0]:#mid
            pos='mid'
            width=j[len(j)-1]-j[0]
            center=j[0]+int(width/2)
        if b[0]>j[len(j)-1]:#rigth
            pos='right'
            oi=j[len(j)-1]-j[endtoend(j)]
            if (oi==0):
                width=b[len(b)-1]-j[0]
            else:
                width=b[len(b)-1]-j[0]
            center=j[0]+int(width/2)
    else:
        pos='default'
    #print('bluestumps=',j,'\nblack stumps=',b,calculate_stumps(j,b))
    return(pos,width,center)
def fire(im):
    x,y=714,184
    k=0
    for i in range(177):
        if tell_color_dis(im.getpixel((364+i,477)),(198,60,174),90):
            k+=1
            break
    if k==1:
        if tell_color_dis(im.getpixel((416,393)),(255,255,255),20):
            k+=1
        if k==2:
            return True
        else:
            return False
    else:
        return True
first=True


nt0=0
lifes=578
last_hit=None
wind_angle=23#52
wind1=15
wind2=26
while True:
    im = pyautogui.screenshot()
        

    red=[(255,70,50)  ,(190,15,0)         ]
    blue=[(65,150,255),(0,80,200)         ]
    pink=[(255,108,255),(100,0,100)       ]
    white=[[255, 255, 255], [200, 190, 200]]#[(255,255,255),(200,200,200)]
    green=[[195, 181, 124],[31, 39, 31]]
    red_pts=[im.getpixel((453,1067)),#0
       im.getpixel((505,1082)),#1
       im.getpixel((453,1067)),#2
       im.getpixel((510,1094)),#3
       im.getpixel((367,1113)),#4
       im.getpixel((450,1104)),#5#prob
       im.getpixel((506,1179)),#6
       im.getpixel((450,1150)),
       im.getpixel((385,1187)),]#7
    
    blue_pts=[im.getpixel((420,1015)),
              im.getpixel((453,1059)),
              im.getpixel((356,1112)),
              im.getpixel((525,1190)),
              im.getpixel((538,1233)),
              im.getpixel((372,1238)),
              im.getpixel((357,1265)),
              im.getpixel((448,1281)),
              im.getpixel((474,1308))]
    #print(((((check_color(red_pts,red), check_color(red_pts,blue)),(check_dis(red_pts)!=True)), check_color(blue_pts,blue)),fire(im)))
    if ((((check_color(red_pts,red)or check_color(red_pts,blue))and(check_dis(red_pts)!=True))or check_color(blue_pts,blue))and fire(im)):
        if flag==0:
            #print('flag is now zero')
            tem=lengths(im)
            width=tem[1]
            pos=tem[0]
            if tem[2]==0:
                center=720
            else:
                center=tem[2]

            for i in range(177):
                #'''
                if inthis(pink[0],pink[1],im.getpixel((432+i,477))):
                    print(inthis(pink[0],pink[1],im.getpixel((432+i,477))),
                        inthis(white[0],white[1],im.getpixel((432+i+11,477))),
                        wc(im,white,432+i+11,477), flag==0,(432+i,477))#'''

                if (inthis(pink[0],pink[1],im.getpixel((432+i,477)))and
                    inthis(white[0],white[1],im.getpixel((432+i+11,477)))and
                    wc(im,white,432+i+11,477)and flag==0):
                    print('wind detected')
                    direction=''
                    f=1
                    wind=1
                    if ( wc2(im,white,432+i,461)and
                         wc2(im,white,432+i,493)) :
                        direction='right'
                    else:
                        direction='left'
                    g=432+i
                    if wc(im,white,g+48,477):
                        f+=1
                        if wc(im,white,g+85,477):
                            f+=1
                    break
                else:
                    if flag!=1:
                        direction=''
            flag=1
            if direction!=''and flag2!=1 :#and f==3:
                u7=lengths(im)
                print(direction+' wind='+str(f)+' '+str(u7))
                #im.save('G:\\Downloads\\Compressed\\scrcpy-win64-v1.8\\MLP\\runout\\runout gen 2\\test_1\\New folder - Copy ('+str(u7[1])+')'+"\\"+str(u7)+'__'+str(nt0)+direction+' '+str(f)+' '+'.png')
                nt0+=1
            flag2=1


        #'''


        if direction=='':
            pyautogui.moveTo(450,1256)
            pyautogui.dragTo(450,521,duration=0.2)
        else:

            angle=wind_angle
            '''
            if width>=10 and width<=11:
                angle=wind_angle+5
            elif width>=11 and width<=12:
                angle=wind_angle+5
            elif width>=12 and width<=13:
                angle=wind_angle+5
            elif width>=13 and width<=14:
                angle=wind_angle+5
            elif width>=14 and width<=15:
                angle=wind_angle+5
            elif width>=15 and width<=16:
                angle=wind_angle
            elif width>=16 and width<=17:
                angle=wind_angle-2
            elif width>=17 and width<=18:
                angle=wind_angle-2
            elif width>=18 and width<=19:
                angle=wind_angle-2
            elif width>=19 and width<=20:
                angle=wind_angle
            elif width>=20 and width<=21:
                angle=wind_angle-2
            elif width>=21 and width<=22:
                angle=wind_angle-2
            elif width>=22 and width<=23:
                angle=wind_angle
            elif width>=23 and width<=24:
                angle=wind_angle-2
            elif width>=24 and width<=25:
                angle=wind_angle-2
            elif width>=25 and width<=26:
                angle=wind_angle-2
            elif width>=26 and width<=27:
                angle=wind_angle-2
            elif width>=27 and width<=28:
                angle=wind_angle-2
            elif width>=28 and width<=29:
                angle=wind_angle-2
            elif width>=29 and width<=30:
                angle=wind_angle-2
            elif width>=30 and width<=31:
                angle=wind_angle-2
            elif width>=31 and width<=32:
                angle=wind_angle-2
            elif width>=32 and width<=33:
                angle=wind_angle-2
            elif width>=33 and width<=34:
                angle=wind_angle-2
            elif width>=34 and width<=35:
                angle=wind_angle-2
            elif width>=35 and width<=36:
                angle=wind_angle-2
            elif width>=36 and width<=37:
                angle=wind_angle-2
            elif width>=37 and width<=38:
                angle=wind_angle-2
            elif width>=38 and width<=39:
                angle=wind_angle-2
            elif width>=39 and width<=40:
                angle=wind_angle-2
            else:
                angle=wind_angle+1
            #'''
            if direction=='left':
                pyautogui.moveTo(450,1256)
                if f==3:
                    pyautogui.dragTo(450+angle,521,duration=0.2)
                elif f==2:
                    pyautogui.dragTo(450+(wind2),521,duration=0.2)
                elif f==1:
                    pyautogui.dragTo(450+(wind1),521,duration=0.2)
            else:
                pyautogui.moveTo(450,1256)
                if f==3:
                    pyautogui.dragTo(450-angle,521,duration=0.2)
                elif f==2:
                    pyautogui.dragTo(450-(wind2),521,duration=0.2)
                elif f==1:
                    pyautogui.dragTo(450-(wind1),521,duration=0.2)        #'''

    else:
        flag=0
        flag2=0
        if wc2(im,white,519,44)and wc2(im,white,519,100)!=True:
            #time.sleep(4)
            #pyautogui.click(824,714)
            pass
            #pyautogui.click(803,736)
        #time.sleep(.5)'''
