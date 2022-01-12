## this is just my test file 


with open("passwords.txt", 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        print(line)