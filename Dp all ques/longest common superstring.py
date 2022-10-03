"""QUESTION
Shortest common superstring
Asked in:  
Google
Problem Setter: raghav_aggiwal Problem Tester: dhruvi
Given a set of strings, A of length N.

Return the length of smallest string which has all the strings in the set as substring.



Input Format:

The first and the only argument has an array of strings, A.
Output Format:

Return an integer representing the minimum possible length of the resulting string.
Constraints:

1 <= N <= 18
1 <= A[i] <= 100
Example:

Input 1:
    A = ["aaaa", "aa"]

Output 1:
    4

Explanation 1:
    Shortest string: "aaaa"

Input 2:
    A = ["abcd", "cdef", "fgh", "de"]

Output 2:
    8

Explanation 2:
    Shortest string: "abcdefgh"
    """





def merge(a,b):
    if a==b:
        return a
    l=1
    string1=string2=a+b
    while len(a)-l>=0 and l<=len(b):
        if a[len(a)-l:]==b[:l]:
            string1=a+b[l:]
        l+=1
    l=1
    while len(b)-l>=0 and l<=len(a):
        if b[len(b)-l:]==a[:l]:
            string2=b+a[l:]
        l+=1
    #print("F",string1,string2)
    if len(string1)>=len(string2):
        return string2
    else:
        return string1
def SCS():
    A=list(map(str,input().split()))
    while True:
        if len(A)==1:
            return A[0]
        max_reduce_length=-1#max length of strings reduces from merging strings 
        new_str=""
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                    
                new_merge=merge(A[i],A[j])
                #print(A[i],A[j],new_merge)
                
                #calc how much string length get reduced from merging
                red_length=len(A[i])+len(A[j])-len(new_merge)
                    
                #Now if red_length is grater then max reduced length then save what
                #strings to remove from A and replace them with new_merge string
                
                if red_length>max_reduce_length:
                    index1=A[i]
                    index2=A[j]
                    new_str=new_merge
                    max_reduce_length=red_length
        A.remove(index1)
        A.remove(index2)
        A.append(new_str)
