# take a str, double every consonatn in the str
# do not double vowels, punctuation, or whitespace

def double_consonants(string):
    res = ""
    vowels = "aeiou"
    for c in string:
        if c.isalpha() and c not in vowels:
            res += c * 2
        else:
            res += c

    return res

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")


