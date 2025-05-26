from pyspark.sql.functions import sum as Fsum, col

def category_percentage(df):
    total_amount = df.agg(Fsum("amount")).collect()[0][0]
    df.groupBy("category") \
      .sum("amount") \
      .withColumn("percentage", (col("sum(amount)") / total_amount) * 100) \
      .show()