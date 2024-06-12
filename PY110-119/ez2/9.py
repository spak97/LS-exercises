# fx that counts the number of occurrences of each element in a list
# print each element alongside the num of occurrences
# case sensitive

def count_occurrences(lst):
    # key = element
    # value = count(key)
    # print key: value
    res = {item: lst.count(item) for item in lst}
    print(res)

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)