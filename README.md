<h1 align="center">SocialBrute</h1>
<p align="center">This is a bruteforce attacker made in Python. Any misuse is beyond my responsibility this is for educational purposes only</p>

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



### NOTE: Removed the final code snippet to prevent `SKIDS` from abusing the tool



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
