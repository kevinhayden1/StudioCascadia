from flask import Flask, render_template, json, redirect
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

@app.route('/artists', methods=['GET'])
def artists():
    db_connection = db.connect_to_database()
    query = "SELECT * FROM Artists;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    db_connection.close()
    return render_template("sc_artists.j2", Artists=results)

## Add Form
@app.route('/artist_add', methods=['GET'])
def artist_add():
    return render_template("sc_artist_add.j2")

## Edit Form
@app.route('/artist_edit', methods=['GET'])
def artist_edit():
    return render_template("sc_artist_edit.j2")

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
    port = int(os.environ.get('PORT', 4936))
    app.run(port=port, debug=True)