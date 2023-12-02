import math
n=8 #no of experiments
p=0.5 #favourable number of outcomes
q=0.5
x=4 #number of times head is coming
prob=math.comb(n,x)*p**x*q**(n-x)
print("probablity:",prob)