import sqlite3

# Function to add a new seasonal flavor
def add_seasonal_flavor(name, start_date, end_date):
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO SeasonalFlavors (name, availability_start, availability_end)
            VALUES (?, ?, ?)
            """, 
            (name, start_date, end_date)
        )

# Function to add a new ingredient to the inventory
def add_ingredient(name, quantity):
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO IngredientInventory (ingredient_name, quantity)
            VALUES (?, ?)
            """, 
            (name, quantity)
        )

# Function to add customer feedback
def add_customer_feedback(name, flavor, allergy):
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO CustomerFeedback (customer_name, suggested_flavor, allergy_concern)
            VALUES (?, ?, ?)
            """, 
            (name, flavor, allergy)
        )

# Function to retrieve all records from a specific table
def get_all_records(table_name):
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()

# Function to update the quantity of an ingredient
def update_ingredient_quantity(ingredient_name, new_quantity):
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE IngredientInventory
            SET quantity = ?
            WHERE ingredient_name = ?
            """, 
            (new_quantity, ingredient_name)
        )
