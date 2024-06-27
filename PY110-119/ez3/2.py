# take time of day and return minutes before and after midnight
# so I have to somehow deformat it
# you get hours and mins
# turn it into mins

def after_midnight(time):
    # take first two digits convert to int
    hrs_in_mins = int(time[:2]) * 60
    # ^ * 60 to get mins
    # convert last two digits to get mins
    mins = int(time[-2:])
    # add together to get total mins
    if time == "24:00":
        return 0
    return hrs_in_mins + mins


def before_midnight(time):
    hrs_in_mins = int(time[:2]) * 60
    mins = int(time[-2:])

    if time == "24:00" or time == "00:00":
        return 0
    return 1440 - (hrs_in_mins + mins)


test = "1223"
print(int(test[:2]))
print(int(test[-2:]))

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

