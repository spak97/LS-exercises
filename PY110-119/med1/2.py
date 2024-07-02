# rotate the last count digits of a number
# take 2 ints (num, ith_digit)
# move the ith_digit to the end
# shift the rest left

"""
Algo:
    - convert num into str
    - convert str(num) into list
    - move ith_digit to the end
    - return str(joined list)
"""

def rotate_rightmost_digits(num, ith):
    listed = list(str(num))
    # move ith_digit to the end
    ith_digit = listed.pop(-ith)
    listed.append(ith_digit)
    return int(''.join(listed))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True



