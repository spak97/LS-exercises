# def is_empty_or_blank(str):
#     if len(str) == 0 or str.isspace():
#         return True
#     else:
#         return False
    
# or
def is_empty_or_blank(str):
    return str.strip(' ') == ''

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True