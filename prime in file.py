file=open("list.c", 'w')
n=int(input("enter the number digits"))
for i in range(n):
    dig = int(input("enter the  digits"))
    file.write(str(dig)+"\n")
file.close

file=open("list.c","r")
prime=open("prime.c","w")
comp=open("comp.c","w")

for j in file:
    flag=0

    for i in range(2, int((j))):
        if (int(j)  % i == 0):
            flag = 1
            break
    if (flag == 1):
        comp.write(j+"\n")
    else:
        prime.write(j + "\n")


