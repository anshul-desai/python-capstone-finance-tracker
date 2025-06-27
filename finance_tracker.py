def add_expense(data):
    try:
        desc = input("Enter expense description: ").strip()
        if not desc:
            print("Description cannot be empty.")
            return

        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return

        amount_input = input("Enter amount: ").strip()
        amount = float(amount_input)

        if category not in data:
            data[category] = []

        data[category].append((desc, amount))
        print("Expense added successfully.\n")

    except ValueError:
        print("Invalid amount. Please enter a number.\n")
    except Exception as e:
        print("An unexpected error occurred:", e, "\n")


def view_expenses(data):
    if not data:
        print("No expenses recorded yet.\n")
        return

    for category, expenses in data.items():
        print(f"Category: {category}")
        for desc, amount in expenses:
            print(f"  - {desc}: ${amount:.2f}")
    print()


def view_summary(data):
    if not data:
        print("No expenses to summarize.\n")
        return

    print("Summary:")
    for category, expenses in data.items():
        total = sum(amount for _, amount in expenses)
        print(f"{category}: ${total:.2f}")
    print()


def main():
    expenses_data = {}
    print("Welcome to the Personal Finance Tracker!\n")

    while True:
        print("What would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()
        print()

        if choice == '1':
            add_expense(expenses_data)
        elif choice == '2':
            view_expenses(expenses_data)
        elif choice == '3':
            view_summary(expenses_data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")


main()
