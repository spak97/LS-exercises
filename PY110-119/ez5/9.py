"""
input: string 
output: every other alphabetic char uppercased

explicit rules:
    - start from first char
    - count non-alphabetic chars in "every other" count
    - 
implicit rules:
    - ??

DS:
    - um. idk bro. 

Algo:
    - heres an idea.
    - ok so what u want to do is 
    - make a string only consisting of alphabetic chars
    - do the uppercasing and lowercasing
    - then put the non-alphabetic chars back in the right place
    - how would u put them back in the right place tho
    - what if i could have a loop and a counter
    - and iterate through the string
    - and if i encounter a non-alphabetic char, i just continue onto the next iteration?
    - that might work?

"""
def staggered_case(string):
    res = ""
    counter = 0
    i = 0
    while i < len(string):
        if string[i].isalpha():
            fx = string[i].upper if counter % 2 == 0 else string[i].lower
            res += fx()
            counter += 1
            i += 1
        else:
            res += string[i]
            i += 1
            
    return res




string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True