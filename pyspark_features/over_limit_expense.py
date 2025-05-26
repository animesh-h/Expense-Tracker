from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType

def flag_suspicious_expenses(df, threshold=400):
    def flag_expense(amount):
        return "Suspicious" if amount > threshold else "Normal"
    flag_udf = udf(flag_expense, StringType())
    df.withColumn("flag", flag_udf(col("amount"))).show()
