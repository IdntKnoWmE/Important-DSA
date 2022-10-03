"""GAME THEORY OPTIMIZATION
QUESTION:
Coins in a Line
Problem Description

There are A coins (Assume A is even) in a line.

Two players take turns to take a coin from one of the ends of the line until there are no more coins left.

The player with the larger amount of money wins, Assume that you go first.

Return the maximum amount of money you can win.

NOTE:

You can assume that opponent is clever and plays optimally.


Problem Constraints
1 <= length(A) <= 500

1 <= A[i] <= 105



Input Format
The first and the only argument of input contains an integer array A.



Output Format
Return an integer representing the maximum amount of money you can win.



Example Input
Input 1:

 A = [1, 2, 3, 4]
Input 2:

 A = [5, 4, 8, 10]


Example Output
Output 1:

 6
Output 2:

 15


Example Explanation
Explanation 1:

 You      : Pick 4
 Opponent : Pick 3
 You      : Pick 2
 Opponent : Pick 1


Total money with you : 4 + 2 = 6

Explanation 2:

 You      : Pick 10
 Opponent : Pick 8
 You      : Pick 5
 Opponent : Pick 4


Total money with you : 10 + 5 = 15
"""



def solve(A):
        dp=[[-1 for i in range(len(A))]for j in range(len(A))]
        
        #rec approach
        """
        def rec_app(i,j):
            if i>=j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            a=A[i]+min(rec_app(i+1,j-1),rec_app(i+2,j))
            b=A[j]+min(rec_app(i,j-2),rec_app(i+1,j-1))
            dp[i][j]=max(a,b)
            return dp[i][j]
            
            
        return rec_app(0,len(A)-1)
        """
        
        #top-down approach
        for gap in range(len(A)):
            if gap==0:
                for i in range(len(A)):
                    dp[i][i]=A[i]
            elif gap==1:
                i=0
                while i+gap<len(A):
                    j=i+gap
                    dp[i][j]=max(A[i],A[j])
                    i+=1
            else:
                i=0
                while i+gap<len(A):
                    j=i+gap
                    #just use rec app here only but iteratively
                    a=A[i]+min(dp[i+1][j-1],dp[i+2][j])
                    b=A[j]+min(dp[i+1][j-1],dp[i][j-2])
                    dp[i][j]=max(a,b)
                    i+=1
        for i in dp:
            print(i)
        return dp[0][len(A)-1]
