from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import json

DATA_FILE = Path("expenses.json")

@dataclass
class Expense:
    amount: float
    category: str
    date: str
    description: str = ""

def load_expenses():
    # If the data file doesn't exist yet or is empty/invalid, return an empty list
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r") as f:
            # json.load will raise a JSONDecodeError for empty or malformed files
            data = json.load(f)
            if not isinstance(data, list):
                # unexpected format, ignore it
                return []
            return [Expense(**item) for item in data]
    except json.JSONDecodeError:
        # file exists but is empty or contains invalid JSON
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump([expense.__dict__ for expense in expenses], f, indent=4)

def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = datetime.now().isoformat()
    description = input("Description (optional): ")
    expense = Expense(amount, category, date, description)

    current_expenses = load_expenses()
    current_expenses.append(expense)
    save_expenses(current_expenses)

    print(f"Expense added: {expense}")

def view_expenses():
    print("Viewing all expenses:")
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Amount: ${expense.amount}, Category: {expense.category}, Date: {expense.date}, Description: {expense.description}")

def main():
    print("Welcome to the Expense Tracker!")

    while True:
        print("Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()