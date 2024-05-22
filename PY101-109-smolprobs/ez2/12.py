def negative(n):
    if abs(n) == n:
        return -n
    else:
        return n
    
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True