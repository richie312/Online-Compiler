def LetterChanges(str): 
  
  newString = ""
  for char in str:
    if char.isalpha():
      if char.lower() == 'z':
        char = 'a'
      else:
        char = chr(ord(char) + 1)
    if char in 'aeiou':
      char = char.upper()
    newString = newString + char

  return newString

with open(r"testcases\letter_changes\letter_changes_input.txt","r") as readfile:
    file = readfile.read()

input_list = file.split('\n')    
output = []
for i in range(len(input_list)):
    output.append(LetterChanges(input_list[i]))
    with open(r"testcases\letter_changes\letter_changes_output.txt","a+") as outfile:
        outfile.write(str(output[i]) + '\n')

