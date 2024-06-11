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

def string_to_signed_integer(str):
    # strip signs
    # save sign of str if any
    sign = 0
    if not str[0].isalnum():
        sign = str[0]
    stripped = str.lstrip("-+")
    # run string_to_integer
    if sign == "-":
        return -1 * string_to_integer(stripped)
    else:
        return string_to_integer(stripped)
    # multiply value by - if saved sign == -

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
