from pyspark.sql.functions import desc

def top_expenses(df, top_n=3):
    df.orderBy(desc("amount")).show(top_n)