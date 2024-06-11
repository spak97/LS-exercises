DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'

def signed_integer_to_string(num):
    res = ""

    if num == 0:
        return integer_to_string(num)
    elif abs(num) == num:  
        return res + "+" + integer_to_string(num)
    else:
        return res + "-" + integer_to_string(abs(num))


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
"""
basically the same as last prob
if negative
    divmod by -10 or divmod abs(num), 10
    add negative sign 
else
    add positive sign
"""