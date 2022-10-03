def matrix_multiply(x,y):
    n=len(x)
    temp=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j]+=x[i][k]*y[k][j]
    return temp

def identity_matrix(n):
    val=[]
    for i in range(n):
        t=[]
        for j in range(n):
            if i==j:
                t.append(1)
            else:
                t.append(0)
        val.append(t)
    return val
    
def matrix_exponentation_iterative(x,n):
    if n==0:
        return 0
    if n==1:
        return x
    val=identity_matrix(n)
    while n>0:
        if n%2!=0:
            val=matrix_multiply(x,val)
            n-=1
        n=n//2
        if n>0:
            x=matrix_multiply(x,x)
    return val
def matrix_exp_rec(x,n):
    if n==0:
        return identity_matrix(len(x))
    if n==1:
        return x
    if n%2!=0:
        return matrix_multiply(x,matrix_exp_rec(matrix_multiply(x,x),n-1//2))
    else:
        return matrix_exp_rec(matrix_multiply(x,x),n//2)










    
