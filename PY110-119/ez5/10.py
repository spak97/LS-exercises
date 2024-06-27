# take sequence of ints
"""
input: list of ints
output: list of unique ints from original list in original order

Algo:
    - iterate through list 
    - push ints onto new list
    - if value already exists in new list
        - skip int
    
"""

def unique_sequence(nums):
    res = []
    for n in nums:
        if n not in res:
            res.append(n)
        else:
            continue

    return res

original = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6]
expected = [1, 2, 3, 4, 5, 6]
print(unique_sequence(original) == expected)      # True