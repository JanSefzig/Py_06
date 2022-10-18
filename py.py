def pattern(n):
 
    for i in n:
        print("|", end = "")
        print("*" * int(i))
n = "41325"
pattern(n)

num = 1
guess = None

while guess != num:
    guess = input("hádej: ")
    guess = int(guess)

    if guess == num:
        print("uhádl jsi!")
        break
    else:
        print("zkus to znovu!")

import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")