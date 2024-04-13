def twice(n):
    listified = list(str(n))
    list_reversed = listified[::-1]
    if listified == list_reversed:
        return n
    else:
        return n * 2
    
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

test = ['1', '1', '2']
test2 = list(str(24234))
test2.reverse()
print(test)