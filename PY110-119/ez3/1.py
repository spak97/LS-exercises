"""
input: positive or negative int
output: time of day

explicit rules:
    - can't use datetime module
    - if input is negative, time is b4 0000
    - if input is positive, time is post 0000

implicit rules:
    - output must be in str and in military time ("23:57")

DS:
    - nothing special

Algo:
    - represent 24 hrs in mins = 24 * 60 
    - day_in_mins + input = time of day 
    - format time of day 
        - convert into hours and minutes
            - how would do this?
                - 
        - format and return
        - if input positive, add to 0
        - if neg, subtract from 1440
"""
MINUTES_PER_DAY = 24 * 60

def format_time(hrs, mins):
    return f"{hrs:02d}:{mins:02d}"

def time_of_day(delta_mins):
    delta_mins = delta_mins % MINUTES_PER_DAY
    hrs = delta_mins // 60
    mins = delta_mins % 60
    return format_time(hrs, mins)

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True