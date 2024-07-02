# is it prime?
# prime number is a pos num that is evenly divisible only by itself and 1
# take a pos int and return true if prime
"""
Algo:
    - if num is divisible by any 1 < number < num
    - not prime
    - so have to divide by every single number leading up to it
    - don't think there is another way 
"""

def is_prime(num):
    if num == 1:
        return False
    
    for n in range(2, num):
        if num % n == 0:
            return False
        
    return True
    
print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
    
