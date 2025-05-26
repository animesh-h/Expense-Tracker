from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def analyze_expenses(file_path):
    # Step 1: Initialize Spark
    spark = SparkSession.builder \
        .appName("ExpenseAnalyzer") \
        .getOrCreate()

    # Step 2: Load CSV data
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    # Step 3: Basic Transformation
    df.printSchema()
    df.show()

    # Step 4: Example - Total expenses per category
    category_totals = df.groupBy("category").sum("amount")
    category_totals.show()

    # Step 5: Filtered view - expenses > 1000
    big_expenses = df.filter(col("amount") > 100)
    big_expenses.show()

    spark.stop()