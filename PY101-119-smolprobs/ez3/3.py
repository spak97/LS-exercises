def print_in_box(str):
    str_len = len(str)
    top_bot = f"+-{str_len * "-"}-+"
    mid = f"| {str_len * " "} |"
    text = f"| {str} |"
    print(top_bot)
    print(mid)
    print(text)
    print(mid)
    print(top_bot)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')