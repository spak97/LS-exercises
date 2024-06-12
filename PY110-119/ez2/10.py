# take list of ints
# return avg of all ints
# rounded down to int of avg

def average(lst):
    total = 0
    for n in lst:
        total += n
    
    ans = total // len(lst)

    return ans


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

