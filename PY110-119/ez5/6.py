# take a list of nums 
# return sum of sums of each leading subsequence in the list

def sum_of_sums(nums):
    sums = []
    for i, n in enumerate(nums):
        if not sums:
            sums.append(n)
        else:
            sums.append(nums[i] + sums[i - 1])
    
    return sum(sums)


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True