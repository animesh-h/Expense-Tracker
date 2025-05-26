import os
os.environ['PYSPARK_PYTHON'] = 'py'
from pyspark.sql.functions import to_date
from pyspark.sql import Row
import expense_manager
import file_handler
import pyspark_features.over_limit_expense

def main_menu():
    file_handler.initialize_file()
    spark = file_handler.get_spark_session()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses by Category")
        print("4. View Total Spent")
        print("5. Over Limit Expense")
        print("6. Add Expenses in DB")
        print("7. Show Expenses from DB")
        print("8. Exit")

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
            print("\n--- Over Limit Expense ---")
            df = file_handler.get_spark_dataframe()
            pyspark_features.over_limit_expense.flag_suspicious_expenses(df)

        if choice == '6':
            print("\n--- Add Expense in DB---")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            note = input("Enter note: ")
            data = [Row(date=date, category=category, amount=amount, note=note)]
            df = spark.createDataFrame(data)
            df = df.withColumn("date", to_date("date", "yyyy-MM-dd"))
            file_handler.write_postgres_query(df, "expenses", save_mode="append")
            print("Expense added in db!")

        elif choice == '7':
            print("\n--- Read from DB ---")
            query = "SELECT * FROM expenses"
            df = file_handler.read_postgres_query(spark, query)
            df.show()

        elif choice == '8':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()