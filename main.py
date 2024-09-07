from finance import add_income, add_expense, calculate_savings, generate_category_report, generate_monthly_report
from file_handler import save_transactions, load_transactions, save_budgets, load_budgets
from visualization import visualize_income_expenses, visualize_expense_categories
from budget import set_budget, view_budgets, check_budget_status
from data_analysis import analyze_expenses, generate_expense_summary  # Import data analysis functions
from currency_api import show_conversion_options

# Load transactions, budgets, and goals when the program starts
transactions = load_transactions()
budgets = load_budgets()


def main_menu():
    while True:
        print("Options:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Savings")
        print("4. Generate Category Report")
        print("5. Generate Monthly Summary Report")
        print("6. Visualize Income and Expenses")
        print("7. Visualize Expense Categories")
        print("8. Set Budget")
        print("9. View Budgets")
        print("10. Check Budget Status")
        print("11. Convert Currency for Transactions")
        print("12. Analyze Expenses")  # New option for analyzing expenses
        print("13. Generate Expense Summary")  # New option for generating expense summary
        print("14. Save Data")
        print("15. Exit")

        choice = input("Enter your choice (1-18): ")
        if choice == '1':
            add_income(transactions)
        elif choice == '2':
            add_expense(transactions)
        elif choice == '3':
            calculate_savings(transactions)
        elif choice == '4':
            generate_category_report(transactions)
        elif choice == '5':
            generate_monthly_report(transactions)
        elif choice == '6':
            visualize_income_expenses(transactions)
        elif choice == '7':
            visualize_expense_categories(transactions)
        elif choice == '8':
            set_budget()
        elif choice == '9':
            view_budgets()
        elif choice == '10':
            check_budget_status(transactions)
        elif choice == '11':
            show_conversion_options(transactions)
       
        elif choice == '12':
            analyze_expenses(transactions)  # Call expense analysis function
        elif choice == '13':
            generate_expense_summary(transactions)  # Call expense summary function
       
        
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
