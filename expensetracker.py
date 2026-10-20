# Python Expense Tracker

expenses = []  # list to store 30 days expenses

# Ask user to enter expenses for 30 days
for day in range(1, 31):
    amount = int(input(f"Enter expense for day {day}: "))
    expenses.append(amount)

# Calculations
total_expense = sum(expenses)
average_expense = total_expense / 30
highest_expense = max(expenses)
days_above_1000 = sum(1 for x in expenses if x > 1000)

# Display results
print("\n--- Monthly Expense Report ---")
print(f"Total Expense: ₹{total_expense}")
print(f"Average Expense: ₹{average_expense:.2f}")
print(f"Highest Expense: ₹{highest_expense}")
print(f"Number of days expense exceeded ₹1000: {days_above_1000}")
