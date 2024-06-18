# take 2 lists of ints of same length
# return new list where each element is the product of corresponding elements from the two lists

def multiply_items(lst1, lst2):
    return [lst1[i] * lst2[i] for i in range(len(lst1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True