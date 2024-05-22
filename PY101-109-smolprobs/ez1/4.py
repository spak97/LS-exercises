print("Enter length")
length = float(input())    

print("Enter width")
width = float(input())

ft_or_m = input("ft or m?")

def room_area(l, w, unit):
    area_m = l * w
    area_ft = area_m * 10.7639
    if unit == "ft":
        print(f"Area of room in feet: {area_ft}")
    else:
        print(f"Area of room in meters: {area_m}.")
      

room_area(length, width, ft_or_m)