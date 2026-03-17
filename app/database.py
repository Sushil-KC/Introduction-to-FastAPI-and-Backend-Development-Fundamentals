import sqlite3

connection = sqlite3.connect("sqllite.db")

cursor = connection.cursor()

# 1. Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS shipment (id INTEGER PRIMARY KEY, weight REAL, content TEXT, status TEXT)")

# cursor.execute("DROP TABLE shipment;")
# connection.commit()
# 2. Add shipment Data
# cursor.execute("""
#     INSERT INTO shipment 
#     VALUES (2, 3.23, 'Basalt', 'In Transit')
# """)
# connection.commit()


# 3. Read a shipment by id
# cursor.execute("""
# SELECT * FROM shipment WHERE id = 1;
# """)
# print(cursor.fetchone())


# cursor.execute("""
# SELECT * FROM shipment;
# """)
# print(cursor.fetchall())

# cursor.execute("""
# SELECT * FROM shipment;
# """)
# print(cursor.fetchmany(1))

# 4. Delete shipment by ID
# cursor.execute("""
#             DELETE FROM shipment where id = 2;
#             """)
# connection.commit()


# 5. UPDATE shipment by ID
# cursor.execute("""
#             UPDATE shipment set weight='100' where id = 2;
#             """)
# connection.commit()
# Close Connection
connection.close()
