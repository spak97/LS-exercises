# take a string, double every char in the string and return it

# def repeater(str):
#     # set empty string
#     res = ""
#     # iterate through str
#     # for each c, empty string += c * 2
#     for c in str:
#         res += c * 2
    
#     return res

def repeater(str):
    return ''.join([c * 2 for c in str])



print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True