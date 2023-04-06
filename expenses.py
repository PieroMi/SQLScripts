import sqlite3
import pandas as pd

create_expenses_table = '''CREATE TABLE IF NOT EXISTS expenses (
                            category TEXT,
                            amount DECIMAL(10,2)
                        )'''

insert_expenses_data = '''INSERT INTO expenses (category, amount) VALUES (?,?)'''

sheet_name = 'Expenses_March'
df_category = pd.read_excel('ReporteVentas.xlsx', sheet_name=sheet_name)
expenses_data = [tuple(x) for x in df_category.to_records(index=False)]

with sqlite3.connect('March_Expenses.db') as conn:
    cursor = conn.cursor()

    cursor.execute(create_expenses_table)

    cursor.executemany(insert_expenses_data, expenses_data)

    conn.commit()

print("Data inserted successfully")