# take a string
# return a list that conatins every word from the string with each word followed by a space and the word's length
# return empty list if empty string or no arg
# every word is separated by a space

# def word_lengths(string = ""):
#     # make new string for each word
#     # concatenate length of word at the end
#     # append word to result list
#     res = []
#     listed = string.split(" ")
#     for word in listed:
#         length = 0
#         for c in word:
#             length += 1
#         word += f" {length}"
#         if len(word) > 2:
#             res.append(word)
    
#     return res

# or much simpler
def word_lengths(string = ""):
    if not string:
        return []
    return [f"{word} {len(word)}" for word in string.split(" ")]

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True
