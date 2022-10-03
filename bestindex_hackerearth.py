import math
n=int(input())
arr=list(map(int,input().split()))
temp=[]
s=0
ma=0
for i in arr:
    s=s+i
    temp.append(s)
for i in range(n):
    t=int((math.sqrt(1+8*(n - i))-1)//2)
    #print(t)
    ma=max(ma,temp[-1+i+t*(t+1)//2] - temp[i-1])
    #ma=max(temp[t]-(temp[i]-arr[i]),ma)
print(ma)
