ma=0
def rec(arr,s,i,j):
  print(s)
  global ma
  if i+1==j or i>len(arr)//2 or j<2:
    ma=max(ma,s)
    return
  rec(arr,s+(arr[j]*arr[i]),i+1,j-1)
  rec(arr,s,i+1,j)
  rec(arr,s,i,j-1)
  rec(arr,s,i+1,j-1)

n=int(input())
arr=list(map(int,input().split()))
s=0
i=0
j=n-1
rec(arr,s,i,j)
print(ma)
