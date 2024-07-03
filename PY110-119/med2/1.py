# fx that takes a string 
# return a dict containing percentages
# counts spaces

def letter_percentages(string):
    res = {}
    # count total num of chars
    total = len(string)
    lower, upper, neither = 0, 0, 0
    for c in string:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        else:
            neither += 1
    p_lower = f"{round((lower / total) * 100, 2):.2f}"
    p_upper = f"{round((upper / total) * 100, 2):.2f}"
    p_neither = f"{round((neither / total) * 100, 2):.2f}"

    res['lowercase'] = p_lower
    res['uppercase'] = p_upper
    res['neither'] = p_neither

    return res

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') )

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') )

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') )
