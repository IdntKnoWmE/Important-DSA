class BIT:
    def __init__(self,arr):
        self.array=[0 for i in range(len(arr)+1)]
        print(self.array)
        for i in range(len(arr)):
            k=i+1
            while k<=len(arr):
                self.array[k]+=arr[i]
                k=k+(k&(-k))
arr=[1,2,4,7,8,9,6,5,4,-5,6,-19]
binind=BIT(arr)
print(binind.array)
