"""
Algo:
    - actually you can't use that just as it is
    - if you just looped rotate_list you would end up with the same num
    - so what to do?
    - use rotate_rightmost_digits
    - ith starts at len(num) and gets decremented 
    - loop runs as long as ith > -1
"""
def rotate_rightmost_digits(num, ith):
    listed = list(str(num))
    # move ith_digit to the end
    ith_digit = listed.pop(-ith)
    listed.append(ith_digit)
    return int(''.join(listed))

# def max_rotation(num):
#     # loop
#     num_list = list(str(num))
#     i = 0
#     while i < len(num_list):
#         ith_digit = num_list.pop(i)
#         num_list.append(ith_digit)
#         i += 1
    
#     return int(''.join(num_list))

# OR use the function you already wrote
def max_rotation(num):
    for count in range(len(str(num)), 1, -1):
        num = rotate_rightmost_digits(num, count)

    return num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
    