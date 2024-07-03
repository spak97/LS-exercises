# bubble sort
# make multiple passes through a list
# on each pass, two values of each pair of consecutive elements are compared
# if first > second, swap elements
# repeat process until complete pass is made without performing any swaps
# at that point, the list is completely sorted

# take a list
# sort using bubble sort

def bubble_sort(lst):
    while True:
        swapped = False
        for i in range(1, len(lst)):
            if lst[i - 1] <= lst[i]:
                continue

            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            swapped = True

        if not swapped:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True