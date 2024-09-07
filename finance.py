# finance.py - Core financial operations

def add_income(transactions):
    """Add an income entry to the transactions list."""
    amount = float(input("Enter income amount: "))
    description = input("Enter income description: ")
    transaction = {'type': 'Income', 'amount': amount, 'description': description}
    transactions.append(transaction)
    print(f"Income of {amount} added successfully.\n")


def add_expense(transactions):
    """Add an expense entry to the transactions list."""
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    category = input("Enter expense category: ")
    transaction = {'type': 'Expense', 'amount': amount, 'description': description, 'category': category}
    transactions.append(transaction)
    print(f"Expense of {amount} added successfully.\n")


def calculate_savings(transactions):
    """Calculate and display total savings."""
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'Expense')
    savings = total_income - total_expenses
    print(f"Total Savings: {savings}\n")


def generate_category_report(transactions):
    """Generate a report of expenses by category."""
    category_totals = {}
    for t in transactions:
        if t['type'] == 'Expense':
            category = t['category']
            category_totals[category] = category_totals.get(category, 0) + t['amount']
    
    print("\nCategory Report:")
    for category, total in category_totals.items():
        print(f"Category: {category}, Total Expense: {total}")
    print()


def generate_monthly_report(transactions):
    """Generate a monthly summary report of income and expenses."""
    # This function can be expanded further to use actual dates
    # For now, it gives a simple summary of income and expenses
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'Expense')
    
    print("\nMonthly Summary Report:")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Net Savings: {total_income - total_expenses}\n")
