# take 2 ints count and starting num of sequence
# return list containing the same num of elements as the count
# value of each element is multiple of starting num
# starting num can be any int
# count is always greater than or equal to 0

def sequence(count, start):
    res = []
    for i in range(1, count + 1):
        res.append(start * i)
    
    return res

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

print(list(range(5, 1, -1)))