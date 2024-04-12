# def xor(arg1, arg2):
#     if arg1:
#         if not arg2:
#             return True
#     elif not arg1:
#         if arg2:
#             return True
#     else:
#         return False

#or

def xor(arg1, arg2):
    if (arg1 and not arg2) or (arg2 and not arg1):
        return True
    
    return False


print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)