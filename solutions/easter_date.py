def easter_date(y):
    g = y%19 + 1
    s = (y-1600)//100 - (y-1600)//400 
    l = (y-1400)//100 * 8 // 25
    p = (3 - (11*g) + s - l)%30
    
    if p == 29 or (p == 28 and g > 11):
        p -= 1

    d = (y + (y//4) - (y//100) + (y//400))%7
    x = ((8-d)%7 - ((3+p)%7)-1)%7 + 1

    if p + x < 11:
        easter = 'March {}'.format(round(p + x + 21))
    else:
        easter = 'April {}'.format(round(p + x - 10))
    
    return easter


if __name__ == '__main__':
    easterDay1 = easter_date(1947)
    easterDay2 = easter_date(1975)
    print(easterDay1)
    print(easterDay2)