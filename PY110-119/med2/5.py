# featured number = odd num that is a mult of 7 with all digits once each
# take an int 
# return the next featured number greater than the int
# issue an error msg if there is no next featured number
# largest possible featured num = 9876543201
def diff_digits(n):
    # check for duplicates
    seen = set()
    for d in str(n):
        if d in seen:
            return False
        else:
            seen.add(d)
    return True

def is_featured(num):
    error = "There is no possible number that fulfills those requirements."
    for n in range(num + 1, 9876543201 + 1):
        if n % 7 == 0 and n % 2 != 0 and diff_digits(n):
            return n
        
    return error

print(is_featured(12) == 21)                  # True
print(is_featured(20) == 21)                  # True
print(is_featured(21) == 35)                  # True
print(is_featured(997) == 1029)               # True
print(is_featured(1029) == 1043)              # True
print(is_featured(999999) == 1023547)         # True
print(is_featured(999999987) == 1023456987)   # True
print(is_featured(9876543186) == 9876543201)  # True
print(is_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(is_featured(9876543201) == error)       # True