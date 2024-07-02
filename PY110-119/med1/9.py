# fibonacci memoization
# basically want to save previously computed values somehow
fibo_dict = {1: 1, 2: 1, }
def fibonacci(nth):
    # base case
    if nth in fibo_dict:
        return fibo_dict[nth]
    
    fibo_dict[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
    return fibo_dict[nth]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True