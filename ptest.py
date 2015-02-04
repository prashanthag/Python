#!/usr/bin/python
import os
ip_list=["192.168.0.1", "192.168.0.103"]
c=3
r=3
s=ip_list[0].strip('"')
print s
os.system("arp -a 192.168.01 >file")
input=open("./file")
for f in range(3):input.next()
s=input.next()
mac=s.split()[1].replace("-","")
print mac

csec = 1.0/c
rsec = 1.0/c
print csec, rsec
cleft=[]
cright=[]
ctop=[]
cbottom=[]
for i in range(r):
    for j in range(c):
        #cleft[i*c+j]    = j*csec
        cleft.append(j*csec)
        cright.append(1.0-(j+1)*csec)
        ctop.append(i*rsec)
        cbottom.append(1.0-(i+1)*rsec)

#for m in range(r*c):
print  cleft,"\n",cright,"\n",ctop,"\n",cbottom,"\n"


