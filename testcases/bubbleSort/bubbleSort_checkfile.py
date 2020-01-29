
import sys

for line in sys.stdin:
    arr = eval(line)
    print(bubbleSort(arr))