import sqlite3  

database = sqlite3.connect("inventory.db")  # Connect to or create the database file

cursor = database.cursor()  # Create a cursor to execute SQL commands

# Create the inventory table if it doesn't exist yet
cursor.execute("""CREATE TABLE IF NOT EXISTS inventory(
    barcode TEXT PRIMARY KEY,
    category TEXT,
    name TEXT,
    size TEXT, 
    color TEXT,
    stock INTEGER)""")

#B22 hoodies 
cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (1, 'Hoodie', 'B22', 'XS', 'black', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (2, 'Hoodie', 'B22', 'S', 'black', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (3, 'Hoodie', 'B22', 'M', 'black', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (4, 'Hoodie', 'B22', 'L', 'black', 10)
               """)

#B22 pants
cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (5, 'Pants', 'B22', 'XS', 'black', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (6, 'Pants', 'B22', 'S', 'black', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (7, 'Pants', 'B22', 'M', 'black', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (8, 'Pants', 'B22', 'L', 'black', 10)
               """)

#L/O hoodies
cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (9, 'Hoodie', 'L/O', 'XS', 'off-white', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (10, 'Hoodie', 'L/O', 'S', 'off-white', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (11, 'Hoodie', 'L/O', 'M', 'off-white', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (12, 'Hoodie', 'L/O', 'L', 'off-white', 10)
               """)

#L/O pants
cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (13, 'Pants', 'L/O', 'XS', 'off-white', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (14, 'Pants', 'L/O', 'S', 'off-white', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (15, 'Pants', 'L/O', 'M', 'off-white', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (16, 'Pants', 'L/O', 'L', 'off-white', 10)
               """)

#D/O hoodies
cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (17, 'Hoodie', 'D/O', 'XS', 'grey', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (18, 'Hoodie', 'D/O', 'S', 'grey', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (19, 'Hoodie', 'D/O', 'M', 'grey', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (20, 'Hoodie', 'D/O', 'L', 'grey', 10)
               """)

#D/O pants
cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (21, 'Hoodie', 'D/O', 'XS', 'grey', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (22, 'Hoodie', 'D/O', 'S', 'grey', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (23, 'Hoodie', 'D/O', 'M', 'grey', 10)
               """)

cursor.execute("""
               INSERT INTO inventory(barcode, category, name, size, color, stock)
               VALUES (24, 'Hoodie', 'D/O', 'L', 'grey', 10)
               """)



database.commit()  # Save changes to the database
database.close()   # Close the connection to the database
