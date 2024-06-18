def reverse_string(string):
    res = ""
    for char in string:
        res = char + res

    return res

print(reverse_string("hello"))

# variable shadowing... just kidding
# it gives hellohello
