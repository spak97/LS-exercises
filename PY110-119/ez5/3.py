# take list of strs 
# return list of same strs but without vowels

def remove_vowels(lst):
    vowels = "aeiouAEIOU"
    res = []
    for str in lst:
        voweless = ""
        for c in str:
            if c not in vowels:
                voweless += c
        res.append(voweless)
    
    return res

    

    

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
            