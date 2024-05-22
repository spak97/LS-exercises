def multisum(n):
    ans = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans
            


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)