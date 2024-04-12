# odd = [n for n in range(1, 100) if n % 2 != 0]

# for i in odd:
#     print(i)

# bonus
start = int(input())
end = int(input())

for n in range(start, end, 2):
    print(n)
