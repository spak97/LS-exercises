"""
write a fx that takes 2 lists as args
return a set that contains union of the two lists
args will always be lists
"""

def union(lst1, lst2):
    return set(lst1) | set(lst2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True