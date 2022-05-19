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

@app.route('/artist_add', methods=["POST", "GET"])
def artist_add():
    if request.method == "POST":
        if request.form.get("add_artist"):
            #grab user form inputs
            print("Here")
            lname = request.form["last_name"]
            fname = request.form["first_name"]
            address = request.form["address"]
            city = request.form["city"]
            state = request.form["state"]
            zip = request.form["zip"]
            phone = request.form["phone"]
            print(lname)
            db_connection = db.connect_to_database()
            query = "INSERT INTO Artists (last_name, first_name, address, city, state, zip, phone) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor = db.execute_query(db_connection=db_connection, query=query, query_params = (lname, fname, address, city, state, zip, phone))
            results = cursor.fetchall()
            print(results)
            db_connection.commit()
            db_connection.close()
        return redirect(url_for("artists"))

    if request.method == "GET":
        return render_template("sc_artist_add.j2")

# Edit Artist

@app.route("/artist_edit/<int:id>", methods=["POST", "GET"])
def artist_edit(id):
    if request.method == "GET":
        db_connection = db.connect_to_database()

        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Artists WHERE id = %s" % (id)
        cursor = db_connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        # mySQL query to grab data for dropdowns
        query2 = "SELECT id, last_name FROM Artists"
        cursor = db_connection.cursor()
        cursor.execute(query2)
        artist_data = cursor.fetchall()

        db_connection.close()

        # render artist_edit page passing our query data and artist data to the artist_edit template
        return render_template("sc_artist_edit.j2", data=data, artists=artist_data)

    if request.method == "POST":
        if request.form.get("artist_edit"):

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

            query = "UPDATE Artists SET id = %s, last_name = %s, first_name = %s, address = %s, city = %s, state = %s, zip = %s, phone=%s WHERE Artists.id = %s"
            cur = db_connection.cursor()
            cur.execute(query, (id, lname, fname, address, city, state, zip, phone))
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

## Add Form
@app.route('/customer_add', methods=['GET'])
def customer_add():
    return render_template("sc_customer_add.j2")

## Edit Form
@app.route('/customer_edit', methods=['GET'])
def customer_edit():
    return render_template("sc_customer_edit.j2")

# Locations CRUD

@app.route('/locations', methods=['GET'])
def locations():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Locations;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_locations.j2", Locations=results)

## Add Form
@app.route('/location_add', methods=['GET'])
def location_add():
    return render_template("sc_location_add.j2")

## Edit Form
@app.route('/location_edit', methods=['GET'])
def location_edit():
    return render_template("sc_location_edit.j2")

# Mediums CRUD

@app.route('/mediums', methods=['GET'])
def mediums():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Mediums;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_mediums.j2", Mediums=results)

## Add Form
@app.route('/medium_add', methods=['GET'])
def medium_add():
    return render_template("sc_medium_add.j2")

## Edit Form
@app.route('/medium_edit', methods=['GET'])
def medium_edit():
    return render_template("sc_medium_edit.j2")

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
@app.route('/payment_add', methods=['GET'])
def payment_add():
    return render_template("sc_payment_add.j2")

## Edit Form
@app.route('/payment_edit', methods=['GET'])
def payment_edit():
    return render_template("sc_payment_edit.j2")

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

# Pieces CRUD

@app.route('/pieces', methods=['GET'])
def pieces():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Pieces;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_pieces.j2", Pieces=results)

## Add Form
@app.route('/piece_add', methods=['GET'])
def piece_add():
    return render_template("sc_piece_add.j2")

## Edit Form
@app.route('/piece_edit', methods=['GET'])
def piece_edit():
    return render_template("sc_piece_edit.j2")

# Sales CRUD

@app.route('/sales', methods=['GET'])
def sales():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Sales;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_sales.j2", Sales=results)

## Add Form
@app.route('/sale_add', methods=['GET'])
def sale_add():
    return render_template("sc_sale_add.j2")

## Edit Form
@app.route('/sale_edit', methods=['GET'])
def sale_edit():
    return render_template("sc_sale_edit.j2")

# Shipments CRUD

@app.route('/shipments', methods=['GET'])
def shipments():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Shipments;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_shipments.j2", Shipments=results)

## Add Form
@app.route('/shipment_add', methods=['GET'])
def shipment_add():
    return render_template("sc_shipment_add.j2")

## Edit Form
@app.route('/shipment_edit', methods=['GET'])
def shipment_edit():
    return render_template("sc_shipment_edit.j2")

### Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4937))
    app.run(port=port, debug=True)