
#majority element using o(n) time and o(1) space
def majorityElement():
        A=list(map(int,input().split()))
        maj=A[0]
        c=1
        for i in range(1,len(A)):
            if A[i]!=maj:
                c-=1
            else:
                c+=1
            if c<=0:
                maj=A[i]
                c=1
        return maj
