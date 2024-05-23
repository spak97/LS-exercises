def word_sizes(str):
    res = {}
    for word in str.split():
        res[len(word)] = 0
    for word in str.split():
        if len(word) in res:
            res[len(word)] += 1

    return res

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
"""
input: str of words
output: dict {length of existing word: n of words that length}

explicit rules:
    - words are any seq of non-space characters
    - 
implicit rules:
    - empty string returns empty dict

ds: 
    - dict
algo:
    - split str
    - iterate through list
    - key = len(word)
    - value = count of 
"""