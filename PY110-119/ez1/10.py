# write fx that converts a non-negative int to str rep of that int
"""
input: non-negative int
output: str representation of that int

explicit rules:
    - can't use std conversion fx

implicit rules:
    - ?? I don't think there are any

questions:
    - none

DS:
    - math and variables
    - int is not iterable
    - dict
        - key = int
        - value = str rep

Algo:
    - calculate and save 1's 10's 100's... digits somehow
    - divmod
        - divmod(100, 10) returns a tuple of (result, remainder) "(10, 0)"
"""


def integer_to_string(num):
    digits = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}

    res = ""

    divved = divmod(num, 10)
    while divved[0] != 0:
        curr_digit = digits[divved[1]]
        res += curr_digit
        divved = divmod(divved[0], 10)

    final_digit = digits[divved[1]]
    res += final_digit

    return res[::-1]

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# num = 4321
# res = ""

# divved1 = divmod(num, 10)
# ones = digits[divved1[1]]
# res += ones

# divved2 = divmod(divved1[0], 10)
# tens = digits[divved2[1]]
# res += tens

# divved3 = divmod(divved2[0], 10)
# huns = digits[divved3[1]]
# res += huns

# divved4 = divmod(divved3[0], 10)
# thous = digits[divved4[1]]
# res += thous

# print(divmod(num, 10))
# print(type(ones))
# print(tens)
# print(huns)
# print(thous)
# print(res[::-1])
# print(divved3)
# print(divved4)
