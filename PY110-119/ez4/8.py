# list all palindromic substrings of a string
def is_palindrome(string):
    if string == string[::-1] and len(string) > 1:
        return True
    else:
        return False

def leading_substrings(string):
    return [string[:i] for i in range(1, len(string) + 1)]

def substrings(string):
    # call above fx on string, slicing each time til u get to last c
    result = []
    for i in range(len(string)):
        result.extend(leading_substrings(string[i:]))
    
    return result

def palindromes(string):
    # run is_palindrome on each substring
    # if true append to result
    return [substring for substring in substrings(string) if is_palindrome(substring)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') )   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True