import numpy as np
def find_missing_number(array,n_elem):
    usual_array = (np.arange(0,n_elem)+1).tolist()
    missing_elem = []
    for elem in usual_array:
        if elem not in array:
            missing_elem.append(elem)
    return missing_elem        

# =============================================================================
# with open(r"testcases\missing_number\missing_number_input.txt","r") as readfile:
#     file = readfile.read()
# input_list = file.split('\n')    
# output = []
# for i in range(len(input_list)):
#     array,n_element = [eval(x) for x in input_list[i].split()]
#     output.append(find_missing_number(array,n_element))
#     with open(r"testcases\missing_number\missing_number_output.txt","a+") as outfile:
#         outfile.write(str(output[i]) + '\n')
# 
# =============================================================================
            









find_missing_number(array)