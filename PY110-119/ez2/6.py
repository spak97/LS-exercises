"""
write a fx that 
takes a list of pos ints
multiply all ints together
divide result by number of elements in list
return result as a string with the value rounded to three decimal places
"""

def multiplicative_average(lst):
    # multiply all elements
    product = 1
    
    for n in lst:
        product *= n
    # divide ^ by len(lst) - 1
    res = product / len(lst)
    # return str(result rounded to 3 decimal places)
    final_res = round(res,3)
    return f"{final_res:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) )
print(multiplicative_average([2, 5, 8]) )
print(multiplicative_average([2, 5]) )
print(multiplicative_average([1, 1, 1, 1]) )
print(multiplicative_average([2, 5, 7, 11, 13, 17]) )
# All of these examples should print True
# print(multiplicative_average([3, 5]) == "7.500")
# print(multiplicative_average([2, 5, 8]) == "26.667")
# print(multiplicative_average([2, 5]) == "5.000")
# print(multiplicative_average([1, 1, 1, 1]) == "0.250")
# print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
