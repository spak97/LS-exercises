"""
fx that
takes 2 lists of numbers
return new list that contains the product of each pair of nums that have the same index
lists contain the same number of elements
"""

def multiply_list(list1, list2):
    res = []
    for i in range(len(list1)):
        res.append(list1[i] * list2[i])

    return res

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # Trues