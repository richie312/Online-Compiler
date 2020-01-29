def frog_jump(X,Y,D):
    if (Y-X)%D == 0:
        n = ((Y-X)-(Y-X)%D)/D
    else:
        n = (((Y-X)-(Y-X)%D)/D) + 1
    return n    


