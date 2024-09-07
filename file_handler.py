import json

FILE_NAME = 'transactions.json'
BUDGET_FILE_NAME = 'budgets.json'

def save_transactions(transactions):
    """Save transactions to a file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(transactions, file)
    print("Transactions saved successfully.")

def load_transactions():
    """Load transactions from a file."""
    try:
        with open(FILE_NAME, 'r') as file:
            transactions = json.load(file)
        print("Transactions loaded successfully.")
        return transactions
    except FileNotFoundError:
        print("No previous transactions found.")
        return []

def save_budgets(budgets):
    """Save budgets to a file."""
    with open(BUDGET_FILE_NAME, 'w') as file:
        json.dump(budgets, file)
    print("Budgets saved successfully.")

def load_budgets():
    """Load budgets from a file."""
    try:
        with open(BUDGET_FILE_NAME, 'r') as file:
            budgets = json.load(file)
        print("Budgets loaded successfully.")
        return budgets
    except FileNotFoundError:
        print("No previous budgets found.")
        return {}
