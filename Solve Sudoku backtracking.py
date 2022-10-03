def SolveSudoku(grid):
    '''
    :param grid : given 9*9 grid of unsolved soduko
    
    '''
    def rec(grid,i,j):
        if i>=len(grid):
            return True
        if grid[i][j]!=0:
            if j+1<len(grid):
                return rec(grid,i,j+1)
            else:
                return rec(grid,i+1,0)
        m=[0 for k in range(10)]
        for k in range(9):
            m[grid[k][j]]=1
            m[grid[i][k]]=1
        x=i//3
        y=j//3
        for k in range(x*3,(x+1)*3):
            for n in range(y*3,(y+1)*3):
                m[grid[k][n]]=1
        c=0
        for k in range(1,10):
            if m[k]==1:
                c+=1
        if c==9:
            return False
        for k in range(1,10):
            if m[k]!=1:
                grid[i][j]=k
                if j+1<10:
                    d=rec(grid,i,j+1)
                else:
                    d=rec(grid,i+1,0)
                if d==True:
                    return True
                else:
                    grid[i][j]=0
                
        return True
    ans=rec(grid,0,0)
    return ans
