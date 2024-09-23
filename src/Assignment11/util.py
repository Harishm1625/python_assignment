
import re

def validation():

    n=int(input("Enter number of mail : "))

    email=[input("Enter : ") for _ in range(n)]

    valid_mail=[]

    for i in email:
        pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'

        if re.match(pattern,i):
            valid_mail.append(i)

    print(valid_mail)


validation()