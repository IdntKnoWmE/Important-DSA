def longestpalindrome(s):
    dp=[[0 for i in range(len(s))]for j in range(len(s))]
    ans=[0,0]
    maxlength=0
    for k in range(0,len(s)):
        i=0
        while i+k<len(s):
            if k==1 or k==0:
                dp[i][i+k]=1
            else:
                if s[i]==s[i+k] and dp[i+1][i+k-1]==1:
                    dp[i][i+k]=1
                    if k+1>maxlength:
                        ans=[i,i+k+1]
                        maxlength=k+1
            i+=1
    print(*dp,sep="\n")
    print(s[ans[0]:ans[1]])
"""In this program we use dp for solving .
Consider a string "s" then we make a dp array of len(s)*len(s).
Now we dp such that row belongs to starting and columns belongs
to ending of substring.
Now for dp[i][j] we fill it such that if string[i:j] is palindrome we
fill dp[i][j]=1 or else we fill it as dp[i][j]=0.
Now the steps:
-->first we define a loop which states the size of string we considering
for checking that it is palindrome or not.
-->Then we fill the size of string 1 and 2 as palindrome in dp as
these size are always palindrome. (dp[i][i]=1 and dp[i][i+1]=1)
-->Now to fill other we consider if string[i:j] is an palindrome then
string[i+1:j-1] is also palindrome.
-->So,we consider if s[i]==s[j or i+k] and dp[i+1][j-1] is 1 then
our string[i:j] is palindrome and dp[i][i+k or j]=1.
"""
