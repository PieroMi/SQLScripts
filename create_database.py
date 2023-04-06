import sqlite3
import datetime
import pandas as pd
import openpyxl



create_sales_table = ''' CREATE TABLE sales (
                        product_name TEXT,
                        quantity INTEGER,
                        unit_price DECIMAL(10,2),
                        total_price DECIMAL(10,2),
                        FOREIGN KEY (product_name) REFERENCES products(product_name)
                        )'''

create_products_table = ''' CREATE TABLE products (
                            product_name TEXT,
                            unit_cost DECIMAL(10,2)
                            )'''


insert_products_data = '''INSERT INTO products (product_name, unit_cost) VALUES (?, ?)'''

insert_sales_data = '''INSERT INTO sales (product_name, quantity, unit_price, total_price) VALUES(?, ?, ?, ?)'''

df = pd.read_excel('C:/Users/PCP/Desktop/SQL POSTO DEMO/Products.xlsx', sheet_name='sheet1')

products = [tuple(x) for x in df.to_records(index=True)]

# print(products)

# workbook = openpyxl.load_workbook(filename='ReporteVentas.xlsx')

# worksheet = workbook['Ventas']

df = pd.read_excel('ReporteVentas.xlsx', sheet_name='Ventas', header=None, skipfooter=1)

with sqlite3.connect('monthly_sales.db') as conn:

    conn.execute(create_sales_table)

    conn.execute(create_products_table)

    for product in products:
        conn.executemany(insert_products_data, product)

    for index, row in df.iterrows():
        product_name = row['product_name']
        quantity = row['quantity']
        unit_price = row['unit_price']
        total_price = row['total_price']

        conn.execute(insert_sales_data, (product_name, quantity, unit_price, total_price))

    conn.commit()

    print("SUCCESSFUL")