import sqlite3
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")
sample_data = [
    ("Laptop", 3, 50000),
    ("Laptop", 2, 52000),
    ("Mouse", 10, 500),
    ("Mouse", 7, 450),
    ("Keyboard", 5, 1500),
    ("Keyboard", 3, 1600),
    ("Monitor", 4, 12000),
    ("Monitor", 2, 11500),
    ("Headphones", 6, 2000),
    ("Headphones", 4, 2200)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("sales_data.db created with sample data")
