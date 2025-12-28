#CASIC - 1.0 - FOSS - classic14
#under GPL v3.0 license
   
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
        print("CASIC: OS not known. CASIC only works on windows, mac, and linux,")

def wait(wt):
    time.sleep(wt)

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
        print("CASIC: OS not known. CASIC only works on windows, mac, and linux,")
            
            
#extras
def used():
    print("CASIC - 1.0 was used in this program.")
    
def open_source():
    print("this program is fully opensource!")

def GPLlicense():
    print("this program is licensed under the GNU General Public License v3.0")   
