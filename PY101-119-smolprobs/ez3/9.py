"""
input: str
output: str with only alpha and space. no consecutive spaces allowed

set fx with param str
    set empty result str
    iterate through str
        if char is alpha:
            add to result
        else if char isn't alpha:
            only add space if it won't be consecutive... how?
            check if the last added char is a space with result[-1]
            if first thing needs to be space, need another qualifier
            so if first char is not alpha, add space.
            in conclusion: 
                if str[0] is not alpha or result[-1] is not space
                    add space
                
"""

def clean_up(str):
    result = ""
    for i in range(len(str)):
        if str[i].isalpha():
            result += str[i]
        elif i == 0 or result[-1] != " ":
            result += " "

    return result


print(clean_up("---what's my +*& line?") == " what s my line ")
# True
print(clean_up("---what's my +*& line?"))