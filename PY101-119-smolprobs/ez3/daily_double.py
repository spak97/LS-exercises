import pdb

def crunch(str):
    crunched_str = ''
    index = 0

    while index < len(str):
        if index == len(str) - 1 or str[index] != str[index + 1]:
            crunched_str += str[index]
        index += 1
    
    return crunched_str

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') )
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')