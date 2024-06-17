# take a str return a list of substrings 
# each substring should begin with the first letter of the word 
# sort from shortest to longest

def leading_substrings(string):
    res = []
    for i in range(1, len(string) + 1):
        res.append(string[:i])

    return res

# All of these examples should print True
print(leading_substrings('abc') )
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])