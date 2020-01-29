def LetterCapitalize(str): 
  words = str.split(" ")
  for i in range(0, len(words)): 
    words[i] = words[i][0].upper() + words[i][1:]
  return " ".join(words)


with open(r"testcases\letter_Capitalise\letter_capitalize_input.txt","r") as readfile:
    file = readfile.read()
input_list = file.split('\n')    
output = []
for i in range(len(input_list)):
    output.append(LetterCapitalize(input_list[i]))
    with open(r"testcases\letter_capitalise\letter_capitalize_output.txt","a+") as outfile:
        outfile.write(str(output[i]) + '\n')
