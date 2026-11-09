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

