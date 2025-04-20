#Write a function that capitalizes the given positions in a string
def capitalizeTwoLetters(pos1, pos2, inStr):
    lenStr = len(inStr)
    
    if lenStr < 1 or pos1 < 0 or pos1 >= lenStr or pos2 < 0 or pos2 >= lenStr or pos1 > pos2:
        return "error in inputs {} {} {}".format(pos1, pos2, inStr)
    else:
        if pos1 == pos2:
            #concatenate portion before pos1 and portion from pos1 with pos1 capitalized
            res = inStr[:pos1] + inStr[pos1:].capitalize()
        else:
            #concatenate portion before pos1, portion from pos1 until pos2 with pos1 capitalized,
            #portion from pos2 all the way to the end with pos2 capitalized
            res = inStr[:pos1] + inStr[pos1: pos2].capitalize() + inStr[pos2:].capitalize()
        
        return res
capitalizeTwoLetters(0, 6, "wonderland")
#capitalizeTwoLetters(0, 0, "wonderland")
#capitalizeTwoLetters(9, 9, "wonderland")
