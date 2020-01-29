

import sys

for line in sys.stdin:
    mat = eval(line)
    print(rotateMatrix(mat))