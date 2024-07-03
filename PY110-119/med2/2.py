# take lengths of 3 sides of a triangle
# return classification of triangle: equilateral, isosceles, scalene, invalid

def valid_triangle(l1, l2, l3):
    # l1 + l2 > l3
    sides = [l1, l2, l3]
    longest = max(l1, l2, l3)
    sides.remove(longest)

    if sum(sides) > longest:
        return True
    else:
        return False

def isosceles(l1, l2, l3):
    # check if 2 of the sides are equal
    if l1 == l2 or l1 == l3 or l2 == l3:
        return True
    else:
        return False

def triangle(l1, l2, l3):
    if valid_triangle(l1, l2, l3) and l1 == l2 == l3:
        return "equilateral"
    elif valid_triangle(l1, l2, l3) and l1 != l2 != l3:
        return "scalene"
    elif valid_triangle(l1, l2, l3) and isosceles(l1, l2, l3):
        return "isosceles"
    else:
        return "invalid"
    
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True