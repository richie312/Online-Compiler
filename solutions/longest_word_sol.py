def LongestWord(sen):     
    arr = sen.split(" ")
    return max(arr, key=len)




# =============================================================================
# with open(r"testcases\longest_word\longest_word_input.txt","r") as readfile:
#     file = readfile.read()
# 
# input_list = file.split('\n')    
# len(input_list)
# output = []
# for i in range(len(input_list)):
#     output.append(LongestWord(input_list[i]))
#     with open(r"testcases\longest_word\longest_word_output.txt","a+") as outfile:
#         outfile.write(str(output[i]) + '\n')
# 
# =============================================================================
