from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Connect to SQLite database
def connect_db():
    return sqlite3.connect("chocolate_house.db")

# Fetch all flavors
def get_flavors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flavors")
    flavors = cursor.fetchall()
    conn.close()
    return flavors

# Fetch all ingredients
def get_ingredients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredients")
    ingredients = cursor.fetchall()
    conn.close()
    return ingredients

# Fetch all customer suggestions
def get_suggestions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Suggestions")
    suggestions = cursor.fetchall()
    conn.close()
    return suggestions

# Route for homepage
@app.route('/')
def index():
    flavors = get_flavors()
    ingredients = get_ingredients()
    suggestions = get_suggestions()
    return render_template('index.html', flavors=flavors, ingredients=ingredients, suggestions=suggestions)

# Add flavor route
@app.route('/add_flavor', methods=['GET', 'POST'])
def add_flavor():
    if request.method == 'POST':
        name = request.form['name']
        season = request.form['season']
        is_available = True if request.form.get('is_available') else False
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Flavors (name, season, is_available) VALUES (?, ?, ?)", (name, season, is_available))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_flavor.html')

# Add ingredient route
@app.route('/add_ingredient', methods=['GET', 'POST'])
def add_ingredient():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Ingredients (name, quantity, unit) VALUES (?, ?, ?)", (name, quantity, unit))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_ingredient.html')

# Update ingredient route
@app.route('/update_ingredient/<int:id>', methods=['GET', 'POST'])
def update_ingredient(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Ingredients WHERE id=?", (id,))
    ingredient = cursor.fetchone()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        cursor.execute("UPDATE Ingredients SET name=?, quantity=?, unit=? WHERE id=?", (name, quantity, unit, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('update_ingredient.html', ingredient=ingredient)

# Add customer suggestion route
@app.route('/add_suggestion', methods=['GET', 'POST'])
def add_suggestion():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        flavor_name = request.form['flavor_name']
        allergy_concerns = request.form['allergy_concerns']
        suggestion_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Suggestions (customer_name, flavor_name, allergy_concerns, suggestion_date) VALUES (?, ?, ?, ?)", 
                       (customer_name, flavor_name, allergy_concerns, suggestion_date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_suggestion.html')

# Delete suggestion route
@app.route('/delete_suggestion/<int:id>', methods=['GET'])
def delete_suggestion(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Suggestions WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
