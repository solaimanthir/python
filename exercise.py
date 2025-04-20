#reverse word list
def revWords(z_inStr):
    word_list = z_inStr.split()
    rev_word_list = word_list[::-1]

    #construct a string from the list with '-' character between words
    return '-'.join(rev_word_list)

revWords('this is a test!')

def checkInRangeOf50Or500(num):
    return (abs(50-num) <= 10) or (abs(500-num) <= 10)
print(checkInRangeOf50Or500(43))
print(checkInRangeOf50Or500(503))
print(checkInRangeOf50Or500(100))
