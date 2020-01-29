
import numpy as np
def find_missing_number(array,n_elem):
    usual_array = (np.arange(0,n_elem)+1).tolist()
    missing_elem = []
    for elem in usual_array:
        if elem not in array:
            missing_elem.append(elem)
    return missing_elem        
