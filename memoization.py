def fib(n):
   m={1:1,2:1}
   def memo(n,m):
       if n in m:
           return m[n]
       ans=memo(n-1,m)+memo(n-2,m)
       m[n]=ans
       return ans
   return memo(n,m)    

    
print(fib(8)) 
