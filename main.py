
import getpass
from datetime import date 
from colorama import Fore, Back, Style
import sys
from time import sleep
import keyboard
import pyautogui as pag
import os


os.system('cls')





os.system('color 0A') 



def type(text):
  words = text
  for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
type("Welcome To SocialBrute \n")

print("\n")



today = date.today()

d2 = today.strftime("%B %d, %Y")



def type(text):
  words = text
  for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
type('Bruteforce started today at \n')

print("\n")
print("\n")

print(d2)

