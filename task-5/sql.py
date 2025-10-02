import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn= sqlite3.connect("sales_data.db")
query="""
SELECT product,
    SUM(quantity) As total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""
df=pd.read_sql_query(query,conn)
print(df)
df.plot(kind='bar',x='product',y='revenue',legend=False, title="Revenue by product")
plt.ylabel("Revenue")
plt.savefig("sales_chart.png")
plt.show()
conn.close()
