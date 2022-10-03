"""
Find the answer of .
   ((A**B)/C)%M

Input:
The only line of input consists of four integers A,B,C and M. The input always has C and M such that .

Output:
Print the answer as asked in the problem statement.

Constraints:
             1<=A,B,C,M<=10**9
             GCD(C,M)=1 //it is compulsory for inv modular
             
."""
#                         SOLUTION
x,y=0,0
#modinv algorithm(Recursive solution)
def modinv(c,d):
    global x,y
    if c==0:
        x=1
        y=0
        #print(c,d,x,y,"y")
    else:
        modinv(d%c,c)
        #print(c,d,x,y,"y")
        temp=x
        x=y
        y=temp-(d//c)*y
        #print(c,d,x,y,"y")

import math
a,b,c,d=list(map(int,input().split()))
result=1
# power exponential algo for calculating higher power of "n" in logn time when used with modular func it becomes modular power exponentila algo
while True:
    if b==1:
        result=(result*a)%d
        break
    elif b%2==0:
        a=(a*a)%d
        b=b//2
    else:
        result=(result*a)%d
        a=(a*a)%d
        b=b//2
modinv(c,d)
res=(y%d+d)%d
#print(res)
print((res*result)%d)


