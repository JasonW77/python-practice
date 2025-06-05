import csv
import os
from datetime import datetime

FILENAME = 'expenses.csv'


def init_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])


def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Transport, Rent): ").strip()
    description = input("Enter description: ").strip()
    amount = input("Enter amount: ").strip()

    try:
        amount = float(amount)
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")


def view_expenses():
    print("\n📋 All Expenses:\n")
    total = 0
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            print(f"{headers[0]:<12} | {headers[1]:<15} | {headers[2]:<25} | {headers[3]:>8}")
            print("-" * 70)
            for row in reader:
                date, category, description, amount = row
                print(f"{date:<12} | {category:<15} | {description:<25} | ${float(amount):>7.2f}")
                total += float(amount)
        print("-" * 70)
        print(f"{'Total':<55} | ${total:>7.2f}")
    except FileNotFoundError:
        print("No expense file found. Please add an expense first.")


def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    init_file()
    menu()
