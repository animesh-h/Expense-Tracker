import csv
import os

DATA_DIR = 'Expense Data'
FILE_NAME = os.path.join(DATA_DIR, 'expenses.csv')

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['date', 'category', 'amount', 'note'])

def read_expenses():
    expenses = []
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['amount'] = float(row['amount'])
            expenses.append(row)
    return expenses

def write_expense(expense):
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense['date'], expense['category'], expense['amount'], expense['note']])