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