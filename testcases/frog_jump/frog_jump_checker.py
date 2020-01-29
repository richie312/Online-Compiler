
import sys

for line in sys.stdin:
    X, Y, D = [int(x) for x in line.split()]
    print(frog_jump(X,Y,D))
