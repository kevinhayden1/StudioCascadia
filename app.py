# Citation for the following application and pages referenced within application:
# Date 6/6/2022
# Copied/Adapted/Based on:
# Source URL: 
# Flask Starter App from Course: https://github.com/osu-cs340-ecampus/flask-starter-app

# Imports
from email.mime import application
from flask import Flask, render_template, json, redirect, request, url_for
import os
import database.db_connector as db

# Configuration
app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

# Home
@app.route('/')
def root():
    return render_template("main.j2")

# Artists READ
@app.route('/artists', methods=["POST", "GET"])
def artists():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Artists;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        db_connection.close()
        return render_template("sc_artists.j2", Artists=results)
    if request.method == "POST":
        if request.form.get("artist_search"):
            first_name = request.form["ArtistName"]
            last_name = request.form["ArtistName"]
            db_connection = db.connect_to_database()
            query = "SELECT * FROM Artists WHERE first_name LIKE %s OR last_name LIKE %s"
            cursor = db.execute_query(first_name, last_name)
            results = cursor.fetchall()
            query2 = "SELECT * FROM Artists;"
            cursor.execute(query2)
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
            return render_template("sc_artists.j2", search_results=search_results, Artists=results)

# Artists CREATE
@app.route('/artist_add', methods=["POST", "GET"])
def artist_add():
    if request.method == "POST":
        if request.form.get("add_artist"):
            #grab user form inputs
            lname = request.form["last_name"]
            fname = request.form["first_name"]
            address = request.form["address"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            phone = request.form["phone"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Artists (last_name, first_name, address, city, state, zip, phone) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (lname, fname, address, city, state, zip, phone))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("artists"))

    if request.method == "GET":
        return render_template("sc_artist_add.j2")

# Artists UPDATE

@app.route("/artist_edit/<int:id>", methods=["POST", "GET"])
def artist_edit(id):
    if request.method == "GET":
        db_connection = db.connect_to_database()

        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Artists WHERE id = %s"
        db_connection = db.connect_to_database()
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (id,))
        data = cursor.fetchall()

        # mySQL query to grab data for dropdowns
        query2 = "SELECT id, last_name FROM Artists"
        db_connection = db.connect_to_database()
        cursor = db.execute_query(db_connection=db_connection, query=query2)
        artist_data = cursor.fetchall()
        db_connection.close()

        # render artist_edit page passing our query data and artist data to the artist_edit template
        return render_template("sc_artist_edit.j2", data=data, Artists=artist_data)
        #  return render_template("sc_artist_edit.j2")

    if request.method == "POST":
        if request.form.get("edit_artist"):
            db_connection = db.connect_to_database()

            #grab user form inputs
            id = request.form["id"]
            lname = request.form["last_name"]
            fname = request.form["first_name"]
            address = request.form["address"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            phone = request.form["phone"]

            query = "UPDATE Artists SET last_name = %s, first_name = %s, address = %s, city = %s, state = %s, zip = %s, phone=%s WHERE Artists.id = %s"
            cur = db_connection.cursor()
            cur.execute(query, (lname, fname, address, city, state, zip, phone, id))
            db_connection.commit()
            db_connection.close()
        
            return redirect("/artists")


# Artists DELETE
@app.route("/artist_delete/<int:id>")
def artist_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Artists WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/artists")

# Customers BROWSE
@app.route('/customers', methods=['GET'])
def customers():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_customers.j2", Customers=results)

# Customers CREATE
@app.route('/customer_add', methods=["POST", "GET"])
def customer_add():
    if request.method == "POST":
        if request.form.get("add_customer"):
            #grab user form inputs
            lname = request.form["last_name"]
            fname = request.form["first_name"]
            address = request.form["address"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            phone = request.form["phone"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Customers (last_name, first_name, address, city, state, zip, phone) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (lname, fname, address, city, state, zip, phone))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("customers"))

    if request.method == "GET":
        return render_template("sc_customer_add.j2")

# Customers DELETE
@app.route("/customer_delete/<int:id>")
def customer_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Customers WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/customers")

# Locations BROWSE
@app.route('/locations', methods=['GET'])
def locations():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Locations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_locations.j2", Locations=results)

# Locations CREATE
@app.route('/location_add', methods=["POST", "GET"])
def location_add():
    if request.method == "POST":
        if request.form.get("add_location"):
            #grab user form inputs
            location = request.form["location"]
            address = request.form["address"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Locations (location, address, city, state, zip) VALUES (%s, %s, %s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (location, address, city, state, zip))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("locations"))

    if request.method == "GET":
        return render_template("sc_location_add.j2")

# Mediums BROWSE
@app.route('/mediums', methods=['GET'])
def mediums():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Mediums;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_mediums.j2", Mediums=results)

# Mediums CREATE
@app.route('/medium_add', methods=["POST", "GET"])
def medium_add():
    if request.method == "POST":
        if request.form.get("add_medium"):
            #grab user form inputs
            medium = request.form["medium"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Mediums (medium) VALUES (%s);"
            print(query)
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (medium,))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("mediums"))

    if request.method == "GET":
        return render_template("sc_medium_add.j2")

