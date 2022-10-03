def micsandjury (N, M, teams):
        l=1
        r=max(teams)
        fans=1
        while l<=r:
            mid = (l+r)//2
            groups=0
            print(mid)
            for i in range(M):
                if teams[i]%mid!=0:
                    groups = groups+(teams[i]//mid) + 1
                else:
                    groups = groups+(teams[i]//mid)
                print(groups,teams[i]//mid,teams[i]%mid)
            
            if(groups>N):
                l = mid+1
            else:
                fans=mid
                r=mid-1
        
        return fans
