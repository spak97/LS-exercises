# take a list of ints between 0 and 19
# return a list of those ints sorted based on the English word for each int
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]
NUMBERED = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def sort_key(num):
    return NUMBERED[num]

def alphabetic_number_sort(lst):
    return sorted(lst, key=sort_key)


print(alphabetic_number_sort(input_list) == expected_result)
# Prints True