#CASIC - 1.0 - FOSS - classic14
#under GPL v3.0 license

# ===CONF===
time_code = False
work = True
old = False
troll = False

# ==errs==
errA = "CASIC: two errors occured, please contact the developer."
errB = "CASIC: an unknown error occured, please contact the developer."
errC = "CASIC: :3"

import time
import os
import sys

if old == True:
    print("CASIC: you are using an old version of CASIC, note the old versions may have bugs")
    time.sleep(4)
    if sys.platform == "win32":
        os.system('cls')
    elif sys.platform in ("linux", "darwin"):
        os.system('clear')
    else:
        print("CASIC: OS not known. CASIC only works on windows, mac, and linux")
        time.sleep(3)
        print(errA)
        time.sleep(3)
        sys.exit()
    
if work == False:
    print("CASIC: work is set to false, if you are a user please contact the developer. exitng...")
    time.sleep(4)
    sys.exit()
    
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

def update_arch():
    update = input("do you want to update your system? (y/n)")
    if update == "y":
        os.system('sudo pacman -Syu --noconfirm')
        clear()
    else:
        print("will not update")
        clear()

def update_fedora():
    update = input("do you want to update your system? (y/n)")
    if update == "y":
        os.system('sudo dnf upgrade --refresh -y')
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
def put(text):
    print(text)
    time.sleep(2)
    clear()

def used():
    print("CASIC - 1.0 was used in this program.")
    
def open_source():
    print("this program is fully opensource!")

def GPLlicense():
    print("this program is licensed under the GNU General Public License v3.0") 

#time (disabled by default)
def year():
    if not time_code:
        print("CASIC: time_code is disabled")
        return
    time_year = time.strftime("%Y")
    print(time_year)

def month():
    if not time_code:
        print("CASIC: time_code is disabled")
        return
    time_month = time.strftime("%m")
    print(time_month)

def day():
    if not time_code:
        print("CASIC: time_code is disabled")
        return
    time_day = time.strftime("%d")
    print(time_day)    

def hour():
    if not time_code:
        print("CASIC: time_code is disabled")
        return
    time_hour = time.strftime("%H")
    print(time_hour)    

def minute():
    if not time_code:
        print("CASIC: time_code is disabled")
        return
    time_minute = time.strftime("%M")
    print(time_minute)

    