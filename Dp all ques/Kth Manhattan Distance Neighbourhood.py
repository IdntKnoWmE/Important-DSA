"""QUESTION
Kth Manhattan Distance Neighbourhood
Asked in:  
Liv.ai
Problem Setter: ishubansal Problem Tester: raghav_aggiwal
Given a matrix M of size nxm and an integer K, find the maximum element in the K manhattan distance neighbourhood for all elements in nxm matrix.
In other words, for every element M[i][j] find the maximum element M[p][q] such that abs(i-p)+abs(j-q) <= K.

Note: Expected time complexity is O(N*N*K)

Constraints:

1 <= n <= 300
1 <= m <= 300
1 <= K <= 300
0 <= M[i][j] <= 1000
Example:

Input:
M  = [[1,2,4],[4,5,8]] , K = 2

Output:
ans = [[5,8,8],[8,8,8]]

"""




def solve(B, A):
        if B==0:
            return A
        dp=[[0 for i in range(len(A[0]))] for j in range(len(A))]
        r=len(A)
        c=len(A[0])
        for k in range(B):
            for i in range(r):
                for j in range(c):
                    #take a cell, check out only its left, right, top, bottom, and itself. Pick the 
                    #max of them all and replace the said current element in a new matrix. Do this
                    #for all elements, and then replace this entire matrix with the newly calculated one
                    #and repeat for K-1 times.
    
                    #diagonal elements are not considered manhattan for an ele. U can only traverse 90 deg
                    #in any direction at each iteration
                    
                    left=A[i][j-1] if j-1>=0 else 0
                    
                    right=A[i][j+1] if j+1<c else 0
                    
                    up=A[i-1][j] if i-1>=0 else 0
                    
                    down=A[i+1][j] if i+1<r else 0
                    
                    dp[i][j]=max(up,down,A[i][j],right,left)
            A,dp=dp,A
        return A
