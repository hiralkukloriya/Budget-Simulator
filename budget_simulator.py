def show_menu():
    print("\nWelcome to Your Budget Buddy")
    print("What would you like to do today?")
    print("1. Set Monthly Income")
    print("2. Add an Expense")
    print("3. View My Budget Summary")
    print("4. Exit")

def main():
    income = 0
    expenses = {}

    print("Hello there! I'm your Budget Buddy.")
    print("Let's keep track of your money together.")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            income = float(input("How much do you earn per month? "))
            print(f"Great! Your monthly income is set to ₹{income:.2f}")

        elif choice == "2":
            category = input("What expense category (e.g., Rent, Food, Fun)? ")
            amount = float(input(f"How much did you spend on {category}? "))
            expenses[category] = expenses.get(category, 0) + amount
            print(f"Added ₹{amount:.2f} to {category}")

        elif choice == "3":
            total_expenses = sum(expenses.values())
            balance = income - total_expenses
            print("\n--- Your Budget Summary ---")
            print(f"Monthly Income: ₹{income:.2f}")
            print("Expenses Breakdown:")
            for cat, amt in expenses.items():
                print(f"  • {cat}: ₹{amt:.2f}")
            print(f"Total Expenses: ₹{total_expenses:.2f}")
            print(f"Remaining Balance: ₹{balance:.2f}")

            # Friendly feedback
            if balance > 0:
                print("Nice work! You’re saving money this month.")
            elif balance == 0:
                print("You balanced perfectly — no savings, no overspending.")
            else:
                print("Careful! You’re overspending. Let’s try to cut back next time.")

        elif choice == "4":
            print("Thanks for using Budget Buddy. Goodbye!")
            break

        else:
            print("Oops, that wasn’t a valid choice. Try again.")

if __name__ == "__main__":
    main()
