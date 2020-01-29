# -*- coding: utf-8 -*-
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
       
# =============================================================================
# with open(r"testcases\fibonacci\fibonacci_input.txt","r") as readfile:
#     file = readfile.read()
# input_list = file.split('\n')    
# output = []
# for i in range(len(input_list)):
#     output.append(fib_seq(int(float(input_list[i]))))
#     with open(r"testcases\fibonacci\fibonacci_output.txt","a+") as outfile:
#         outfile.write(str(output[i]) + '\n')
# 
# =============================================================================


