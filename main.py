## Python bruteforce attacker
## By @unofficialdxnny



### Modules that will be used
import getpass
from datetime import date 
from colorama import Fore, Back, Style
import sys
from time import sleep
import keyboard
import pyautogui as pag
import os
import requests 
import webbrowser
import time


## when the program starts it clears the terminal
os.system('cls')


print("""



  /££££££                      /££           /££ /£££££££                        /££              
 /££__  ££                    |__/          | ££| ££__  ££                      | ££              
| ££  \__/  /££££££   /£££££££ /££  /££££££ | ££| ££  \ ££  /££££££  /££   /££ /££££££    /££££££ 
|  ££££££  /££__  ££ /££_____/| ££ |____  ££| ££| £££££££  /££__  ££| ££  | ££|_  ££_/   /££__  ££
 \____  ££| ££  \ ££| ££      | ££  /£££££££| ££| ££__  ££| ££  \__/| ££  | ££  | ££    | ££££££££
 /££  \ ££| ££  | ££| ££      | ££ /££__  ££| ££| ££  \ ££| ££      | ££  | ££  | ££ /££| ££_____/
|  ££££££/|  ££££££/|  £££££££| ££|  £££££££| ££| £££££££/| ££      |  ££££££/  |  ££££/|  £££££££
 \______/  \______/  \_______/|__/ \_______/|__/|_______/ |__/       \______/    \___/   \_______/
                                                                                                  
                                                                   Author: unofficiadxnny
                                                                       Version: 1.0.0                               
                                                                                                  


""")

## background color is black(0) and the text is green(A)
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 


## new linee
print("\n")

os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 



## Gets system time
today = date.today()

## date format
d2 = today.strftime("%B %d, %Y")


## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type('Program launched successfully today @ ')


## print the final time
print(d2)

os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 

print("\n")
### Final code that does the bruteforcing
url = input("Enter Site login Url: ")

os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 

print("\n")

username = input("Enter the username of victim: ")


os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 


webbrowser.open(url)

os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 

os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 
os.system('color 0b') 
os.system('color 0A') 


## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type('I have just opened your url \n ')


## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type("Press Enter when your mouse is over the username/email area \n")




if keyboard.read_key() == "enter":
  usernamebar = pag.position()
  print(f"Cords captured: {usernamebar}")
  time.sleep(2)

  
  
  
## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type("Press Enter when your mouse is over the password area \n")




if keyboard.read_key() == "enter":
  passwordbar = pag.position()
  print(f"Cords captured: {passwordbar}")
  time.sleep(10)

  
  
## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type("All set lets move to the final step")


# import the time module
import time

# define the countdown func.
def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in which you want to start the program: ")




# function call
countdown(int(t))

 

 ## Gets system time
today = date.today()

## date format
d2d = today.strftime("%B %d, %Y")

## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type('Successfully started today @ ')


## print the final time
print(d2d)
