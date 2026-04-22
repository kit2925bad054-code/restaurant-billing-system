# Restaurant Billing System

# Step 1: Initialize list
items = []

# Step 2: Input number of items
n = int(input("Enter number of items: "))

# Step 3: Get item details
for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    items.append((name, price))

# Step 4: Calculate total
total = 0
print("\n----- BILL -----")
for item in items:
    print(item[0], ":", item[1])
    total += item[1]

# Step 5: Display total
print("----------------")
print("Total Amount:", total)
print("----------------")
