str = "launch school tech & talk"
str_list = str.split()
cap_sentence = []

for word in str_list:
    cap_sentence.append(word.capitalize())

print(" ".join(cap_sentence))

