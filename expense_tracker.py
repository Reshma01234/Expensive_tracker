"""Expense Tracker CLI - Day 7 mini-project."""


def show_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")


def get_description():
    while True:
        description = input("Description: ").strip()
        if description == "":
            print("Description cannot be blank. Please try again.")
        else:
            return description


def get_amount():
    while True:
        text = input("Amount: ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Invalid amount. Please enter a number such as 250 or 99.50.")
            continue
        # float() accepts "nan" and "inf", and they slip past the < 0 check.
        # nan != nan is True, and inf - inf is nan, so this catches both.
        if amount - amount != 0:
            print("Invalid amount. Please enter a normal number such as 250 or 99.50.")
            continue
        if amount < 0:
            print("Amount cannot be negative. Please try again.")
            continue
        return amount


def add_expense(expenses):
    description = get_description()
    amount = get_amount()
    expenses.append({"description": description, "amount": amount})
    print(f"Added: {description} - {amount:.2f}")


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    print("\n--- Expenses ---")
    number = 1
    for expense in expenses:
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")
        number += 1


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def show_total(expenses):
    total = calculate_total(expenses)
    print(f"Total expenses: {total:.2f}")


def run_menu(expenses):
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    expenses = []
    try:
        run_menu(expenses)
    except (EOFError, KeyboardInterrupt):
        print("\nInput ended. Exiting the Expense Tracker.")


if __name__ == "__main__":
    main()
