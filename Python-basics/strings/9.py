def starts_with(str, prefix):
    count = []
    for i in range(len(prefix) - 1):
        if prefix[i] == str[i]:
            count.append(True)
        else:
            count.append(False)
    if False in count:
        return False
    else:
        return True
    
# or just use method .startswith



print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True