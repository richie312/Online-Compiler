# -*- coding: utf-8 -*-

from itertools import groupby

def solution(N):
    b = "{0:b}".format(N)
    return max(len(list(v)) for k, v in groupby(b.strip("0")) if k == "0")



# =============================================================================
# with open(r"testcases\binary_gap\binary_gap_input.txt","r") as readfile:
#     file = readfile.read()
# input_list = file.split('\n')    
# output = []
# for i in range(len(input_list)):
#     output.append(solution(int(input_list[i])))
#     with open(r"testcases\binary_gap\binary_gap_output.txt","a+") as outfile:
#         outfile.write(str(output[i]) + '\n')
# 
# =============================================================================
