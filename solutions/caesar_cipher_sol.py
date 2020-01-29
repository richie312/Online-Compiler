import numpy as np
def find_missing_number(array_num):
    usual_array = (np.arange(0,array_len)+1).tolist()
    missing_elem = []
    for elem in usual_array:
        if elem not in array:
            missing_elem.append(elem)
    return missing_elem        
            










find_missing_number(array)