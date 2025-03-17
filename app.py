from flask import Flask, render_template  # Flask for web server, render_template to load HTML files
import sqlite3 

app = Flask(__name__)  # Initialize Flask app

@app.route("/")  # Homepage route
def homepage():
    return render_template("home.html")  # Show homepage

@app.route("/inventory")  # Route to display inventory table
def inventory():
    connection = sqlite3.connect("inventory.db")  # Connect to DB
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")  # Get all inventory rows
    inventory_data = cursor.fetchall() 
    connection.close()
    return render_template("inventory.html", inventory=inventory_data)  # Send data to HTML

@app.route("/update_stock_form")  # Route to show stock update form
def update_stock_form():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT category FROM inventory") #getting categories from inventory for category dropdown menu
    categories = cursor.fetchall() #getting all categories and assigning a variable to it 

    cursor.execute("SELECT DISTINCT name FROM inventory") #getting names from inventory for category dropdown menu
    names = cursor.fetchall() #assigning a variable to them 

    cursor.execute("SELECT DISTINCT size FROM inventory") #getting size from inventory for category dropdown menu
    sizes = cursor.fetchall() #assigning a variable to them 

    cursor.execute("SELECT DISTINCT color FROM inventory") #getting color from inventory for category dropdown menu
    colors = cursor.fetchall() #assigning a variable to them



    connection.close()
    return render_template("update_stock_form.html", categories=categories, names=names, sizes=sizes, colors=colors) # Send to form page
 
if __name__ == "__main__":
    app.run(debug=True)  # Run app in debug mode
