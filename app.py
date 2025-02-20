from flask import Flask, render_template
import sqlite3

app = Flask(__name__) 

@app.route("/")
def homepage():
    return render_template("home.html") 

@app.route("/inventory") 
def inventory():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor() 
    cursor.execute("SELECT * FROM inventory")
    inventory_data = cursor.fetchall()
    connection.close()
    print("Fetched Inventory Data:", inventory_data)  #Debugging Step
    return render_template("inventory.html", inventory=inventory_data) 

if __name__ == "__main__":
    app.run(debug=True) 