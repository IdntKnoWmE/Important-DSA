#take an array and sort it using merge sort
def mergesort(ans):
    if len(ans)>1:
        mid=len(ans)//2
        #make a recursive call until the final list remains is of length 1
        left=ans[:mid]
        right=ans[mid:]
        left=mergesort(left)
        right=mergesort(right)
    #make a new arr to store sort result
        ans=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                ans.append(left[i])
                i+=1
            else:
                ans.append(right[j])
                j+=1
        print("left",left)
        print("right",right)
        print("ans",ans)
        for m in range(i,len(left)):
            ans.append(left[m])
        for n in range(j,len(right)):
            ans.append(right[n])
        print(ans)
    return ans


#main program
if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(arr)
    print(mergesort(arr))

"""                                                               1 9 5 7 6
                                                                     /   \
                                                                   /       \
                                                                1 9       5 7 6
                                                                / \            /\ 
                                                              /     \         /   \  
                                                            1        9       5     7 6
                                                                                     / \
                                                                                    /    \
                                                                                  7        6



"""




