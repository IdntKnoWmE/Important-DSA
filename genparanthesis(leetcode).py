
#Here question is simple that you have find n number of balanced paranthesis
if __name__=="__main__":
      n=int(input())
      ans=[]
      #herebacktrack is used which uses Depth first search
      def backtrack(s, left, right):
            print(s,left,right)
            if len(s) == 2 * n:
                  ans.append(s)
                  return
            if left < n:
                  backtrack(s + '(', left + 1, right)
            if right < left:
                  backtrack(s + ')', left, right = right + 1)
            
            
      backtrack(s = '', left = 0, right = 0)
      print(ans)
