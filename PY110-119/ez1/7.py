def swap(str):
    word_list = str.split()
    res = []
    for word in word_list:
        swapped = ""
        for i, c in enumerate(word):
            if i == 0:
                swapped += word[-1]
            elif i == len(word) - 1:
                swapped += word[0]
            else:
                swapped += c
        res.append(swapped)

    return ' '.join(res)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
"""
input: str of words 
output: new str with first and last letters of every word swapped

explicit rules:
    - every word contains at least one letter
    - str always contains at least one word
    - str isalnum
    - no leading, trailing, or repeated spaces

implicit rules:
    - if word is one letter, return letter
    - case sensitive

DS:
    - .split() and use list

Algo:
    - .split
    - iterate through list
    - change each word
    - outer loop
        - swapped = ""
        - for i, c in word
            - if i == 0
                - swapped += word[-1]
            - elif i == len(word) - 1
                - swapped += word[0]
            - else
                - swapped += c
        - list.append(word)
    - join words into sentence
"""

