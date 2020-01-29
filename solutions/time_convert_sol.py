import math
def TimeConvert(num): 
  hours = int(math.floor(num / 60))
  minutes = num % 60
  return str(hours) + ':' + str(minutes);



with open(r"testcases\time_convert\time_convert_input.txt","r") as readfile:
    file = readfile.read()
input_list = file.split('\n')    
output = []
for i in range(len(input_list)):
    output.append(TimeConvert(int(float(input_list[i]))))
    with open(r"testcases\time_convert\time_convert_output.txt","a+") as outfile:
        outfile.write(str(output[i]) + '\n')
