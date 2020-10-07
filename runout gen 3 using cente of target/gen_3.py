import pyautogui
import time
import math
import subprocess

#print('lol{}'.format(input('enter')))
print('move value: ')
wind_angle=29
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
    y=y-3
    g=1
    for i in range(5):
        #print((x,y+i),inthis(white[0],white[1],im.getpixel((x,y+i))),inthis(white[0],white[1],im.getpixel((x-1,y+i))))
        if (inthis(white[0],white[1],im.getpixel((x,y+i)))and inthis(white[0],white[1],im.getpixel((x-1,y+i))))==False:
            return (False)
    return (True)
def wc2(img,white,x,y):
    y=y-1
    x=x-1
    g=1
    for i in range(2):
        for fd in range(2):
            #print((x+fd,y+i))
            if (inthis(white[0],white[1],im.getpixel((x+i,y+fd))))==False:
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
    for i in range(107):
        if tell_color_dis(im.getpixel((663+i,298)),(198,60,174),90):
            k+=1
            break
    if k==1:
        if tell_color_dis(im.getpixel((700,266)),(255,255,255),20):
            k+=1
        if k==2:
            return True
        else:
            return False
    else:
        return True
first=True


nt0=0
while True:
    im = pyautogui.screenshot()
    red=[(255,70,50)  ,(190,15,0)         ]
    blue=[(65,150,255),(0,80,200)         ]
    pink=[(255,108,255),(100,0,100)       ]
    white=[[255, 255, 255], [200, 190, 200]]#[(255,255,255),(200,200,200)]
    green=[[195, 181, 124],[31, 39, 31]]
    red_pts=[im.getpixel((668,696)),#0
       im.getpixel((686,676)),#1
       im.getpixel((722,667)),#2
       im.getpixel((720,690)),#3
       im.getpixel((758,684)),#4
       im.getpixel((720,719)),#5#prob
       im.getpixel((679,742)),#6
       im.getpixel((755,737)),]#7
    blue_pts=[im.getpixel((661,695)),
              im.getpixel((722,662)),
              im.getpixel((671,774)),
              im.getpixel((719,801)),
              im.getpixel((775,771)),
              im.getpixel((662,791)),
              im.getpixel((735,818)),
              im.getpixel((767,744)),
              im.getpixel((731,634))]
    if (((check_color(red_pts,red)or check_color(red_pts,blue))and(check_dis(red_pts)!=True))or check_color(blue_pts,blue))and fire(im):
        if flag==0:
            #print('flag is now zero')
            tem=lengths(im)
            width=tem[1]
            pos=tem[0]
            if tem[2]==0:
                center=720
            else:
                center=tem[2]

            for i in range(107):
                if (inthis(pink[0],pink[1],im.getpixel((663+i,298)))and inthis(white[0],white[1],im.getpixel((663+i+7,298)))
                    and wc2(im,white,663+i+7,298)and flag==0):
                    ui=im.getpixel((663+i,298))
                    direction=''
                    f=1
                    wind=1
                    if ( wc2(im,white,663+i,288)and wc2(im,white,663+i,308)) :
                        direction='right'
                    else:
                        direction='left'
                    g=663+i+7
                    if wc(im,white,g+23,297):
                        f+=1
                        if wc(im,white,g+44,297):
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
            pyautogui.moveTo(720,719)
            pyautogui.dragTo(center,332,duration=0.2)
        else:

            if direction=='left':
                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(center+wind_angle,332,duration=0.2)
                else:
                    pyautogui.dragTo(center+(8*f),332,duration=0.2)
            else:

                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(center-wind_angle,332,duration=0.2)
                else:
                    pyautogui.dragTo(center-(8*f),332,duration=0.2)
        #'''

    else:
        flag=0
        flag2=0
        if wc2(im,white,519,44)and wc2(im,white,519,100)!=True:
            #time.sleep(4)
            #pyautogui.click(824,714)
            pass
            #pyautogui.click(803,736)
        #time.sleep(.5)'''
