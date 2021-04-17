"""
An Amazing Python tool to get all stored wifi passwords on your Windows PC.
Created By: Subroto Das
"""
#Imported Modules
import subprocess

#Variables
commands=subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode('utf-8').split('\n')
networks=[i.split(':') [1] [1:-1] for i in commands if "All User Profile" in i]

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
purple = '\033[95m'
Bwhite = '\033[97m'
blue = '\033[94m'
gray = '\033[90m'

#Label
print (cyan+bold+"••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")
print (blue+bold+"""
___       _______         __________               ______
__ |     / /___(_)        ___  ____/____  ____________  /_______ ________
__ | /| / / __  / __________  /_    _  / / /_  ___/__  //_/_  _ \__  ___/
__ |/ |/ /  _  /  _/_____/_  __/    / /_/ / / /__  _  ,<   /  __/_  /
____/|__/   /_/           /_/       \__,_/  \___/  /_/|_|  \___/ /_/"""+cyan+bold+"""

[  F u c k   A l l   S t o r e d   W i f i   P a s s w o r d s  ]"""+yellow+bold+"""
-----------------------------------------------------------------------------------------------------"""+purple+bold+"""
........................................................................................."""+blue+bold+"""
Created By"""+red+bold+"""   : """+cyan+bold+"""[ S u b r o t o  D a s ]"""+cyan+bold+"""
Code Name"""+red+bold+"""    : """+blue+bold+"""[ Tr0j@n_Pr!nc3 ]"""+purple+bold+"""
........................................................................................."""+blue+bold+"""
Team Name"""+red+bold+"""    : """+cyan+bold+"""[ U n d e r w o r l d  H a c k e r s ]"""+cyan+bold+"""
We Are"""+red+bold+"""       : """+blue+bold+"""[ Tr0j@n_Pr!nc3 | D4rk_W1z@rD | Xyr!5h | bL@nk_c0nS0L3 | BL4ck_5h4d0w ]"""+purple+bold+"""
........................................................................................."""+blue+bold+"""
Version"""+red+bold+"""      : """+cyan+bold+"""[ 1.0.1 (Console Based) ]"""+cyan+bold+"""
Date"""+red+bold+"""         : """+blue+bold+"""[ 15/04/2021 | 9:16 AM ]"""+purple+bold+"""
........................................................................................."""+yellow+bold+"""
-----------------------------------------------------------------------------------------------------"""+cyan+bold+"""
••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••"""+lgreen+bold)


for i in networks:
	pwd=subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode('utf-8').split('\n')
	pwd=[b.split(":") [1] [1:-1] for b in pwd  if "Key Content" in b]
	try:
		print ("{:<60} |	 {:<}".format(i, pwd[0]))
	except IndexError:
		print ("{:<60} |	 {:<}".format(i, ""))

print("\n",Bwhite+bold+"------------------------------------------------------------")
print (lgreen+bold+"[*] All Stored Wifi Passwords Are Fucked UP!"+red+bold)
input ("[!] Press Enter to Exit")

