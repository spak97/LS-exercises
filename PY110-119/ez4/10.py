# return True or False based on whether inventory item is available
# return true only if the sum of the quantity values is > 0

def transactions_for(id, transactions):
    # make a list of dicts where dict["id"] == id
    return [dic for dic in transactions if dic["id"] == id]

def is_item_available(id, transactions):
    # get inventory totals for each item
        # add if in
        # subtract if out
    total = 0
    for dic in transactions:
        if dic["id"] == id and dic["movement"] == "in":
            total += dic["quantity"]
        elif dic["id"] == id and dic["movement"] == "out":
            total -= dic["quantity"]
    # if total for item inventory is >= 0 return True
    return total >= 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True