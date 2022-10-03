"""Dp solution to determine number of attempts you need to
find so to find the critical floor from which egg break when drops.

Solution for this question are basically three.
"""
import sys
import time
# 1. Recursive Solutions with DP.
#n-> Numbers of Eggs
#k-> Numbers of Floors
def rec_egg_drop(n,k):
    start=time.time()

    dp=[[-1 for i in range(n+1)]for j in range(k+1)]
    def rec(n,k):
        if k==1 or k==0:
            return k
        elif n==1:
            return k
        if dp[k][n]!=-1:
            return dp[k][n]
        else:
            m=sys.maxsize
            for i in range(1,k+1):
                #if egg broke from ith floor then reduce egg and travel below ith
                #floor for finding the critical floor.
                a=rec(n-1,i-1)
                
                #if egg doesn't broke then move towards upper floors i.e.
                #check the from the left floors where it would broke.
                b=rec(n,k-i)
                
                #worst case must be choose for optimumising problems as it is
                #based on pure calculation but not on faith

                worst_case=max(a,b)

                #from all worst case choose the best or say minimum worst
                #Case.

                m=min(m,worst_case)
        dp[k][n]=m+1
        return dp[k][n]
    
    ans=rec(n,k)
    end=time.time()
    #for i in dp:
    #    print(i)
    print(end-start)
    return ans


#2. Iterative Solution
def Iter_egg_drop(n,k):
    start=time.time()
    dp=[[-1 for i in range(k+1)]for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            #def base cases
            if j==1:
                dp[i][j]=1
            elif i==1:
                dp[i][j]=j
            else:
                for r in range(j):
                    res=1+max(dp[i-1][r],dp[i][j-r-1])
                    if dp[i][j]==-1:
                        dp[i][j]=res
                    else:
                        dp[i][j]=min(res,dp[i][j])
    end=time.time()
    #for i in dp:
    #    print(i)
    print(end-start)
    return dp[n][k]
                    
                





















        
