def is_real_palindrome(str):
    # case-insensitive
    # ignore all non-alphanumeric
    stripped = ""
    for c in str:
        if c.isalnum():
            stripped += c
    
    return stripped[::-1].lower() == stripped.lower() 


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True