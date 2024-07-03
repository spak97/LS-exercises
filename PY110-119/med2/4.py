# take a year
# return the number of Friday 13ths in that year
# assume year > 1752 which is when we started on the modern gregorian calendar

"""
input: year
output: number of friday 13ths

DS: 

Algo:
    - use the datetime module
"""
import datetime

def friday_the_13ths(year):
    count = 0
    for month in range(1, 13):
        date = datetime.date(year, month, 13)

        if date.weekday() == 4:
            count += 1
    
    return count

print(friday_the_13ths(1986) )      # True
print(friday_the_13ths(2015) )      # True
print(friday_the_13ths(2017) )      # True