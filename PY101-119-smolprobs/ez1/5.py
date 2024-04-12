bill_amt = float(input("What is the bill? "))
tip_rate = float(input("What is the tip percentage? ")) * 0.01
tip = bill_amt * tip_rate
total = bill_amt + tip

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")