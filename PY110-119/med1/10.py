# fibonacci number location by length
import sys

sys.set_int_max_str_digits(50_000)
# write a fx that calculates and returns the index of the first fibo number that has the number of digits specified by the argument

fibo_dict = {1: 1, 2: 1, }
def fibonacci(nth):
    # base case
    if nth in fibo_dict:
        return fibo_dict[nth]
    
    fibo_dict[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
    return fibo_dict[nth]

def find_fibonacci_index_by_length(n_digits):
# use memoization
# search and return

