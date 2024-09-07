

# budget.py - Manage budgeting features

budgets = {} 

def set_budget():
    """Set a budget for a specific category."""
    category = input("Enter the category to set a budget for: ")
    amount = float(input(f"Enter the budget amount for {category}: "))
    budgets[category] = amount
    print(f"Budget of {amount} set for category '{category}'.")

def view_budgets():
    """View all budgets and their statuses."""
    if not budgets:
        print("No budgets set yet.")
        return

    print("\nCurrent Budgets:")
    for category, amount in budgets.items():
        print(f"Category: {category}, Budget: {amount}")
    print()

def check_budget_status(transactions):
    """Check the spending status against the budget for each category."""
    if not budgets:
        print("No budgets set yet.")
        return

    print("\nBudget Status:")
    category_spending = {category: 0.0 for category in budgets}

    # Calculate total spending per category
    for transaction in transactions:
        if transaction['type'] == 'Expense' and transaction['category'] in category_spending:
            category_spending[transaction['category']] += transaction['amount']

    # Display budget status
    for category, budget in budgets.items():
        spent = category_spending[category]
        remaining = budget - spent
        print(f"Category: {category}, Budget: {budget}, Spent: {spent}, Remaining: {remaining}")
    print()

