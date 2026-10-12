customer_id = input("Enter Customer ID: ")
order_amount = float(input("Enter Order Amount (₹): "))
category = input("Enter Customer Category (Premium/Regular): ").strip().lower()
location = input("Enter Delivery Location (Local/Other): ").strip().lower()

# Calculate membership discount
if category == "premium":
    discount = order_amount * 0.15
elif category == "regular":
    discount = order_amount * 0.05
else:
    discount = 0

# Additional discount for orders above ₹5000
if order_amount > 5000:
    discount += 500

# Maximum discount is 20% of original amount
max_discount = order_amount * 0.20
discount = min(discount, max_discount)

# Calculate delivery charges
if order_amount >= 3000:
    delivery_charge = 0
elif location == "local":
    delivery_charge = 50
else:
    delivery_charge = 100

# Calculate final payable amount
final_amount = order_amount - discount + delivery_charge

# Display order summary
print("\n===== E-COMMERCE ORDER SUMMARY =====")
print("Customer ID          :", customer_id)
print("Customer Category    :", category.title())
print("Original Order Amount: ₹", round(order_amount, 2))
print("Discount Amount      : ₹", round(discount, 2))
print("Delivery Charge      : ₹", round(delivery_charge, 2))
print("Final Payable Amount : ₹", round(final_amount, 2))

print("\nOrder Summary:")
print("Original Amount : ₹", round(order_amount, 2))
print("Total Discount  : ₹", round(discount, 2))
print("Delivery Charge : ₹", round(delivery_charge, 2))
print("Amount to Pay   : ₹", round(final_amount, 2))