def sort_value(item):
    # return the value to a key
    return item[1]

def order_by_value(dic):
    sorted_items = sorted(dic.items(), key=sort_value)    
    return [key for key, value in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True