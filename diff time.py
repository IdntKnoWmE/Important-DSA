def recdate():
    d=[2,4,5,9,5,9]
    from collections import deque
    q=deque()
    vis=[0 for i in range(10)]
    q.append([vis,[]])
    while len(q)>0:
        v,temp=q.popleft()
        t=len(temp)
        if t==6:
            print(temp)
            continue
        for i in range(t,6):
            for j in range(d[i]+1):
                if v[j]!=1:
                    v[j]=1
                    temp.append(j)
                    q.append([v,temp])
                    v[j]=0
                    temp.pop()
