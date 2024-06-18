# take a positive int
# return sum of its digits

def sum_digits(num):
    # convert to str
    # split into list
    # convert to int
    # return sum
    res = 0
    for d in str(num):
        res += int(d)

    return res

print(sum_digits(23) )              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

