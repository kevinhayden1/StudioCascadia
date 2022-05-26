from email.mime import application
from flask import Flask, render_template, json, redirect, request, url_for
import os
import database.db_connector as db

### Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

### Routes 

# Home

@app.route('/')
def root():
    return render_template("main.j2")

# Artists CRUD

@app.route('/artists', methods=["POST", "GET"])
def artists():
    if request.method == "GET":
        db_connection = db.connect_to_database()
        query = "SELECT * FROM Artists;"
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        db_connection.close()
        return render_template("sc_artists.j2", Artists=results)

# Add Artist
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

# Edit Artist

@app.route("/artist_edit/<int:id>", methods=["POST", "GET"])
def artist_edit(id):
    if request.method == "GET":
        print("Edit GET")
        print(id)
        db_connection = db.connect_to_database()

        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Artists WHERE id = %s"
        cursor = db_connection.cursor()
        cursor.execute(query, (id,))
        data = cursor.fetchall()

        # # mySQL query to grab data for dropdowns
        query2 = "SELECT id, last_name FROM Artists"
        cursor = db_connection.cursor()
        cursor.execute(query2)
        artist_data = cursor.fetchall()

        db_connection.close()

        # render artist_edit page passing our query data and artist data to the artist_edit template
        return render_template("sc_artist_edit.j2", data=data, artists=artist_data)
        #  return render_template("sc_artist_edit.j2")

    if request.method == "POST":
        if request.form.get("edit_artist"):
            print("Edit POST")
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


# Delete Artist
@app.route("/artist_delete/<int:id>")
def artist_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Artists WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/artists")

# Customers CRUD

@app.route('/customers', methods=['GET'])
def customers():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Customers;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_customers.j2", Customers=results)

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

## Edit Form
@app.route('/customer_edit', methods=['GET'])
def customer_edit():
    return render_template("sc_customer_edit.j2")

# Delete Customer
@app.route("/customer_delete/<int:id>")
def customer_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Customers WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/customers")

# Locations CRUD

@app.route('/locations', methods=['GET'])
def locations():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Locations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_locations.j2", Locations=results)

# Add Location
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

## Edit Form
@app.route('/location_edit', methods=['GET'])
def location_edit():
    return render_template("sc_location_edit.j2")

# Delete Location
@app.route("/location_delete/<int:id>")
def location_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Locations WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/locations")

# Mediums CRUD

@app.route('/mediums', methods=['GET'])
def mediums():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Mediums;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_mediums.j2", Mediums=results)

# Add Medium
@app.route('/medium_add', methods=["POST", "GET"])
def medium_add():
    if request.method == "POST":
        if request.form.get("add_medium"):
            #grab user form inputs
            media = request.form["media"]
            db_connection = db.connect_to_database()
            query = "INSERT INTO Mediums (media) VALUES (%s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (media))
            results = cursor.fetchall()
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("mediums"))

    if request.method == "GET":
        return render_template("sc_medium_add.j2")

## Edit Form
@app.route('/medium_edit', methods=['GET'])
def medium_edit():
    return render_template("sc_medium_edit.j2")

# Delete Medium
@app.route("/medium_delete/<int:id>")
def medium_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Mediums WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/mediums")

# Payments CRUD

@app.route('/payments', methods=['GET'])
def payments():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Payments;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_payments.j2", Payments=results)

## Add Form
@app.route('/payment_add', methods=["POST", "GET"])
def payment_add():
    # if request.method == "POST":
    #     if request.form.get("add_payment"):
    #         #grab user form inputs
    #         date = request.form["date"]
    #         card = request.form["card"]
    #         cash = request.form["cash"]
    #         check = request.form["check"]
    #         card_number = request.form["card_number"]
    #         exp_date = request.form["exp_date"]
    #         amount = request.form["amount"]

    #         # null card_number and exp_date
    #         if card_number == "" and exp_date == "":
    #             db_connection = db.connect_to_database()
    #             query = "INSERT INTO Payments (date, card, cash, check, amount) VALUES (%s, %s, %s, %s, %s);"
    #             cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (date, card, cash, check, amount))
    #             results = cursor.fetchall()
    #             db_connection.commit()
    #             db_connection.close()

    #         # no null inputs
    #         else:
    #             db_connection = db.connect_to_database()
    #             query = "INSERT INTO Payments (date, card, cash, check, card_number, exp_date, amount) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    #             cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (date, card, cash, check, card_number, exp_date, amount))
    #             results = cursor.fetchall()
    #             db_connection.commit()
    #             db_connection.close()

    #     return redirect(url_for("payments"))

    if request.method == "GET":
        return render_template("sc_payment_add.j2")

