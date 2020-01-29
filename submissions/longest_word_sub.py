def LongestWord(sen):     
    arr = sen.split(" ")
    return max(arr, key=len)
