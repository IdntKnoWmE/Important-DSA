"""basic of finding a number is prime or not is that to loop
to either n-1 or root n which gives the time complexity of
either n or root(n) but for prime even more large we can use
some algo like -->
"""
# Optimized school method
"""As we know that prime are either 6k+1 or 6k-1 so we can
check any number is prime or not using o(root(n)) complexity
even more stabily using increment of 6"""
def optimized_school_method(n):
    if n%2==0 or n%3==0:
        return "No"
    i=5
    while i*i<n:
        if n%i==0 or n%i+2==0:
            return "No"
        i+=6
    return "Yes"


#Femat Method
"""This method says if n is a primme number than,
for every "a", i.e. 1<a<n-1
a^(n-1)=1%m
or

a^(n-1)%n=1
This method return True or False in regarding of the number
but if a number is prime there is a also a chance or wrong
answer since this method uses is an probablastic approach and we know
problitic approach can be improved by more iteration.
Now us do some iteration -->
"""

def pow(n,p,m):
    #modular exponentation
    res=1
    n=n%m
    while p>0:
        if p%2!=0:
            res=(res*n)%m
            p-=1
        n=(n*n)%m
        p=p//2
    return res%m
    
def fermit_method(n,k):
    #here k is number of iteration you want to do
    import random
    if n==1 or n==4:
        return False
    elif n==2 or  n==3:
        return True
    else:
        for i in range(k):
            #generate any random number between 1 and n
            num=random.randint(2,n-2)# choose range so no remainder can be 1.
            #check (num^n-1)%n==1 or not
            if pow(num,n-1,n)!=1:
                return False
    return True
    #Time complexity of this method depends upon your number of iteration k.
"""There is one issue with this number that exixst some composite numbers
where a^(n-1)%n=1 also known as carmichael numbers such as 561=3*11*17.
These numbers are really rare but still they totally effect our answer."""


#Miller-Rabin Method(For more go to cp.algorithm)
"""
Its just like fermit method i.e. a probilistic method but it is preferred more
than fermit method.
The method is:
-> handle base case of n<4 and even number which is false by the way.
-> now consider a "n" number we want to test so we know that n is an odd
number off course and n-1 will be an even number.
This n-1 the even number can be dwritten as product of d*2^r.
where d is an odd number and r is the power of 2.(here d can be 1 also).
we can write a^(n-1)=1%n as a^(d*2^r)-1=0%n
also we can write a^(d*2^r)-1=0%n as,
-->(a^(2^(r−1)d+1) (a^(2^(r+1)d+1)≡0modn

-->(a^(2^(r−1)d+1)(a^(2^(r−2)^d+1)..........(a^d+1)(a^d−1)≡0modn

so to n to be prime n must divide this all numbers which we will generate to
it primality probabilty.




-> Now start your iterations lets take it as k so, a loop untill k is started
In Iteration do:
    --> pick a random number in range of 2,n-2
    -->compute x=pow(a,d,n) here we do modular exponentetaion so  to get
        (a**d)%n.
    -->if x==1 or x==n-1 return True i.e its an prime number.
    -->if last statement doesn't run then run a while loop in which:
        -->find (x*x)%n using modular exp
        -->if x==1 return False
        --> if x==n-1 return True
        -->put d=d*2
        --> Run the while loop untill d != n-1.
   --> At end of loop if anything doesnot become then return False as it may
   not be a prime number.



"""


def Miller_Rabin_bestprimetest(n,k):
    import random
    if n%2==0:
        return False
    if n==2 or n==3:
        return True
    if n<=4:
        return False
    d=n-1
    while d%2==0:
        d=d//2
    #start Iteration
    print("d=",d)
    for _ in range(k):
        p=d
        a=2+random.randint(1,n-4)
        print("a=",a)
        x=pow(a,p,n)#modular exp
        print("1",x)
        if x==1 or x==n-1:
            return True
        while p!=n-1:
            x=(x*x)%n
            p=p*2
            print("2",x)
            if x==1:
                return False
            if x==n-1:
                return True
    return False
    
        



















