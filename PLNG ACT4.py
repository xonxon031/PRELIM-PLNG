
item1 = float(input("Enter cost of item 1: "))
item2 = float(input("Enter cost of item 2: "))

total_cost = item1 + item2
print(f"Total cost: ${total_cost:.2f}")

payment = float(input("Enter payment amount: "))

if payment < total_cost:
    amount_owed = total_cost - payment
    print(f"Insufficient payment. You still owe: ${amount_owed:.2f}")
else:
    change = payment - total_cost
    print(f"Thank you for your payment! Your change is: ${change:.2f}")