# take 2 args: inv item id and list of transactions
# return a list containing only the transaction for the specified item

def transactions_for(id, transactions):
    # make a list of dicts where dict["id"] == id
    return [dic for dic in transactions if dic["id"] == id]

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True