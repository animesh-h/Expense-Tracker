import csv
import os
os.environ['PYSPARK_PYTHON'] = 'py'
from pyspark.sql import SparkSession

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
    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([expense['date'], expense['category'], expense['amount'], expense['note']])

######## SPARK Module ###########

def get_spark_dataframe():
    spark = SparkSession.builder.appName("ExpenseTracker").getOrCreate()
    return spark.read.csv(FILE_NAME, header=True, inferSchema=True)        

######## SPARK Module with local Postgres ###########

def get_spark_session():
    spark = SparkSession.builder \
        .appName("PostgresConnector") \
        .config("spark.jars", r"C:\Users\anisin06\Downloads\Python Projects\Expense Tracker\postgresql-42.7.2.jar") \
        .getOrCreate()
    return spark

def read_postgres_query(spark, query):
    jdbc_url = "jdbc:postgresql://localhost:5432/expense-tracker"
    connection_properties = {
        "user": "postgres",
        "password": "postgres",
        "driver": "org.postgresql.Driver"
    }
    return spark.read.jdbc(
        url=jdbc_url,
        table=f"({query}) AS tmp",
        properties=connection_properties
    )

def write_postgres_query(df, table_name, save_mode="append"):
    jdbc_url = "jdbc:postgresql://localhost:5432/expense-tracker"
    connection_properties = {
        "user": "postgres",
        "password": "postgres",
        "driver": "org.postgresql.Driver"
    }
    df.write.jdbc(
        url=jdbc_url,
        table=table_name,
        mode=save_mode,
        properties=connection_properties
    ) 