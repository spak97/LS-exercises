def crunch(str):
    listified = list(str)
    for c in listified:
        if listified.count(c) > 1:
            listified.remove(c)
    
    return ''.join(listified)


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') )
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

