import pyautogui
import time
import math
f = open('op.txt','w')
f.close()
#print('lol{}'.format(input('enter')))
print('move value: ')
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
def dis(pt1):
    #pt1=[255,0,255]
    pt2=[76,255,0]
    distance=math.sqrt(  ((pt1[0]-pt2[0])**2)+((pt1[1]-pt2[1])**2)+((pt1[2]-pt2[2])**2)  )
    return(distance<=187.11761007451972)
def check_dis(k):
    for i in range(len(k)):
        #print(dis(k[i]),i)
        if dis(k[i]):
            return True
    return False
flag=0
direction=''
f=1
wind=1
flag2=0
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
        
def lengths(im):#172 error
    color=[[195, 181, 124],[31, 39, 31]]
    p=688
    j=[]
    b=[]
    pos=''
    width=0
    bp=0
    bt=50
    for i in range(70):
        #print(tell_color_dis(im.getpixel((p+i,441)),[33,124,245],169.45205811674285))
        if tell_color_dis(im.getpixel((p+i,441)),[0,100,252],174.0833133875846):
            j.append(p+i)
            #break
        #print((tell_color_dis(im.getpixel((p+i,441)),[0,00,0],50),p+i, tell_color_dis(im.getpixel((p+i,441)),[173,173,173],200.00)))
        #print(bt)
        if (tell_color_dis(im.getpixel((p+i,441)),[0,00,0],bt)or tell_color_dis(im.getpixel((p+i,441)),[173,173,173],200.00)or True) :
            #print(p+i)
            for hk in range(16):
                if tell_color_dis(im.getpixel((p+i,441-hk)),[0,00,0],bt):
                    #print(tell_color_dis(im.getpixel((p+i,441-hk)),[0,00,0],100),(p+i,441-hk))
                    b.append(p+i)
                    
                    if bp==0:
                        bp=1
                        bt=100
                    break
    if b !=[] and j!=[]:
        if b[0]<j[0]:
            pos='left'
            oi=j[len(j)-1 ]-j[endtoend(j)]
            if (oi==0):
                width=j[len(j)-1]-b[0]#(j[len(j)-1]-j[0])+(j[0]-b[0])
                #print(width)
            else:
                width=j[len(j)-1]-b[0]#(j[len(j)-1]-j[0])+(j[len(j)-1]-j[endtoend(j)])
        if b[0]<j[len(j)-1] and b[0]>j[0]:
            pos='mid'
            width=j[len(j)-1]-j[0]
        if b[0]>j[len(j)-1]:
            pos='right'
            oi=j[len(j)-1]-j[endtoend(j)]
            #print(oi)#j[len(j)-1]-j[endtoend(j)])
            if (oi==0):
                
                width=b[len(b)-1]-j[0]#(j[len(j)-1]-j[0])+(b[0]-j[len(j)-1])+len(b)
                #print(width)
            else:
                width=b[len(b)-1]-j[0]#(j[len(j)-1]-j[0])+(j[len(j)-1]-j[endtoend(j)])
    else:
        pos='default'
    print(j,b)
    return(pos,width)
first=True

        
nt0=0            
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
    #print(k)
    #print((check_color(k,red)or check_color(k,blue))and(check_color(k,green)!=True),(check_color(k,green,0)),(check_color(k,green)))
    if (((check_color(k,red)or check_color(k,blue))and(check_dis(k)!=True))or check_color(blue_pts,blue)):
        
        for i in range(107):
            if (inthis(pink[0],pink[1],im.getpixel((663+i,298)))and inthis(white[0],white[1],im.getpixel((663+i+7,298))) and wc2(im,white,663+i+7,298)and flag==0):
                ui=im.getpixel((663+i,298))
                direction=''
                f=1
                wind=1
                tem=lengths(im)
                width=tem[1]
                pos=tem[0]
                if ( wc2(im,white,663+i,288)and wc2(im,white,663+i,308)) :
                    direction='right'
                else:
                    direction='left'
                g=663+i+7
                if wc(im,white,g+23,297):
                    f+=1
                    if wc(im,white,g+44,297):
                        f+=1
                #print(direction,'at',663+i,' ',f,g+21)
                #print(direction,f,lengths(im))
                flag=1
                break
            else:
                if flag!=1:
                    direction=''

        if direction!=''and flag2!=1 and f==3:
            print(direction+' '+str(f)+' '+str(lengths(im)))
            #im.save(str(lengths(im))+'__'+str(nt0)+direction+' '+str(f)+' '+'.png')
            nt0+=1
        flag2=1

        '''
        
        
        if direction=='':
            pyautogui.moveTo(720,719)
            pyautogui.dragTo(720,332,duration=0.2)
        else:
            angle=wind_angle
            if width>=10 and width<=11:
                angle=wind_angle
            elif width>=11 and width<=12:
                angle=wind_angle
            elif width>=12 and width<=13:
                angle=wind_angle
            elif width>=13 and width<=14:
                angle=wind_angle
            elif width>=14 and width<=15:
                angle=wind_angle
            elif width>=15 and width<=16:
                angle=wind_angle
            elif width>=16 and width<=17:
                angle=wind_angle
            elif width>=17 and width<=18:
                angle=wind_angle
            elif width>=18 and width<=19:
                angle=wind_angle
            elif width>=19 and width<=20:
                angle=wind_angle
            elif width>=20 and width<=21:
                angle=wind_angle
            elif width>=21 and width<=22:
                angle=wind_angle
            elif width>=22 and width<=23:
                angle=wind_angle
            elif width>=23 and width<=24:
                angle=wind_angle
            elif width>=24 and width<=25:
                angle=wind_angle
            elif width>=25 and width<=26:
                angle=wind_angle
            elif width>=26 and width<=27:
                angle=wind_angle
            elif width>=27 and width<=28:
                angle=wind_angle
            elif width>=28 and width<=29:
                angle=wind_angle
            elif width>=29 and width<=30:
                angle=wind_angle
            elif width>=30 and width<=31:
                angle=wind_angle
            elif width>=31 and width<=32:
                angle=wind_angle
            elif width>=32 and width<=33:
                angle=wind_angle
            elif width>=33 and width<=34:
                angle=wind_angle
            elif width>=34 and width<=35:
                angle=wind_angle
            elif width>=35 and width<=36:
                angle=wind_angle
            elif width>=36 and width<=37:
                angle=wind_angle
            elif width>=37 and width<=38:
                angle=wind_angle
            elif width>=38 and width<=39:
                angle=wind_angle
            elif width>=39 and width<=40:
                angle=wind_angle
            else:
                angle=wind_angle
            if direction=='left':
                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(720+angle,332,duration=0.2)
                else:
                    pyautogui.dragTo(720+(8*f),332,duration=0.2)
            else:

                pyautogui.moveTo(720,719)
                if f==3:
                    pyautogui.dragTo(720-angle,332,duration=0.2)
                else:
                    pyautogui.dragTo(720-(8*f),332,duration=0.2)
        #'''

    else:
        flag=0
        flag2=0
        if wc2(im,white,519,44):
            #pyautogui.click(784,767)
            pass
            #pyautogui.click(803,736)
        #time.sleep(.5)'''
