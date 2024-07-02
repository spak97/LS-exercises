# fibonacci numbers (procedural)
# write a fx that computes the nth Fibonacci number
"""
F(1st) = 1
F(2nd) = 1
F(nth) = F(n - 1) + F(n - 2) (where n > 2)

DS:
    - list
        - uses memory
    - just use two variables to save the previous two numbers
Algo:
    - how do i get the previous two F_nums??
    - have some kind of loop that generates the fibonacci seq and push into list
"""

def fibonacci(n):
    fib = []
    # loop
    for i in range(n):
        if len(fib) == 0 or len(fib) == 1:
            fib.append(1)
        else:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[-1]
        
    # += previous 2 Fnums
    # stop when reach n or something
    # return last num in list

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
