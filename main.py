import expense_manager
import file_handler

def main_menu():
    file_handler.initialize_file()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses by Category")
        print("4. View Total Spent")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            print("\n--- Add Expense ---")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            note = input("Enter note: ")
            expense_manager.add_expense(date, category, amount, note)
            print("Expense added!")

        elif choice == '2':
            print("\n--- Your Expenses ---")
            expense_manager.view_expenses()
            print()

        elif choice == '3':
            print("\n--- Search Expenses by Category ---")
            category = input("Enter category to search: ")
            expense_manager.search_by_category(category)
            print()

        elif choice == '4':
            while True:
                print("\n--- View Totals ---")
                print("1. Total Spent")
                print("2. Total Spent By Category")
                print("3. Back To Main Menu")
                sub_choice = input("Choose an option: ")

                if sub_choice == '1':
                    print("\n--- Total Spent ---")
                    expense_manager.calculate_total()
                    print()
                elif sub_choice == '2':
                    print("\n--- Total Spent By Category ---")
                    expense_manager.calculate_total_by_category()
                    print()
                elif sub_choice == '3':
                    break
                else:
                    print("Invalid choice. Try again.\n")

        elif choice == '5':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()