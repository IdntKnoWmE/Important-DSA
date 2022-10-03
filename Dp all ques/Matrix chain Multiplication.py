#solution 1 using recursion and modify array technique
def mcm1(n, arr):
        # code here
        mat=[]
        for i in range(1,n):
            mat.append([arr[i-1],arr[i]])
        def rec(mat,s,ans):
            if len(mat)==2:
                ans[0]=min(ans[0],s+mat[0][1]*mat[0][0]*mat[1][1])
                return
            for i in range(1,len(mat)):
                print(mat)
                tem=mat[i-1][0]*mat[i][0]*mat[i][1]
                d=mat[:i-1]+[[mat[i-1][0],mat[i][1]]]+mat[i+1:]
                rec(d,s+tem,ans)
        ans=[float("inf")]
        rec(mat,0,ans)
        return ans[0]

#using recursive and indexing approach
def mcm2(n,arr):
    def rec(arr,i,j):
        if i>=j:
            return 0 #Base case as it denotes same matrix
        tem=float("inf")#for calc min number of multiplication
        for k in range(i,j):
            temp=rec(arr,i,k)+rec(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
            tem=min(tem,temp)
        return tem
    return rec(arr,1,n-1)

#using rec and memozitation
def mcm3(n, arr):
        # code here
        dp=[[-1 for i in range(n)]for j in range(n)]
        def rec(mat,i,j):
            if i>=j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=float("inf")
            for k in range(i,j):
                temp=rec(mat,i,k)+rec(mat,k+1,j)+arr[i-1]*arr[k]*arr[j]
                dp[i][j]=min(dp[i][j],temp)
            return dp[i][j]
                
        return rec(arr,1,n-1)


#using jump and dp top down approach
def mcm4(n,arr):
    dp=[[0 for i in range(n-1)]for j in range(n-1)]
    
    for valid_jump in range(1,n-1):
        for i in range(n-valid_jump-1):
            j=i+valid_jump

            tem=float("inf")#similarly for calc min number of multiplication
            for k in range(i,j):
                #here i had use 0 based indexing for dividing matrix
                temp=dp[i][k]+dp[k+1][j]+arr[i]*arr[k+1]*arr[j+1]
                tem=min(temp,tem)

            dp[i][j]=tem
    return dp[0][n-2]
                

















            

