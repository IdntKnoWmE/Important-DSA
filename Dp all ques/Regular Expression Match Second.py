"""Question
mplement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
Some Example:
                    isMatch("aa","a") → 0
                    isMatch("aa","aa") → 1
                    isMatch("aaa","aa") → 0
                    isMatch("aa", "a*") → 1
                    isMatch("aa", ".*") → 1
                    isMatch("ab", ".*") → 1
                    isMatch("aab", "c*a*b") → 1

        Return T or F as 1 or 0.
        """

#Solution
def ismatch(A,B):#A=parent string B=To be matched string
    m=len(A)
    n=len(B)
    dp=[[False for i in range(m+1)]for j in range(n+1)]

    #start
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:#Case for blank space before both string so to solve ques
                if i==0 and j==0:
                    dp[i][j]=True#as blank space == blank space
                elif i==0:
                    pass #as b_space doesn't match with any char
                elif j==0 and B[i-1]=="*":
                    dp[i][j]=dp[i-2][j] #As prec_char+"*" can also be blank_space so check for True cases
            else:
                if B[i-1]=="." or A[j-1]==B[i-1]:
                    dp[i][j]=dp[i-1][j-1]#Check for preceding strings is A[:j-1]==B[:i-1]
                elif B[i-1]=="*":
                    #main case
                    if B[i-2]!=A[j-1] and B[i-2]!=".":#if preceding char is not matching then just check if preceding string for prec+"*"=Blank_space
                        dp[i][j]=dp[i-2][j]

                    elif B[i-2]==A[j-1]:
                        #check if prec char == A[j-1] then check alse precidings strings of A[:j-1]==B[:i-1] with case of considering prec_char+"*" as blank_space
                        dp[i][j]=dp[i-2][j] or dp[i][j-1]

                    elif B[i-2]==".":
                        #same as above as . matches any char
                        dp[i][j]=dp[i-2][j] or dp[i][j-1]
                else:
                    dp[i][j]=False#obvious nothing matches
    return dp[n][m]















                
