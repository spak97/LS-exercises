# take a str arg "First Last"
# return new string "Last, First"

def swap_name(name):
    return ', '.join(name.split()[::-1])

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True