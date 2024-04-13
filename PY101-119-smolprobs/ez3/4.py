def stringy(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True