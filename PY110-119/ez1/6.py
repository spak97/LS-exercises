# exclue non-letters
def strip(str):
    new_word = ""
    for c in str:
        if c.isalpha():
            new_word += c
    
    return new_word

def word_sizes(str):
    words_list = str.split()
    res = {}

    for word in words_list:
        word_size = len(strip(word))
        if word_size not in res:
            res[word_size] = 0
        
        res[word_size] += 1
    
    return res

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})