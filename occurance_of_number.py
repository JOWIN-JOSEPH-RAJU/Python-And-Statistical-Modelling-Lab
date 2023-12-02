list=[0,0,0,0,0,0,0,0,0,0,0]

x=int(input("enter the number of elements in the list"))
for i in range (0,x):
    a= int(input("enter the element"))
    list[i]=a
count=0
b=int(input("enter the number"))
for i in range (x):
    if(b==list[i]):
        count=count+1

print(b, "is present",count,"times")
