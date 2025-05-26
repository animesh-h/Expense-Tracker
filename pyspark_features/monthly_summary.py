from pyspark.sql.functions import month, year

def monthly_summary(df):
    df.withColumn("month", month("date")) \
      .withColumn("year", year("date")) \
      .groupBy("year", "month", "category") \
      .sum("amount") \
      .orderBy("year", "month") \
      .show()