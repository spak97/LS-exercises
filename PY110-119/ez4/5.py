# take 2 lists
# determine elements that are unique to the first list
# return a set

# def unique_from_first(lst1, lst2):
#     res = []
#     for i, n in enumerate(lst1):
#         res.append(n)
#         for j, k in enumerate(lst2):
#             if n == k:
#                 res.remove(n)

#     return set(res)

# or much simpler
def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)


list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})