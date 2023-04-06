import sqlite3
import pandas as pd


create_products_table = '''CREATE TABLE IF NOT EXISTS products (
                            product_name TEXT,
                            unit_cost DECIMAL(10,2),
                            PRIMARY KEY (product_name)
                            )'''

create_sales_table = '''CREATE TABLE IF NOT EXISTS sales (
                        product_name TEXT,
                        quantity INTEGER,
                        unit_price DECIMAL(10,2),
                        total_price DECIMAL(10,2),
                        FOREIGN KEY (product_name) REFERENCES products(product_name)
                        )'''

insert_products_data = '''INSERT INTO products (product_name, unit_cost) VALUES (?, ?)'''

insert_sales_data = '''INSERT INTO sales (product_name, quantity, unit_price, total_price) VALUES (?, ?, ?, ?)'''


# Read the products data from Excel
df_products = pd.read_excel('products.xlsx')
products_data = [tuple(x) for x in df_products.to_records(index=False)]

# Read the sales data from Excel
sheet_name = 'Ventas_March'
df_sales = pd.read_excel('ReporteVentas.xlsx', sheet_name=sheet_name, dtype={'quantity': 'float64', 'total_price' : 'float64'})
sales_data = [tuple(x) for x in df_sales.to_records(index=False)]


# Create a connection to the SQLite database
with sqlite3.connect('March_Monthly_Sales.db') as conn:
    cursor = conn.cursor() # cursor object is used to execute the sql statements to create tables, insert data, query, etc.

    # Create the products table
    cursor.execute(create_products_table)

    # Insert the data into the products table
    cursor.executemany(insert_products_data, products_data)

    # Create the sales table
    cursor.execute(create_sales_table)

    # Insert the data into the sales table
    cursor.executemany(insert_sales_data, sales_data)

    # Commit the changes and close the connection
    conn.commit()

print('Data inserted successfully.')
