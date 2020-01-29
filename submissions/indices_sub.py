import sys # import to have access to the standard input stream

def indices(a,b):
	c = a**b
	return c
	
for line in sys.stdin: # process input line by line
	a, b = [int(x) for x in line.split()] # split values in the line and cast them to "int" type
	print(indices(a,b)) # print calculated value  
