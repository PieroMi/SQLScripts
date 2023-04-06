import pandas as pd
import sqlite3

# Read the Excel file
df = pd.read_excel('Products.xlsx', sheet_name='sheet1')

# Create the connection to the database
conn = sqlite3.connect('your_database.db')

# Create the products table
conn.execute('CREATE TABLE products (product_name TEXT, unit_cost DECIMAL(10,2))')

# Insert data into the products table
for index, row in df.iterrows():
    conn.execute('INSERT INTO products (product_name, unit_cost) VALUES (?, ?)', (row['product_name'], row['unit_cost']))

# Commit the changes and close the connection
conn.commit()
conn.close()

print('Data has been successfully inserted into the database.')
