def mergesorthighspacecomp(A):
      if len(A)<2:
            return A
      mid=len(A)//2
      left=mergesorthighspacecomp(A[:mid])
      right=mergesorthighspacecomp(A[mid:])

      i=j=0
      res=[]
      while len(res)<len(A):
            if j>=len(right) or (i<len(left) and left[i]<right[j]):
                  res.append(left[i])
                  i+=1
            elif j<len(right):
                  res.append(right[j])
                  j+=1
      return res

def mergeit(A,res,start,end):
      if end-start<2:
            return
      mid=(start+end)//2
      mergeit(res,A,start,mid)
      mergeit(res,A,mid,end)
      i=start
      j=mid
      idx=start
      print(i,j,end)
      while idx<end:
            if j>=end or (i<mid and A[i]<A[j]):
                  res[idx]=A[i]
                  i+=1
            else:
                  res[idx]=A[j]
                  j+=1
            idx+=1
            print(A,res,sep="or")
      

def mergesortwithlinearcomp(A):
      res=A[:]
      mergeit(A,res,0,len(A))
      print(res,A)

