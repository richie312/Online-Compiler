import sys

for line in sys.stdin:
    txt,nKey = [x for x in line.split()]
    print(caesar_cipher(txt,int(nKey)))
