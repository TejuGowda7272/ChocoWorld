import sqlite3
from datetime import datetime

# Connect to SQLite database
def connect_db():
    return sqlite3.connect("chocolate_house.db")

# Create tables if they don't exist
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        season TEXT NOT NULL,
        is_available BOOLEAN NOT NULL DEFAULT 1
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        unit TEXT NOT NULL
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        flavor_name TEXT NOT NULL,
        allergy_concerns TEXT,
        suggestion_date TEXT NOT NULL
    )''')
    
    conn.commit()
    conn.close()

# Add a new flavor
def add_flavor(name, season, is_available=True):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Flavors (name, season, is_available) VALUES (?, ?, ?)",
                   (name, season, is_available))
    conn.commit()
    conn.close()

# View all flavors
def view_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Flavors")
    flavors = cursor.fetchall()
    for flavor in flavors:
        print(flavor)
    conn.close()

# Add ingredients
def add_ingredient(name, quantity, unit):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Ingredients (name, quantity, unit) VALUES (?, ?, ?)",
                   (name, quantity, unit))
    conn.commit()
    conn.close()

# View all ingredients
def view_ingredients():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Ingredients")
    ingredients = cursor.fetchall()
    for ingredient in ingredients:
        print(ingredient)
    conn.close()

# Add customer suggestion
def add_suggestion(customer_name, flavor_name, allergy_concerns):
    suggestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO Suggestions (customer_name, flavor_name, allergy_concerns, suggestion_date) VALUES (?, ?, ?, ?)",
                   (customer_name, flavor_name, allergy_concerns, suggestion_date))
    conn.commit()
    conn.close()

# View customer suggestions
def view_suggestions():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Suggestions")
    suggestions = cursor.fetchall()
    for suggestion in suggestions:
        print(suggestion)
    conn.close()

if __name__ == "__main__":
    create_tables()
    
    # Example usage (You can add more commands or inputs here)
    add_flavor("Hot Cocoa", "Winter")
    add_ingredient("Cocoa", 50, "grams")
    add_suggestion("Alice", "Chocolate Mint", "None")
    
    print("\nAvailable Flavors:")
    view_flavors()
    
    print("\nIngredients:")
    view_ingredients()
    
    print("\nCustomer Suggestions:")
    view_suggestions()
