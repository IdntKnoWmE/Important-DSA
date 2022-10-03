def combinationSum(a,n,b):
        # code here
        a.sort()
        ans={}
        def leapoffaith(i,b,s,a):  
            if i>=len(a):
                if b==0:
                    if tuple(s) not in ans:
                        ans[tuple(s)]=1
                return
            if b<0:
                return
            if b==0:
                if tuple(s) not in ans:
                    ans[tuple(s)]=1
                return
            leapoffaith(i+1,b,s,a)
            leapoffaith(i+1,b-a[i],s+[a[i]],a)
        s=[]
        i=0
        leapoffaith(i,b,s,a)
        an=[]
        for i in ans:
            an.append(i)
        return an
a=list(map(int,input().split()))
n=len(a)
b=int(input())
print(combinationSum(a,n,b))
