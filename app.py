from flask import Flask, request, render_template, redirect, url_for
from operations import (
    add_seasonal_flavor, 
    add_ingredient, 
    add_customer_feedback, 
    get_all_records, 
    update_ingredient_quantity
)

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    # Retrieve all data from the database
    context = {
        "seasonal_flavors": get_all_records("SeasonalFlavors"),
        "ingredients": get_all_records("IngredientInventory"),
        "feedbacks": get_all_records("CustomerFeedback")
    }
    # Pass the retrieved data to the template
    return render_template("index.html", **context)

# Route to add a new seasonal flavor
@app.route("/add_flavor", methods=["POST"])
def add_flavor():
    data = {
        "name": request.form.get("flavor_name"),
        "start_date": request.form.get("start_date"),
        "end_date": request.form.get("end_date")
    }
    add_seasonal_flavor(data["name"], data["start_date"], data["end_date"])
    return redirect(url_for("home"))

# Route to add a new ingredient
@app.route("/add_ingredient", methods=["POST"])
def add_ingredient_route():
    ingredient = {
        "name": request.form.get("ingredient_name"),
        "quantity": request.form.get("quantity")
    }
    add_ingredient(ingredient["name"], ingredient["quantity"])
    return redirect(url_for("home"))

# Route to add customer feedback
@app.route("/add_feedback", methods=["POST"])
def add_feedback():
    feedback = {
        "name": request.form.get("customer_name"),
        "flavor": request.form.get("suggested_flavor"),
        "allergy": request.form.get("allergy_concern")
    }
    add_customer_feedback(feedback["name"], feedback["flavor"], feedback["allergy"])
    return redirect(url_for("home"))

# Route to update ingredient quantity
@app.route("/update_ingredient", methods=["POST"])
def update_ingredient():
    updated_data = {
        "ingredient_name": request.form.get("ingredient_name"),
        "new_quantity": int(request.form.get("quantity"))
    }
    update_ingredient_quantity(updated_data["ingredient_name"], updated_data["new_quantity"])
    return redirect(url_for("home"))

# Route to view records of a specific table
@app.route("/view_records/<table_name>")
def view_records(table_name):
    records = get_all_records(table_name)
    return {"data": records}  # Returns JSON data

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
