def clean_up(str):
    result = []
    for c in str:
        if c.isalpha():
            result.append(c)
        else:
            result.append(" ")
    return ''.join(result)


print(clean_up("---what's my +*& line?") == " what s my line ")
# True
print(clean_up("---what's my +*& line?"))