class node:
      def __init__(self,value=None):
            self.val=value
            self.left=None
            self.right=None
class btree:
      def __init__(self):
            self.root=None
      def add(self,val):
            if self.root==None:
                  self.root=node(val)
            else:
                  self._add(self.root,val)
      def _add(self,root,val):
            if val<root.val:
                  if root.left==None:
                        root.left=node(val)
                        return
                  else:
                        self._add(root.left,val)
            else:
                  if root.right==None:
                        root.right=node(val)
                        return
                  else:
                        self._add(root.right,val)
      def print(self):
            if self.root==None:
                  return
            else:
                  h=0
                  d={}
                  self._print(self.root,h,d)
                  print(d)
      def _print(self,root,h,d):
            if root:
                  if h in d:
                        d[h].append(root.val)
                  else:
                        d[h]=[root.val]
                  self._print(root.left,h+1,d)
                  self._print(root.right,h+1,d)

def filltree(arr,low,high,bi):
      if low<=high:
            mid=(low+high)//2
            bi.add(arr[mid])
            filltree(arr,low,mid-1,bi)
            filltree(arr,mid+1,high,bi)
if __name__=="__main__":
      arr=[1,2,4,5,6,8,10,14,16,20,29,35,36,47,58,69,70]
      low=0
      high=len(arr)-1
      bi=btree()
      filltree(arr,low,high,bi)
      print(arr)
      bi.print()
