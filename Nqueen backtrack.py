def nQueen(n):
        # code here
        ans=[]
        arr=[[False for i in range(n+1)]for j in range(n+1)]
        def back(arr,i,d,n):
            if i>=n:
                ans.append(d)
                return
            for j in range(1,n+1):
                if arr[i][j]!=True:
                    arr[i+1][j]=True
                    arr[i+1][j-1]=True
                    arr[i+1][j+1]=True
                    back(arr,i+1,d+[j],n)
                    arr[i+1][j]=False
                    arr[i+1][j-1]=False
                    arr[i+1][j+1]=False
        back(arr,0,[],n)
        return ans
