import pdb
"""
input: int (year)
output: str ('th century)

set fx with param year 
    math operation and get century 
        year / 100 get something like 
            20.01 == 21st 
            20.00 == 20th 
        so if year / 100 == sth.00 
            century is year / 100  
        else 
            century is year / 100 + 1 
    if ten's place of century is 1: 
        add "th" 
    elif one's place of century is 1:
        add "st"
    elif ones place of cent is 2:
        add "nd"
    elif ones place of cent is 3:
        add "rd"
    else:
        add "th"
"""
def century(year):
    if year % 100 == 0:
        cent = str(year // 100)
    else:
        cent = str((year // 100) + 1)

    tens_place = (int(cent) % 100) // 10
    ones_place = cent[-1]
     
    if tens_place == 1:
        cent += "th"
    elif ones_place == "1":
        cent += "st"
    elif ones_place == "2":
        cent += "nd"
    elif ones_place == "3":
        cent += "rd"
    else:
        cent += "th"
    
    return cent
        
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True




