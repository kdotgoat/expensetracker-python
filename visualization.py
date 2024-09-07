# visualization.py - Visualization of financial data

import matplotlib.pyplot as plt

def visualize_income_expenses(transactions):
    """Visualize income and expenses using a bar chart."""
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'Income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'Expense')

    labels = ['Income', 'Expenses']
    amounts = [total_income, total_expenses]

    plt.bar(labels, amounts, color=['green', 'red'])
    plt.title('Income vs. Expenses')
    plt.ylabel('Amount')
    plt.show()


def visualize_expense_categories(transactions):
    """Visualize expenses by category using a pie chart."""
    category_totals = {}
    for t in transactions:
        if t['type'] == 'Expense':
            category = t['category']
            category_totals[category] = category_totals.get(category, 0) + t['amount']
    
    if not category_totals:
        print("No expenses to display.")
        return

    labels = category_totals.keys()
    sizes = category_totals.values()

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Expenses by Category')
    plt.show()
