from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

print(today_year)
print(iso_year)

# isocalendar returns a tuple with 3 values. Also uses ISO calendar
# instead of gregorian calendar.

# .join needs single argument iterable (list or tuple)

# use in