# Mediums DELETE
@app.route("/medium_delete/<int:id>")
def medium_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Mediums WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/mediums")

# Payments BROWSE
@app.route('/payments', methods=['GET'])
def payments():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Payments;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()

    return render_template("sc_payments.j2", Payments=results)

# Payments CREATE
@app.route('/payment_add', methods=["POST", "GET"])
def payment_add():
    if request.method == "POST":
        if request.form.get("add_payment"):
            # grab user form inputs
            sale_id = request.form["sale_id"]
            date = request.form["date"]
            card = request.form["card"]
            cash = request.form["cash"]
            check = request.form["check"]
            card_number = request.form["card_number"]
            exp_date = request.form["exp_date"]
            amount = request.form["amount"]

            # null card_number and exp_date
            if card_number == "" or exp_date == "":
                db_connection = db.connect_to_database()
                query = "INSERT INTO Payments (sale_id, `date`, `card`, cash, `check`, amount) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (sale_id, date, card, cash, check, amount))
                results = cursor.fetchall()
                db_connection.commit()
                db_connection.close()

            # no null inputs
            else:
                db_connection = db.connect_to_database()
                query = "INSERT INTO Payments (sale_id, `date`, `card`, cash, `check`, card_number, exp_date, amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (sale_id, date, card, cash, check, card_number, exp_date, amount))
                results = cursor.fetchall()
                db_connection.commit()
                db_connection.close()

        return redirect(url_for("payments"))

    if request.method == "GET":
        # get valid sale ID drop down
        db_connection = db.connect_to_database()
        query5 = "Select id, amount FROM Sales;"
        cursor5 = db.execute_query(db_connection=db_connection, query=query5)
        results5 = cursor5.fetchall()
        db_connection.commit()
        db_connection.close()
        return render_template("sc_payment_add.j2", sales=results5)

# Payments DELETE
@app.route("/payment_delete/<int:id>")
def payment_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Payments WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/payments")

# Pieces_Artists BROWSE
@app.route('/pieces_artists', methods=["POST", "GET"])
def pieces_artists():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Pieces_Artists;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    # print(results)
    db_connection.close()
    return render_template("sc_pieces_artists.j2", Pieces_Artists=results)

# Pieces_Artists CREATE
@app.route('/piece_artist_add', methods=["POST", "GET"])
def piece_artist_add():
    if request.method == "POST":
        if request.form.get("add_piece_artist"):
            #grab user form inputs
            artist_id = request.form["artist_id"]
            piece_id = request.form["piece_id"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Pieces_Artists (artist_id, piece_id) VALUES (%s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (artist_id, piece_id))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("pieces_artists"))

    if request.method == "GET":
        # get valid artist ID drop down
        db_connection = db.connect_to_database()
        query10 = "Select id, last_name FROM Artists;"
        cursor10 = db.execute_query(db_connection=db_connection, query=query10)
        results10 = cursor10.fetchall()
        # get valid piece ID drop down
        query11 = "Select id, title FROM Pieces;"
        cursor11 = db.execute_query(db_connection=db_connection, query=query11)
        results11 = cursor11.fetchall()
        db_connection.commit()
        db_connection.close()
        return render_template("sc_piece_artist_add.j2", artists=results10, pieces=results11)

# Pieces_Artists DELETE
@app.route("/piece_artist_delete/<int:id>")
def piece_artist_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Pieces_Artists WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/pieces_artists")

# Pieces BROWSE
@app.route('/pieces', methods=["POST", "GET"])
def pieces():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Pieces;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        db_connection.close()
        return render_template("sc_pieces.j2", Pieces=results)

