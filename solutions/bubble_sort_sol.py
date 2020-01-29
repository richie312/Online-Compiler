def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# =============================================================================
# with open(r"testcases\bubbleSort\bubbleSort_input.txt","r") as readfile:
#     file = readfile.read()
# input_list = file.split('\n')    
# array = [eval(x) for x in input_list]
# output = []
# for i in range(len(array)):
#     output.append(bubbleSort(array[i]))
#     with open(r"testcases\bubbleSort\bubbleSort_output.txt","a+") as outfile:
#         outfile.write(str(output[i]) + '\n')
# =============================================================================

