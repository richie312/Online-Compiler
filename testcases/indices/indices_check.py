import sys

for line in sys.stdin:   
    X, Y = [int(float(x)) for x in line.split()]
    print(indices(X, Y))
