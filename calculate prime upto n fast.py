def prime(n):
    n-=1
    if n < 2:
        return 0
    r = int(n ** 0.5)
    V = [n//d for d in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    print(V)
            
    S = {v: v - 1 for v in V}
    print(S)
    for p in range(2, r + 1):
        print("p=",p)
        if S[p] == S[p - 1]:
            print(S[p],S[p-1],"cont")
            continue
        p2 = p * p
        print("p=",p,"p2=",p2)
        print("S[p]=",S[p],"S[p-1]=",S[p-1])
        sp_1 = S[p - 1]
        for v in V:
            print("v=",v)
            if v < p2:
                break
            print("s[v]=",S[v],"v//p=",v//p,"s[v/p]=",S[v//p],"sp_1=",sp_1,"do")
            S[v] -= S[v//p] - sp_1
            print("s[v]=",S[v],"v//p=",v//p,"s[v/p]=",S[v//p],"sp_1=",sp_1,"after")
        print(S)
    return S[n]

if __name__=="__main__":
    n=int(input())
    print(prime(n))
