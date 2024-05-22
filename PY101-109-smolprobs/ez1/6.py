integer = int(input("Enter an int greater than 0: "))
computation = input("Enter s to compute sum, or p to compute product ")

sum = sum(range(1, integer + 1))
prod = 1
for n in range(1, integer + 1):
    prod *= n

if computation == "s":
    print(f"The sum of the ints between 1 and {integer} is {sum}")
elif computation == "p":
    print(f"The product of the ints between 1 and {integer} is {prod}")
else:
    print("Invalid input. Please run again")