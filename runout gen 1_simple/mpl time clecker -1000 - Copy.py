import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
#k=0
wind_angle=28
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
        
flag=0
direction=''
f=1
wind=1
def check_color(k,color,m=1):
    for i in range(len(k)):
        if(inthis(color[0],color[1],k[i])==True):

            if color[0]==[195, 181, 124] and m==0:
                print(k[i],i,len(k))
                
            return True
    return False
first=True
while True:
    im = pyautogui.screenshot()
    red=[(255,70,50)  ,(190,15,0)         ]
    blue=[(65,150,255),(0,80,200)         ]
    pink=[(255,108,255),(100,0,100)       ]
    white=[[255, 255, 255], [200, 190, 200]]#[(255,255,255),(200,200,200)]
    green=[[195, 181, 124],[31, 39, 31]]
    k=[im.getpixel((668,696)),#0
       im.getpixel((686,676)),#1
       im.getpixel((722,667)),#2
       im.getpixel((720,690)),#3
       im.getpixel((758,684)),#4
       im.getpixel((720,719)),#5
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
    #print(k)
    #print((check_color(k,red)or check_color(k,blue))and(check_color(k,green)!=True),(check_color(k,green)))
    if (((check_color(k,red)or check_color(k,blue))and(check_color(k,green,0)!=True))or check_color(blue_pts,blue)):
        for i in range(107):
            if (inthis(pink[0],pink[1],im.getpixel((663+i,298)))and inthis(white[0],white[1],im.getpixel((663+i+7,298))) and wc2(im,white,663+i+7,298)and flag==0):
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
                print(direction,'at',663+i,' ',f,g+21)
                flag=1
                break
            else:
                if flag!=1:
                    direction=''
        #'''

        if direction=='':
            
            pyautogui.moveTo(720,719)
            pyautogui.dragTo(720,332,duration=0.2)
        else:
            if direction=='left':

                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(720+(wind_angle),332,duration=0.2)
                else:
                    pyautogui.dragTo(720+(8*f),332,duration=0.2)
            else:

                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(720-(wind_angle),332,duration=0.2)
                else:
                    pyautogui.dragTo(720-(8*f),332,duration=0.2)
        #'''

    else:
        flag=0
        #time.sleep(.5)'''
