from dataclasses import dataclass
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
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Expense(**item) for item in data]

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump([expense.__dict__ for expense in expenses], f, indent=4)

def add_expense():
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD): ")
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