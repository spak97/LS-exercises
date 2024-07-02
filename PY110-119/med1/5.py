# take a string
# return string with num word replaced with digit
NUM_TO_WORD = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}

def word_to_digit(string):
    word_list = string.split()
    for i, word in enumerate(word_list):
        if word in NUM_TO_WORD:
            word_list[i] = NUM_TO_WORD[word]

    return ' '.join(word_list)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True