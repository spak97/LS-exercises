# take 3 angles of a triangle 
# return type of triangle right, acute, obtuse, invalid

def triangle_type(a1, a2, a3):
    angles = [a1, a2, a3]
    if angles.count(90) == 1:
        return "right"
    elif a1 < 90 and a2 < 90 and a3 < 90:
        return "acute"
    elif a1 > 90 or a2 > 90 or a3 > 90:
        return "obtuse"
        

def valid_triangle(a1, a2, a3):
    angles = [a1, a2, a3]
    if sum(angles) == 180 and 0 not in angles:
        return True
    else:
        return False

def triangle(a1, a2, a3):
    if valid_triangle(a1, a2, a3):
        return triangle_type(a1, a2, a3)
    else:
        return "invalid"
    
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True