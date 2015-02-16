#!/usr/bin/python
#import os
from subprocess import Popen, PIPE
ip_list=["192.168.0.1", "192.168.0.103"]
c=3
r=3
for ss in ip_list:
	ss=ss.strip('"')
	pid = Popen(["arp", "-a", ss], stdout=PIPE)
	s = pid.communicate()[0]
	input=open("./file","w+");
	input.write(s)
	input.seek(0,0)	
	for f in range(3):input.next()
	mn=input.next()
	mac=mn.split()[1].replace("-","")
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


