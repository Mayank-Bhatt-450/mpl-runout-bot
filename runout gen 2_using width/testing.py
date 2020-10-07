f=open('op3.txt','r')
r=f.read()
f.close()
p=r.split('\n')
no=[]
k={}
for i in p:
    u=i.split(',')
    if int(u[3]) not in no:
        no.append(int(u[3]))
        k[str(u[3])]=1
    else:
        k[str(u[3])]+=1


print(sorted(no) )
for i in sorted(no):
    print(i,'=',k[' '+str(i)])
