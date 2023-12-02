str1="my name is jowin"
print(str1[4:6])
str2="jowin"
temp=0
for i in range (len(str1)):
    if(str2==str1[i:len(str2)-1]):
        print(str1[i:len(str2)-1])
        temp=i
print(str1[temp:len(str2)-1])