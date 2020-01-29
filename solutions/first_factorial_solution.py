def FirstFactorial(num): 
    if num <=1:
        return 1
    else:
        return num * FirstFactorial(num - 1)
    
with open(r"testcases\first_factorial\first_factorial_input.txt","r") as readfile:
    file = readfile.read()
input_list = file.split('\n')    
output = []
for i in range(len(input_list)):
    output.append(FirstFactorial(int(float(input_list[i]))))
    with open(r"testcases\first_factorial\first_factorial_output.txt","a+") as outfile:
        outfile.write(str(output[i]) + '\n')
