# return a list of all substrings of a string
# order returned list by where in the string the substring begins
# order by shortest to longest for each starting index

def leading_substrings(string):
    return [string[:i] for i in range(1, len(string) + 1)]

def substrings(string):
    # call above fx on string, slicing each time til u get to last c
    result = []
    for i in range(len(string)):
        result.extend(leading_substrings(string[i:]))
    
    return result

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True