from itertools import groupby

def solution(N):
    b = "{0:b}".format(N)
    return max(len(list(v)) for k, v in groupby(b.strip("0")) if k == "0")
