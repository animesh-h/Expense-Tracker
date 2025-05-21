import file_handler

def add_expense(date, category, amount, note):
    expense = {
        'date': date,
        'category': category,
        'amount': float(amount),
        'note': note
    }
    file_handler.write_expense(expense)

def view_expenses():
    expenses = file_handler.read_expenses()
    for expense in expenses:
        print(f"{expense['date']} | {expense['category']} | ${expense['amount']} | {expense['note']}")

def search_by_category(category):
    expenses = file_handler.read_expenses()
    found = [e for e in expenses if e['category'].lower() == category.lower()]
    for expense in found:
        print(f"{expense['date']} | {expense['category']} | ${expense['amount']} | {expense['note']}")

def calculate_total():
    expenses = file_handler.read_expenses()
    total = sum(e['amount'] for e in expenses)
    print(f"Total spent: ${total:.2f}")


def calculate_total_by_category():
    expenses = file_handler.read_expenses()
    category_totals = {}

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")