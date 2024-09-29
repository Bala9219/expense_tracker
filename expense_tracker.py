import json
from datetime import datetime

# File to store expenses
EXPENSE_FILE = 'expenses.json'

def load_expenses():
    """Load expenses from a JSON file."""
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file)

def add_expense(expenses):
    """Add a new expense."""
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    date_str = input("Enter the date (DD-MM-YYYY) or press Enter for today: ")
    date = date_str if date_str else datetime.now().strftime('%Y-%m-%d')

    expenses.append({
        'amount': amount,
        'category': category,
        'date': date
    })
    save_expenses(expenses)
    print("Expense added successfully.")

def view_summary(expenses):
    """View expense summaries."""
    if not expenses:
        print("No expenses recorded.")
        return

    total_spent = sum(exp['amount'] for exp in expenses)
    print(f"Total Spending: ${total_spent:.2f}")

    category_summary = {}
    for exp in expenses:
        category_summary[exp['category']] = category_summary.get(exp['category'], 0) + exp['amount']

    print("\nSpending by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: ${amount:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
