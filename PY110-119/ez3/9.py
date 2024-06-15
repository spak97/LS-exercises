# take a list and reverse its elements in place
# mutatue the list passed into the fx
# the returned obj should be the same obj used as the arg
# do not use list.reverse or slicing

def reverse_list(lst):
    # iterate backwards and reassign each idx
    duplicate = lst.copy()
    i = 0
    while i < len(lst):
        for j in range(len(lst) - 1, -1, -1):
            lst[i] = duplicate[j]
            i += 1
            
    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result )               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True