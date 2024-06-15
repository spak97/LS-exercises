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

def time_of_day(num):
    day_in_mins = 24 * 60
    time_in_mins = day_in_mins + num