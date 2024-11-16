import sqlite3
from datetime import datetime
import os

# Connect to SQLite database (ensure it's format 3)
def connect_db():
    return sqlite3.connect("chocolate_house.db", detect_types=sqlite3.PARSE_DECLTYPES)

# Create tables if they don't exist
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create Flavors Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        season TEXT NOT NULL,
                        is_available BOOLEAN NOT NULL DEFAULT 1)''')
    
    # Create Ingredients Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Ingredients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit TEXT NOT NULL)''')
    
    # Create Suggestions Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Suggestions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        flavor_name TEXT NOT NULL,
                        allergy_concerns TEXT,
                        suggestion_date TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

# Check if the database exists and remove it if necessary
def reset_db():
    if os.path.exists("chocolate_house.db"):
        os.remove("chocolate_house.db")
        print("Old database removed, creating a fresh one.")

# Add default data for flavors
def add_default_flavors():
    conn = connect_db()
    cursor = conn.cursor()

    # Add default flavors
    cursor.executemany('''INSERT INTO Flavors (name, season, is_available) VALUES (?, ?, ?)''', [
        ('Hot Cocoa', 'Winter', 1),
        ('Strawberry Cream', 'Spring', 1),
        ('Mango Chili', 'Summer', 1),
        ('Key Lime Pie', 'Summer', 1),
        ('Caramel Apple', 'Autumn', 1)
    ])
    
    conn.commit()
    conn.close()

# Add default ingredients
def add_default_ingredients():
    conn = connect_db()
    cursor = conn.cursor()

    # Add default ingredients
    cursor.executemany('''INSERT INTO Ingredients (name, quantity, unit) VALUES (?, ?, ?)''', [
        ('Cocoa beans', 300, 'grams'),
        ('Cocoa butter', 500, 'grams'),
        ('Milk Powder', 1000, 'grams'),
        ('Vanilla Extract', 500, 'milliliters'),
        ('Butter', 250, 'grams'),
        ('Sugar', 2000, 'grams'),
        ('Honey', 100, 'grams')
    ])
    
    conn.commit()
    conn.close()

# Add default customer suggestions
def add_default_suggestions():
    conn = connect_db()
    cursor = conn.cursor()

    # Add default suggestions
    cursor.executemany('''INSERT INTO Suggestions (customer_name, flavor_name, allergy_concerns, suggestion_date) VALUES (?, ?, ?, ?)''', [
        ('Teju', 'Milk Chocolate', 'Dairy Allergy', '2024-11-17 10:00:00'),
        ('Tanmay', 'Dark Chocolate', 'Lactose Intolerant', '2024-11-02 11:30:00'),
        ('Vikas', 'Hazelnut Chocolate', 'Nut Allergy', '2024-11-12 14:15:00'),
        ('Amruth', 'Mint Chocolate', 'Gluten Allergy', '2024-11-13 16:45:00'),
        ('Ammu', 'Peanut Butter Chocolate', 'Peanut Allergy', '2024-11-14 18:20:00')
    ])
    
    conn.commit()
    conn.close()

# Run the setup script
if __name__ == "__main__":
    reset_db()               # Optionally remove any old database
    create_tables()           # Create tables if they don't exist
    add_default_flavors()     # Add default flavors
    add_default_ingredients() # Add default ingredients
    add_default_suggestions() # Add default customer suggestions
    print("Database setup complete with default data!")
