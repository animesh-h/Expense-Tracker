from pyspark.sql.window import Window
from pyspark.sql.functions import sum as Fsum

def running_total(df):
    windowSpec = Window.orderBy("date").rowsBetween(Window.unboundedPreceding, 0)
    df.withColumn("running_total", Fsum("amount").over(windowSpec)).show()
