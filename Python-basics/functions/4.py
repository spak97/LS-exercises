def squared_number(n):
    return n * n

squared_number(3)   # 9

#5 
def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

# prints nothing because you need parentheses to call function