# take a string 
# return string with staggered cap
# capitalize every other character
# non-alphabetic chars are counted as characters

def staggered_case(string):
    res = ""
    for i, c in enumerate(string):
        fx = c.upper if i % 2 == 0 else c.lower
        res += fx()

    return res

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True