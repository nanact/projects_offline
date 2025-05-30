
bill_amount = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

due_amount = bill_amount - amount_paid

if due_amount > 0:
    print(f"The customer still owes {due_amount:.2f}.")
elif due_amount < 0:
    print(f"Change to return: {-due_amount:.2f}.")
else:
    print("The bill is fully paid. No amount due.")