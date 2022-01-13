## this is just my test file  if you want to test some code changes try them here than create a pull request with the changes

with open("passwords.txt", 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        print(line)
