def solve(nums,target):
      nums.sort()
      L, N, S, M = len(nums), {j:i for i,j in enumerate(nums)}, set(), nums[-1]
      print(nums)
      print(L,N,S,M)
      for i in range(L-3):
            a=nums[i]
            print(a,M,a+3*M)
            if a+3*M<target:
                  continue
            if 4*a>target:
                  break
            print("2..",a,M)
            for j in range(i+1,L-2):
                  b=nums[j]
                  if a+b+2*M<target:
                        continue
                  if a+3*b>target:
                        break
                  for k in range(j+1,L-1):
                        c=nums[k]
                        d=target-(a+b+c)
                        if d>M:
                              continue
                        if d<c:
                              break
                        if d in N and N[d]>k:
                              S.add((a,b,c,d))
      print(S)

nums=[1,0,0,1,2,5,3,1,2,4,7,8,9,-8,0,-1,0,-2,2]
target=0
solve(nums,target)
