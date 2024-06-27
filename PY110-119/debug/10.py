# remove duplicates
# presever order

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
def unique_data(nums):
    res = []
    seen = set()
    for n in nums:
        if n not in seen:
            res.append(n)
            seen.add(n)
    
    return res

print(unique_data(data) == [4, 2, 1, 3]) # order not guaranteed