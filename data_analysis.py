# data_analysis.py - Data Analysis Functions

def analyze_expenses(transactions):
    """
    Analyze expenses to identify trends or patterns.
    :param transactions: List of transactions, each with 'amount' and 'type' fields.
    """
    if not transactions:
        print("No transactions available for analysis.")
        return

    total_expense = 0.0
    expense_categories = {}

    for transaction in transactions:
        if transaction['type'] == 'expense':
            amount = transaction['amount']
            total_expense += amount
            category = transaction.get('category', 'Uncategorized')
            if category not in expense_categories:
                expense_categories[category] = 0.0
            expense_categories[category] += amount

    print(f"Total Expense: ${total_expense:.2f}")
    print("Expenses by Category:")
    for category, amount in expense_categories.items():
        print(f"  {category}: ${amount:.2f}")

def generate_expense_summary(transactions):
    """
    Generate a summary of expenses, including total and categorized amounts.
    :param transactions: List of transactions, each with 'amount' and 'type' fields.
    """
    if not transactions:
        print("No transactions available for summary.")
        return

    total_expense = 0.0
    expense_categories = {}

    for transaction in transactions:
        if transaction['type'] == 'expense':
            amount = transaction['amount']
            total_expense += amount
            category = transaction.get('category', 'Uncategorized')
            if category not in expense_categories:
                expense_categories[category] = 0.0
            expense_categories[category] += amount

    print(f"Expense Summary:")
    print(f"  Total Expenses: ${total_expense:.2f}")
    print("Categorized Expenses:")
    for category, amount in expense_categories.items():
        print(f"  {category}: ${amount:.2f}")

def main():
    # Sample transactions for testing
    transactions = [
        {'amount': 50.0, 'type': 'expense', 'category': 'Food'},
        {'amount': 30.0, 'type': 'expense', 'category': 'Transport'},
        {'amount': 20.0, 'type': 'expense', 'category': 'Food'},
        {'amount': 100.0, 'type': 'income', 'category': 'Salary'},
    ]

    analyze_expenses(transactions)
    generate_expense_summary(transactions)

if __name__ == "__main__":
    main()
