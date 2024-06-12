# combine 2 lists
# return new list that contains all elements from both
# alternate each element

def interleave(list1, list2):
    res = []

    for i in range(len(list1)):
        res.append(list1[i])
        res.append(list2[i])
    
    return res

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
