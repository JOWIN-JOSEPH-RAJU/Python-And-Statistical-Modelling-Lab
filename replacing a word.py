string="my name is jowin joseph raju"
str=input("enter the string to replace")
inp=input("the input string")
for i in range (len(string)):
    if(str==string[i:len(str)-1]):
        temp=i
out=string[ :(i-1)]+ inp+ string[i+len(inp)-1:]
print(out)