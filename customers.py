# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Marina Rodriguez Teixeira
#
# Reflection 1: .get() vs. bracket notation
# I would use bracket notation when a key must always exist, like a customer's
# name or ID, because a KeyError shows right away that something is wrong with
# the data. I would use .get() for optional fields, like phone or email, that
# some records may not have. My rule of thumb: required field -> brackets,
# optional field -> .get() with a default.
#
# Reflection 2: Summary dictionary vs. Excel
# Building a summary dictionary with a loop reminds me of a pivot table or the
# SUMIF function in Excel, where you total sales by region. The Python version
# is more useful for large datasets because it can process thousands of rows
# automatically, and I can rerun the same code whenever new data comes in
# instead of redoing the work by hand.


# ---------------------------------------------------------
# Exercise 1: One customer
# ---------------------------------------------------------
print("=== Exercise 1: One customer ===")

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400.00,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# ---------------------------------------------------------
# Exercise 2: Update and add
# ---------------------------------------------------------
print("\n=== Exercise 2: Update and add ===")

customer["phone"] = "813-555-0142"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# ---------------------------------------------------------
# Exercise 3: Safe lookup
# ---------------------------------------------------------
print("\n=== Exercise 3: Safe lookup ===")

email = customer.get("email", "no email on file")
print(".get() result:", email)

try:
    print(customer["email"])
except KeyError as error:
    print("Bracket notation raised a KeyError:", error)


# ---------------------------------------------------------
# Exercise 4: Iterate
# ---------------------------------------------------------
print("\n=== Exercise 4: Iterate ===")

for key, value in customer.items():
    print(f"{key}: {value}")

print("\nWithout .items():")
for key in customer:
    print(key)

# Difference: looping with .items() gives both the key and the value at the
# same time. Looping over the dictionary directly only gives the keys, so to
# see a value I would have to look it up with customer[key].


# ---------------------------------------------------------
# Exercise 5: Lookup table
# ---------------------------------------------------------
print("\n=== Exercise 5: Lookup table ===")

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

purchase = 200.00
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount rate: {discount_rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")


# ---------------------------------------------------------
# Exercise 6: List of dicts
# ---------------------------------------------------------
print("\n=== Exercise 6: List of dicts ===")

customers = [
    {"name": "Alice", "tier": "gold", "ytd_spend": 12400},
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "platinum", "ytd_spend": 28900},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

purchase = 300.00
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} ({c['tier']}): ${discount_amount:.2f} off a ${purchase:.2f} purchase")


# ---------------------------------------------------------
# Exercise 7: Nested catalog
# ---------------------------------------------------------
print("\n=== Exercise 7: Nested catalog ===")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")


# ---------------------------------------------------------
# Exercise 8: Sales by region
# ---------------------------------------------------------
print("\n=== Exercise 8: Sales by region ===")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for t in transactions:
    region = t["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + t["amount"]

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")

