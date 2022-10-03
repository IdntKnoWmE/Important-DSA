def multiply_mat(a,b):
    x=a[0][0]*b[0][0]+a[0][1]*b[1][0]

    y=a[0][0]*b[0][1]+a[0][1]*b[1][1]

    z=a[1][0]*b[0][0]+a[1][1]*b[1][0]

    w=a[1][0]*b[0][1]+a[1][1]*b[1][1]

    return [[x,y],[z,w]]





def calc_pow(mat,A):
    m=[[1,1],[1,0]]
    if A==1:
        return m
    if A%2==0:
        f=calc_pow(mat,A//2)
        return multiply_mat(f,f)
    if A%2!=0:
        f=calc_pow(mat,A-1)
        return multiply_mat(f,m)


def fibnacci(A):
    if A==0:
        return 0
    if A==1:
        return 1
    mat=[[1,1],[1,0]]
    return calc_pow(mat,A-1)
    print(mat)
        
