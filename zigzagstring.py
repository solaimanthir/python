def myfunc(mystr):
    newstr = ''
    idx = 1
    
    for c in mystr:
        if idx%2 == 0:
            newstr = newstr + c.upper()
        else:
            newstr = newstr + c.lower()
        idx = idx + 1
        
    return newstr
