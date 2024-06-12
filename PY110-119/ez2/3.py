"""
write a fx that takes a list as an arg 
returns a list that contains 2 list elements.

put first half of orig list elements in first element of return value
put second half in the second element

if orig list contains odd number of elements, place middle element in first half
"""

def halvsies(lst):
    half = (len(lst) + 1) // 2
    first = lst[:half]
    second = lst[half:]

    return [first, second]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])