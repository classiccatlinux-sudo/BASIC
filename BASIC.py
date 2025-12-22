#BASIC - 1.0 - FOSS - classic14
    
import time
import os
import sys

#basic_python
def clear():
    if sys.platform == "win32":
        os.system('cls')
    elif sys.platform in ("linux", "darwin"):
        os.system('clear')
    else:
        print("BASIC: err(OS for clear not known")
    
def time3():
    time.sleep(3)

def time5():
    time.sleep(5)
    
def time1():
    time.sleep(1)
    
def update_debian():
    update = input("do you want to update your system? (y/n)")
    if update == "y":
        os.system('sudo apt update -y && sudo apt full-upgrade -y')
        clear()
    else:
        print("will not update")
        clear()
    
def reboot():
    if sys.platform == "win32":
        os.system('shutdown /r /t 0')
    elif sys.platform == "linux" or sys.platform == "darwin":
        os.system('reboot')
    else:
        print("BASIC: err(OS for reboot not known"))
            
            
#extras
def used():
    print("BASIC - 1.0 was used in this program.")
    
def open_source():
    print("this program is fully opensoucre!")

#def cat():
    time.sleep(1)
    print("  ∧,,,,∧ ")
    time.sleep(1)
    print("(  ̳• · • ̳) ")
    time.sleep(1)
    print("/     づ♡ BASIC was used in this program. ")

