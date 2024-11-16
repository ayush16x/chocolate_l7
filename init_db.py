import sqlite3

# Establish a connection to the database
with sqlite3.connect("chocolate_house.db") as connection:
    cursor = connection.cursor()
    
    # Create SeasonalFlavors table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SeasonalFlavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            availability_start DATE NOT NULL,
            availability_end DATE NOT NULL
        )
    """)

    # Create IngredientInventory table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS IngredientInventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)

    # Create CustomerFeedback table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CustomerFeedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            suggested_flavor TEXT,
            allergy_concern TEXT
        )
    """)

# No need for explicit commit and close as `with` handles it
