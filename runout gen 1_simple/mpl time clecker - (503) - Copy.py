import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
#k=0
wind_angle=27
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
    y=y-5
    g=1
    for i in range(9):
        if (inthis(white[0],white[1],im.getpixel((x,y+i)))and inthis(white[0],white[1],im.getpixel((x-1,y+i))))==False:
            return (False)
    return (True)
def wc(img,white,x,y):
    y=y-1
    x=y-1
    g=1
    for i in range(2):
        for fd in range(2):
            if (inthis(white[0],white[1],im.getpixel((x+i,y+fd)))and inthis(white[0],white[1],im.getpixel((x-i,y+fd))))==False:
                return (False)
    return (True)
        
flag=0
direction=''
f=1
wind=1
while True:
    im = pyautogui.screenshot()
    red=[(255,70,50)  ,(190,15,0)         ]
    blue=[(65,150,255),(0,80,200)         ]
    pink=[(255,108,255),(100,0,100)       ]
    white=[[255, 255, 255], [200, 183, 200]]#[(255,255,255),(200,200,200)]
    k=[im.getpixel((722,648)),im.getpixel((679,742)),
       im.getpixel((767,744)),im.getpixel((720,719)),
       im.getpixel((779,775)),im.getpixel((719,811)),
       im.getpixel((671,774))]
    #print(k)
    if ((inthis(red[0],red[1],k[0]or inthis(red[0],red[1],k[1])or inthis(red[0],red[1],k[2]))or inthis(red[0],red[1],k[3])or inthis(red[0],red[1],k[4])or inthis(red[0],red[1],k[5]))
        or
        (inthis(blue[0],blue[1],k[0])or inthis(blue[0],blue[1],k[1])or inthis(blue[0],blue[1],k[2])or inthis(blue[0],blue[1],k[3])or inthis(blue[0],blue[1],k[4])or inthis(blue[0],blue[1],k[5]))):
        for i in range(107):
            #if flag==0:
            #    print((663+i,298),'=pink=',inthis(pink[0],pink[1],im.getpixel((663+i,298))),'(663+i+7,298)white=',inthis(white[0],white[1],im.getpixel((663+i+7,298))))

            if (inthis(pink[0],pink[1],im.getpixel((663+i,298)))and inthis(white[0],white[1],im.getpixel((663+i+7,298)))and flag==0):
                ui=im.getpixel((663+i,298))
                direction=''
                f=1
                wind=1
                if (inthis2(white[0],white[1],im.getpixel((663+i,288)))):
                    #print(im.getpixel((663+i,288)))
                    direction='right'
                else:
                    #print(im.getpixel((663+i,288)))
                    direction='left'
                g=663+i+7
                if(inthis(white[0],white[1],im.getpixel((g+25,297)))):
                    f+=1
                    if(inthis(white[0],white[1],im.getpixel((g+46,297)))):
                        f+=1
                print(direction,'at',663+i,' ',f,g+21)
                flag=1
                break
            else:
                if flag!=1:
                    direction=''
        #'''

        if direction=='':
            #print(direction,'front')
            pyautogui.moveTo(720,719)
            pyautogui.dragTo(720,332,duration=0.2)
        else:
            if direction=='left':
                #print('left')
                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(720+(wind_angle),332,duration=0.2)
                else:
                    pyautogui.dragTo(720+(8*f),332,duration=0.2)
            else:
                #print('right',flag,direction,f,wind)
                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(720-(wind_angle),332,duration=0.2)
                else:
                    pyautogui.dragTo(720-(8*f),332,duration=0.2)
        #'''

    else:
        flag=0
        #time.sleep(0.2)'''
