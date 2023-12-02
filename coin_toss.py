import random as rand
import math
no_throws=8
no_head=0
list=[]
for i in range (no_throws):
    list.append(rand.choice(["head","tail"]))

print(list)

for i in list:
    if(i=="head"):
        no_head=no_head+1
no_tail=no_throws-no_head
prob=math.comb(8,no_head)*0.5**no_head*0.5**no_tail
print("probablity:",prob)