"""QUESTION
Min Jumps Array
Asked in:  
Amazon
Ebay
Google
Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Return the minimum number of jumps required to reach the last index.

If it is not possible to reach the last index, return -1.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer, representing the answer as described in the problem statement.
"""


#SOLUTION

def min_jump():
        A=list(map(int,input().split()))
        #dp=[0 for i in range(len(A))]
        if A[0]==0:
            if len(A)==1:
                return 0
            return -1
        max_index=1
        for i in range(len(A)):
            if i==0:
                #Base case for 0 index
                max_index=max(max_index,i+A[i])#calculate max jump from index 0
                
                #Assign steps to reach max_jump from i 
                steps_to_reach_maxindex=A[i]
                
                #jumps to reach max index
                jumps_to_reach_maxindex=1
                
                
            elif i==len(A)-1:#return number of jumps when i reaches end
                return jumps_to_reach_maxindex
            else:
                if i>max_index:#It means a bunch of zero jump has come in between so reach to end is impossible
                    return -1
                #update max index
                max_index=max(A[i]+i,max_index)
                
                #update steps to reach max index as steps or dist dec with inc of i
                steps_to_reach_maxindex-=1
                
                #If steps reaches to zero that means max index has been approach now if there is
                #an another max index then steps to reach must be calc
                if steps_to_reach_maxindex==0:
                    
                    jumps_to_reach_maxindex+=1
                    
                    steps_to_reach_maxindex=max_index-i
            
