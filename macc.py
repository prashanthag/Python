#import uuid
#print ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
#from uuid import getnode as get_mac
#mac = get_mac()
#print hex(mac)
from subprocess import Popen, PIPE
IP = "192.168.0.1"
pid = Popen(["arp", "-a", IP], stdout=PIPE)
s = pid.communicate()[0]
input=open("./file","w+");
input.write(s)
print s
input.seek(0,0)	
for f in range(3):input.next()
mn=input.next()
print mn
mac=mn.split()[1].replace("-","")
print mac

 