## Edit Form
@app.route('/payment_edit', methods=['GET'])
def payment_edit():
    return render_template("sc_payment_edit.j2")

# Delete Payment
@app.route("/payment_delete/<int:id>")
def payment_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Payments WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/payments")

# Pieces_Artists CRUD

@app.route('/pieces_artists', methods=['GET'])
def pieces_artists():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Pieces_Artists;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_pieces_artists.j2", Pieces_Artists=results)

## Add Form
@app.route('/piece_artist_add', methods=['GET'])
def piece_artist_add():
    return render_template("sc_piece_artist_add.j2")

## Edit Form
@app.route('/piece_artist_edit', methods=['GET'])
def piece_artist_edit():
    return render_template("sc_piece_artist_edit.j2")

# Delete Piece Artist
@app.route("/piece_artist_delete/<int:id>")
def piece_artist_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Pieces_Artists WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/pieces_artists")

# Pieces CRUD

@app.route('/pieces', methods=['GET'])
def pieces():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Pieces;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_pieces.j2", Pieces=results)

# Add Piece
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
        return render_template("sc_piece_add.j2")

## Edit Form
@app.route('/piece_edit', methods=['GET'])
def piece_edit():
    return render_template("sc_piece_edit.j2")

# Delete Piece
@app.route("/piece_delete/<int:id>")
def piece_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Pieces WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/pieces")

# Sales CRUD

@app.route('/sales', methods=['GET'])
def sales():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Sales;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_sales.j2", Sales=results)

# Add Sale
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
        return render_template("sc_sale_add.j2")

## Edit Form
@app.route('/sale_edit', methods=['GET'])
def sale_edit():
    return render_template("sc_sale_edit.j2")

# Delete Sale
@app.route("/sale_delete/<int:id>")
def sale_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Sales WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/sales")

# Shipments CRUD

@app.route('/shipments', methods=['GET'])
def shipments():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Shipments;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_shipments.j2", Shipments=results)

# Add Shipment
@app.route('/shipment_add', methods=["POST", "GET"])
def shipment_add():
    # if request.method == "POST":
    #     if request.form.get("add_shipment"):
    #         #grab user form inputs
    #         shipped = request.form["shipped"]
    #         delivered = request.form["delivered"]
    #         carrier = request.form["carrier"]
    #         tracking = request.form["tracking"]

    #         # null card_number and exp_date
    #         if tracking == "":
    #             db_connection = db.connect_to_database()
    #             query = "INSERT INTO Shipments (shipped, delivered, carrier) VALUES (%s, %s, %s);"
    #             cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (shipped, delivered, carrier))
    #             results = cursor.fetchall()
    #             db_connection.commit()
    #             db_connection.close()

    #         # no null inputs
    #         else:
    #             db_connection = db.connect_to_database()
    #             query = "INSERT INTO Payments (shipped, delivered, carrier, tracking) VALUES (%s, %s, %s, %s);"
    #             cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (shipped, delivered, carrier, tracking))
    #             results = cursor.fetchall()
    #             db_connection.commit()
    #             db_connection.close()

    #     return redirect(url_for("shipments"))

    if request.method == "GET":
        return render_template("sc_shipment_add.j2")

## Edit Form
@app.route('/shipment_edit', methods=['GET'])
def shipment_edit():
    return render_template("sc_shipment_edit.j2")

# Delete Shipment
@app.route("/shipment_delete/<int:id>")
def shipment_delete(id):
    db_connection = db.connect_to_database()
    query = "DELETE FROM Shipments WHERE id = '%s';"
    cursor = db_connection.cursor()
    cursor.execute(query, (id,))
    db_connection.commit()

    # redirect
    return redirect("/shipments")

### Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4938))
    app.run(port=port, debug=True)