# Pieces CREATE
@app.route('/piece_add', methods=["POST", "GET"])
def piece_add():
    if request.method == "POST":
        if request.form.get("add_piece"):
            #grab user form inputs
            location_id = request.form["location_id"]
            medium_id = request.form["medium_id"]
            title = request.form["title"]
            year = request.form["year"]
            price = request.form["price"]
            available = request.form["available"]
            hold = request.form["hold"]
            commission = request.form["commission"]
            style = request.form["style"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Pieces (location_id, medium_id, title, year, price, available, hold, commission, style) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (location_id, medium_id, title, year, price, available, hold, commission, style))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("pieces"))

    if request.method == "GET":
        # get valid location ID drop down
        db_connection = db.connect_to_database()
        query8 = "Select id, location FROM Locations;"
        cursor8 = db.execute_query(db_connection=db_connection, query=query8)
        results8 = cursor8.fetchall()
        # get valid medium ID drop down
        query9 = "Select id, medium FROM Mediums;"
        cursor9 = db.execute_query(db_connection=db_connection, query=query9)
        results9 = cursor9.fetchall()
        db_connection.commit()
        db_connection.close()
        return render_template("sc_piece_add.j2", locations=results8, mediums=results9)

# Pieces DELETE
@app.route("/piece_delete/<int:id>")
def piece_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Pieces WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/pieces")

# Sales BROWSE
@app.route('/sales', methods=['GET'])
def sales():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Sales;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_sales.j2", Sales=results)

# Sales CREATE
@app.route('/sale_add', methods=["POST", "GET"])
def sale_add():
    if request.method == "POST":
        if request.form.get("add_sale"):
            #grab user form inputs
            piece_id = request.form["piece_id"]
            customer_id = request.form["customer_id"]
            date = request.form["date"]
            amount = request.form["amount"]
            ship = request.form["ship"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Sales (piece_id, customer_id, date, amount, ship) VALUES (%s, %s, %s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (piece_id, customer_id, date, amount, ship))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("sales"))

    if request.method == "GET":
        # get valid piece ID drop down
        db_connection = db.connect_to_database()
        query6 = "Select id, title FROM Pieces;"
        cursor6 = db.execute_query(db_connection=db_connection, query=query6)
        results6 = cursor6.fetchall()
        # get valid customer ID drop down
        query7 = "Select id, last_name FROM Customers;"
        cursor7 = db.execute_query(db_connection=db_connection, query=query7)
        results7 = cursor7.fetchall()
        db_connection.commit()
        db_connection.close()
        return render_template("sc_sale_add.j2", pieces=results6, customers=results7)

# Sales DELETE
@app.route("/sale_delete/<int:id>")
def sale_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Sales WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/sales")

# Shipments BROWSE
@app.route('/shipments', methods=['GET'])
def shipments():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Shipments;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_shipments.j2", Shipments=results)

# Shipments CREATE
@app.route('/shipment_add', methods=["POST", "GET"])
def shipment_add():
    if request.method == "POST":
        if request.form.get("add_shipment"):
            #grab user form inputs
            sale_id = request.form["sale_id"]
            shipped = request.form["shipped"]
            delivered = request.form["delivered"]
            carrier = request.form["carrier"]
            tracking = request.form["tracking"]

            # null card_number and exp_date
            if tracking == "":
                db_connection = db.connect_to_database()
                query = "INSERT INTO Shipments (sale_id, shipped, delivered, carrier) VALUES (%s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (sale_id, shipped, delivered, carrier))
                results = cursor.fetchall()
                db_connection.commit()
                db_connection.close()

             # no null inputs
            else:
                db_connection = db.connect_to_database()
                query = "INSERT INTO Shipments (sale_id, shipped, delivered, carrier, tracking) VALUES (%s, %s, %s, %s, %s);"
                cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (sale_id, shipped, delivered, carrier, tracking))
                results = cursor.fetchall()
                db_connection.commit()
                db_connection.close()

        return redirect(url_for("shipments"))

    if request.method == "GET":
        # get valid sale ID drop down
        db_connection = db.connect_to_database()
        query5 = "Select id, amount FROM Sales;"
        cursor5 = db.execute_query(db_connection=db_connection, query=query5)
        results5 = cursor5.fetchall()
        db_connection.commit()
        db_connection.close()
        return render_template("sc_shipment_add.j2", sales=results5)

# Shipments DELETE
@app.route("/shipment_delete/<int:id>")
def shipment_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Shipments WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/shipments")

# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 6654))
    app.run(port=port, debug=True)
