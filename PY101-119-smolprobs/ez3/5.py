def triangle(n):
    space_count = n - 1
    star_count = 1
    for i in range(1, n + 1):
        print(f"{" " * space_count}{"*" * star_count}")
        space_count -= 1
        star_count += 1

triangle(5)
triangle(9)
        