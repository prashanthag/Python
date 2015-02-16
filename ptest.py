#!/usr/bin/python
#import os
ip_list=["192.168.0.1", "192.168.0.103"]
c=3
r=3
roundVal=3
def extractMAC(ss):
	ss=ss.strip('"')
	pid = Popen(["arp", "-a", ss], stdout=PIPE)
	s = pid.communicate()[0]
	input=open("./file","w+");
	input.write(s)
	input.seek(0,0)	
	for f in range(3):input.next()
	mn=input.next()
	mac=mn.split()[1].replace("-","")
	return mac
	
from subprocess import Popen, PIPE


if (c*r)!=len(ip_list):
	print "required devices is ",c*r,"but you entered ",len(ip_list)," ip devices"
	#return
for ss in ip_list:
	print extractMAC(ss);


csec = round(1.0/c,roundVal)
rsec = round(1.0/c,roundVal)
print csec, rsec
cleft=[]
cright=[]
ctop=[]
cbottom=[]
for i in range(r):
    for j in range(c):
        #cleft[i*c+j]    = j*csec
        cleft.append(round((j*csec),roundVal))
        cright.append(round((1.0-(j+1)*csec),roundVal))
        ctop.append(round((i*rsec),roundVal))
        cbottom.append(round((1.0-(i+1)*rsec),roundVal))

#for m in range(r*c):
print  cleft,"\n",cright,"\n",ctop,"\n",cbottom,"\n"


