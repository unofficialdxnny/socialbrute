
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

## the main import lol
import requests 


## when the program starts it clears the terminal
os.system('cls')




## banner (need a better one)
print("""


                                                                                                                                                                                
   d888888o.       ,o888888o.         ,o888888o.     8 8888          .8.          8 8888         8 888888888o   8 888888888o.  8 8888      88 8888888 8888888888 8 8888888888   
 .`8888:' `88.  . 8888     `88.      8888     `88.   8 8888         .888.         8 8888         8 8888    `88. 8 8888    `88. 8 8888      88       8 8888       8 8888         
 8.`8888.   Y8 ,8 8888       `8b  ,8 8888       `8.  8 8888        :88888.        8 8888         8 8888     `88 8 8888     `88 8 8888      88       8 8888       8 8888         
 `8.`8888.     88 8888        `8b 88 8888            8 8888       . `88888.       8 8888         8 8888     ,88 8 8888     ,88 8 8888      88       8 8888       8 8888         
  `8.`8888.    88 8888         88 88 8888            8 8888      .8. `88888.      8 8888         8 8888.   ,88' 8 8888.   ,88' 8 8888      88       8 8888       8 888888888888 
   `8.`8888.   88 8888         88 88 8888            8 8888     .8`8. `88888.     8 8888         8 8888888888   8 888888888P'  8 8888      88       8 8888       8 8888         
    `8.`8888.  88 8888        ,8P 88 8888            8 8888    .8' `8. `88888.    8 8888         8 8888    `88. 8 8888`8b      8 8888      88       8 8888       8 8888         
8b   `8.`8888. `8 8888       ,8P  `8 8888       .8'  8 8888   .8'   `8. `88888.   8 8888         8 8888      88 8 8888 `8b.    ` 8888     ,8P       8 8888       8 8888         
`8b.  ;8.`8888  ` 8888     ,88'      8888     ,88'   8 8888  .888888888. `88888.  8 8888         8 8888    ,88' 8 8888   `8b.    8888   ,d8P        8 8888       8 8888         
 `Y8888P ,88P'     `8888888P'         `8888888P'     8 8888 .8'       `8. `88888. 8 888888888888 8 888888888P   8 8888     `88.   `Y88888P'         8 8888       8 888888888888 


""")


## background color is black(0) and the text is green(A)
os.system('color 0A') 



##TypeWriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
type("Welcome To SocialBrute \n")

## new linee
print("\n")



## Gets system time
today = date.today()

## date format
d2 = today.strftime("%B %d, %Y")



## typewriter effect
def type(text):
  words = text
  for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
type('Bruteforce started today at \n')

## 2 new lines 
print("\n")
print("\n")

## print the final time
print(d2)


