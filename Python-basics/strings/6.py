# def is_empty(str):
#     if len(str) == 0:
#         return True
#     else:
#         return False



# simpler
def is_empty(str):
    return len(str) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
