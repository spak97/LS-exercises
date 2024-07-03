# compute the difference b/w 
# the square of the sum of the first nth positive integers
# and the sum of the squares of the first nth pos ints
def sum_of_squares(nth):
    res = 0
    for n in range(nth + 1):
        res += n**2

    return res

def square_of_sum(nth):
    running_sum = 0
    for n in range(nth + 1):
        running_sum += n
    
    return running_sum**2


def sum_square_difference(nth):
    return square_of_sum(nth) - sum_of_squares(nth)

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True