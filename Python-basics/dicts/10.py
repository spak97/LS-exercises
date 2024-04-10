numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for pair in numbers.items():
    print(pair)

for k, v in numbers.items():
    print(f"a {k} number is {v}")