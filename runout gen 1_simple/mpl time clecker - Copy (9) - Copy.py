import pyautogui
import time

'''
#it reaches to top in 0.4 second
'''
print('move value: ')
#m=int(input())
k=0
wind_angle=27
def inthis(u,l,v):
    #print((v[0]>=l[0] , v[0]<=u[0] ),((v[1]>=l[1] , v[1]<=u[1] )),((v[1]>=l[1] , v[1]<=u[1])))
    if ((v[0]>=l[0] and v[0]<=u[0] )and((v[1]>=l[1] and v[1]<=u[1] ))and((v[1]>=l[1] and v[1]<=u[1]))):
        print((v[0]>=l[0] , v[0]<=u[0] ),((v[1]>=l[1] , v[1]<=u[1] )),((v[1]>=l[1] , v[1]<=u[1])))
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
        
flag=0
k=''
f=1
wind=1
while True:

    im = pyautogui.screenshot()
    red=[(255,70,50)  ,(190,15,0)         ]
    blue=[(65,150,255),(0,99,237)         ]
    pink=[(255,90,255),(120,0,120)       ]
    white=[[255, 255, 255], [230, 183, 230]]#[(255,255,255),(200,200,200)]
    k=[im.getpixel((722,648)),im.getpixel((679,742)),
       im.getpixel((767,744)),im.getpixel((720,719)),
       im.getpixel((779,775)),im.getpixel((719,811)),
       im.getpixel((671,774))]
    if ((inthis(red[0],red[1],k[0]or inthis(red[0],red[1],k[1])or inthis(red[0],red[1],k[2]))or inthis(red[0],red[1],k[3])or inthis(red[0],red[1],k[4])or inthis(red[0],red[1],k[5]))
        or
        (inthis(blue[0],blue[1],k[0])or inthis(blue[0],blue[1],k[1])or inthis(blue[0],blue[1],k[2])or inthis(blue[0],blue[1],k[3])or inthis(blue[0],blue[1],k[4])or inthis(blue[0],blue[1],k[5]))):
        for i in range(107):

            #im.getpixel((663+i,298))
            #print('\n\n\n')
            #print((inthis(pink[0],pink[1],im.getpixel((663+i,298))), inthis(white[0],white[1],im.getpixel((663+i+7,298))),(wc(im,white,663+i+7,298))))
            if (inthis(pink[0],pink[1],im.getpixel((663+i,298)))and inthis(white[0],white[1],im.getpixel((663+i+7,298)))and(wc(im,white,663+i+7,298))and flag==0):
                if(wc(im,white,663+i+7,298))!=False:
                    im.save(str(663+i)+str(298)+'.png')
                    #exit()
                ui=im.getpixel((663+i,298))
                
                print((inthis(pink[0],pink[1],ui), inthis(white[0],white[1],im.getpixel((663+i+7,298))),(wc(im,white,663+i+7,298))))
                print(ui)
                k=''
                f=1
                wind=1
                if (inthis(white[0],white[1],im.getpixel((663+i,288)))):
                       k='right'
                else:
                    print(im.getpixel((663+i,288)))
                    k='left'
                g=663+i+7
                #+21

                if(inthis(white[0],white[1],im.getpixel((g+21,297)))):
                    f+=1
                    if(inthis(white[0],white[1],im.getpixel((g+42,297)))):
                        f+=1
                print(k,'at',663+i,' ',f,g+21)
                flag=1
                break
            else:
                if flag!=1:
                    k=''
        '''

        if k=='':
            pyautogui.moveTo(720,719)
            pyautogui.dragTo(720,332,duration=0.2)
        else:
            if k=='left':
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
        '''

    else:
        flag=0
        #time.sleep(0.2)'''
