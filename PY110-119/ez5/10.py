# take sequence of ints

def unique_sequence(nums):
    return list(set(nums))

original = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6]
expected = [1, 2, 3, 4, 5, 6]
print(unique_sequence(original) == expected)      # True