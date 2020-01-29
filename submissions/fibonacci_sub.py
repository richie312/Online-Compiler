
def fib(n):  
   if n <= 1:  
       return n  
   else:  
       return fib(n-1) + fib(n-2)
def fib_seq(n):
    seq = []
    for i in range(n):
        seq.append(fib(i))
    return seq