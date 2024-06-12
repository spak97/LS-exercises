# take 1 pos int as an arg return list of the digits in the int

def digit_list(num):
    res = []
    stringed = str(num)

    for d in stringed:
        res.append(int(d))

    return res

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

