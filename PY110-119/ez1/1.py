first = input("Enter the 1st n: ")
second = input("Enter the 2nd n: ")
third = input("Enter the 3rd n: ")
fourth = input("Enter the 4th n: ")
fifth = input("Enter the 5th n: ")
last = input("Enter the last n: ")

nums = [first, second, third, fourth, fifth]

if last in nums:
    print(f"{last} is in {nums}")
else:
    print(f"{last} isn't in {nums}")