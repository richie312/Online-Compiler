# -*- coding: utf-8 -*-
  
def sortLexo(my_string): 
    words_list = my_string.split() 
    special_chars = "~!@#$%^&*()-_+={}[]:;'<>?/,.|`"
    clean_words = []
    for word in words_list:
        for char in word:
            if char in special_chars:
                word = word.replace(char,"")
            else:
                None
        clean_words.append(word)
    clean_words.sort()
    return clean_words

# =============================================================================
# string = "machine Learning is an application of artificial intelligence (ai) that provides systems the ability to automatically learn and improve from Experience without being explicitly programmed"
# 
# with open(r"testcases\lexographical\lexographical_order_input.txt","r") as readfile:
#     file = readfile.read()
# 
# input_list = file.split('\n')    
# 
# with open(r"testcases\lexographical\lexographical_order_output.txt","a+") as outfile:
#     outfile.write(str(sortLexo(input_list[0])) + '\n')
# 
# =============================================================================
