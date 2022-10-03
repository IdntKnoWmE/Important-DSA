
def merge(arr, l, m, r): 
    # code here
    if r==l+1:
        if arr[l]>arr[r]:
            arr[l],arr[r]=arr[r],arr[l]
        print(arr,l,m,r)
        return
    print(arr,l,m,r)
    a=[]
    i=l
    j=m+1
    while i<=m and j<r+1:
        if arr[i]<arr[j]:
            a.append(arr[i])
            i+=1
        else:
            a.append(arr[j])
            j+=1
    #print(i,j)
    while i<=m:
        a.append(arr[i])
        i+=1
    while j<r+1:
        a.append(arr[j])
        j+=1
    k=0
    for i in range(l,r+1):
        arr[i]=a[k]
        k+=1
    print(arr)




#{ 
#  Driver Code Starts
#Initial Template for Python 3

def mergeSort (arr, l, r):
    if l < r:
        m = l + (r - l)//2
        
        mergeSort (arr, l, m)
        mergeSort (arr, m+1, r)
        merge (arr, l, m, r)

if __name__ == "__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    mergeSort(arr, 0, n-1)
    for i in range(n):
        print(arr[i],end=" ")
    print()
# } Driver Code Ends
