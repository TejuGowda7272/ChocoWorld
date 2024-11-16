# ChocoWorld
Simple Python Application for a fictional chocolate house

# This Python application simulates a chocolate house using SQLite to manage:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

# Chocolate House Application

The Chocolate House is a Flask-based web application designed to manage a fictional chocolate shop's seasonal flavors, ingredient inventory, and customer suggestions. It demonstrates the integration of Python, Flask, SQLite, and basic frontend technologies (HTML, CSS, and JavaScript).


### Folder Structure
```
Chocolate_House/
│
├── app.py                  # Main Flask application
├── init_db.py              # Script to initialize the database
├── chocolate_house.db      # SQLite database file
├── templates/              # HTML templates for the application
│   ├── index.html          # Home page
│   ├── add_flavor.html     # Add a new flavor
│   ├── add_ingredient.html # Add a new ingredient
│   ├── update_ingredient.html # Update ingredient quantities
│   ├── add_suggestion.html # Add a new suggestion
│   ├── delete_suggestion.html # Delete a customer suggestion
├── static/
│   └── style.css           # CSS for application styling
└── README.md               # Readme file with project description and instructions
```

---

# Requirements
- Python 3.10+
- Flask (`pip install flask`)
- SQLite (comes pre-installed with Python)

---

### **Setup Instructions**

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/chocolate-house.git
cd chocolate-house
```

#### Step 2: Set up a Virtual Environment (Optional but Recommended)
```bash
python -m venv env

Source env\Scripts\activate    
```

#### Step 3: Install Dependencies
pip install flask


#### Step 4: Initialize the Database
Run the `init_db.py` script to create the database and tables:
python init_db.py


#### Step 5: Start the Application
Run the Flask application using the following command:
python app.py

#### Step 6: Open in Browser
Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the application.

---

#### **Usage Instructions**
- **Home Page**:
  View the list of seasonal flavors, ingredients, and customer suggestions.
  
- **Add New Flavor**:
  Navigate to the "Add Flavor" page to create a new chocolate flavor.
  
- **Manage Ingredients**:
  Add or update the quantity of ingredients in the inventory.

- **Customer Suggestions**:
  View, add, or delete customer suggestions.


#### Contact
For queries or issues, contact:  
- **Name**: Tejaswini G H  
- **Email**:tejugowda363@gmail.com  

#### Snippets
![Image Alt](https://github.com/TejuGowda7272/ChocoWorld/blob/a608783e7a2da517dbb5c02041ed2081b6d67756/Screenshots/Screenshot%20(9).png)

![Image Alt](https://github.com/TejuGowda7272/ChocoWorld/blob/00dff603aa40480912949b1a3e7dab5667616b6c/Screenshots/Screenshot%20(10).png)

![Image Alt](https://github.com/TejuGowda7272/ChocoWorld/blob/00dff603aa40480912949b1a3e7dab5667616b6c/Screenshots/Screenshot%20(11).png)

![Image Alt](https://github.com/TejuGowda7272/ChocoWorld/blob/a608783e7a2da517dbb5c02041ed2081b6d67756/Screenshots/Screenshot%20(12).png)

![Image Alt](https://github.com/TejuGowda7272/ChocoWorld/blob/a608783e7a2da517dbb5c02041ed2081b6d67756/Screenshots/Screenshot%20(13).png)

![Image Alt](https://github.com/TejuGowda7272/ChocoWorld/blob/a608783e7a2da517dbb5c02041ed2081b6d67756/Screenshots/Screenshot%20(14).png)

