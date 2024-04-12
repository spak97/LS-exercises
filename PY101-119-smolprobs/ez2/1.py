def greetings(lst, dct):
    name = " ".join(lst)
    title = " ".join(list(dct.values()))
    return f"Hello, {name}! Nice to have a {title} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.