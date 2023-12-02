import re
e=input("enter the email")
pat="[a-zA-Z0-9-_]+@[a-zA-Z0_9]+.[a-z]{1,3}"
if(re.match(pat,e)):
    print("email is valid")
else:
    print("email is not valid")
