

import sys

for line in sys.stdin:
    array,n_element = [eval(x) for x in line.split()]
    missingNumbers(array[0],int(n_element))

