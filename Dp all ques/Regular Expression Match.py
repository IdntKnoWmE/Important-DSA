"""Question:
                Implement wildcard pattern matching with support for ‘?’ and ‘*’ for strings A and B.

’?’ : Matches any single character.
‘*’ : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""

def isMatch(A, B):
        #Let A=baaabab and B=ba*a?
        #consider strings as baaabab_ and ba*a?_
        #Now make an dp array of size 1+len(B)*1+len(A) here i choose col as A and row as B.
        
        dp=[[False for i in range(1+len(A))] for j in range(1+len(B))]
        
        """Since blank space we add doesn't match with any alphabet but match with each other
        only so we put dp[len(B)][len(A)]=True ans all as False.
        Now you think * also matches empty space but if we match * as blank then what will
        happen to a? they will be left behind so consider such as False only as string are
        not matching for such case.
        
        """
        #Now we are gonna use down to top approach here as ? can be matched to any preceeding
        #string we have to find that precding string is matching or not.
        
        for i in range(len(B),-1,-1):
            for j in range(len(A),-1,-1):
                if i==len(B) or j==len(A):
                    if i==len(B) and j==len(A):
                        dp[i][j]=True
                    elif j==len(A) and B[i]=="*":
                        dp[i][j]=dp[i+1][j]
                else:
                    if B[i]=="?":
                        dp[i][j]=dp[i+1][j+1]
                #since ? is matched to anything so just check the after string are matched
                #or not of both A & B if we choose ? as A[j].
                
                    
                    elif B[i]=="*":#Special Case
                        #for better time comp
                        dp[i][j]=dp[i+1][j] or dp[i][j+1]
                    
                        #for k in range(j,len(A)+1):
                            #if dp[i+1][k]==True:
                                #dp[i][j]=True
                                #break
                    #Since * can match with blank or any sets of character so we check if any of string
                    #after * in B[i+1:] matches with any A from j to len(A) then we return True
                    
                    elif B[i]==A[j]:
                        dp[i][j]=dp[i+1][j+1]
        return int(dp[0][0])
        for i in dp:
            print(i)
        
    
