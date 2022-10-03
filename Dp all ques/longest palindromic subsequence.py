#Here we have to find longest subsequence of substring for which it is palindrome.
dp={}
import time
def use_recursion(s):
    i=0
    j=len(s)-1
    #using dictionary for storing already calls indexes will result in more tiom so use Two dimensional list.
    # To confirm for a same string dictionary takes 0.002991914749145508 seconds and Two-D array takes 0.001992464065551758 seconds
    # i.e. half of it.
    dp=[[0 for i in range(len(s))]for j in range(len(s))]
    def rec_dp(i,j,s):
        if i==j:
            return 1
        if s[i]==s[j] and i+1==j:
            return 2
        if dp[i][j]!=0:
            return dp[i][j]
        if s[i]==s[j]:
            dp[i][j]=rec_dp(i+1,j-1,s)+2
            return dp[i][j]
        dp[i][j]=max(rec_dp(i+1,j,s),rec_dp(i,j-1,s))
        return dp[i][j]
    start=time.time()
    call_ans=rec_dp(i,j,s)
    end=time.time()
    return (end-start,call_ans)
        
"""
#lets do table dp that is non-recursive dp solution.
def use_table_dp(s):
    dp=[[0 for i in range(len(s))]for j in range(len(s))]

    #bbabcbcab
      0 1 2 3 4 5 6 7 8
    0 1 2 2
    1 0 1 0 
    2 0 0 1 0
    3 0 0 0 1 0
    4 0 0 0 0 1 0
    5 0 0 0 0 0 1 0
    6 0 0 0 0 0 0 1 0
    7 0 0 0 0 0 0 0 1 0
    8 0 0 0 0 0 0 0 0 1 0



"""








