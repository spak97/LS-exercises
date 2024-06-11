# fx that takes str of digits and returns int
# don't use int
# assume all chars are numeric
# assume all are positive

def string_to_integer(s):
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in s:
        value = (10 * value) + digits[char]
    
    return value


print(string_to_integer("4321"))
print(ord("5") - ord("0"))

"""
input: number in type str
output: number in type int

explicit rules
    - can't use int()
    - calculate the result by using the characters in the string
    - assume all characters are numeric

implicit rules
    - ?? Are there even any?
    - I don't think so

DS
    - 
"""