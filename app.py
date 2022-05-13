from flask import Flask, render_template, json
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
    cursor = db.execute_query(db_connection=db_connection, query=query)  # !!!!!!!!!!!!!!!!!! CAUSES DB BREAK
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
@app.route('/mediums_add', methods=['GET'])
def mediums_add():
    return render_template("sc_mediums_add.j2")

## Edit Form
@app.route('/mediums_edit', methods=['GET'])
def mediums_edit():
    return render_template("sc_mediums_edit.j2")

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
@app.route('/payments_add', methods=['GET'])
def payments_add():
    return render_template("sc_payments_add.j2")

## Edit Form
@app.route('/payments_edit', methods=['GET'])
def payments_edit():
    return render_template("sc_payments_edit.j2")

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
@app.route('/pieces_artists_add', methods=['GET'])
def pieces_artists_add():
    return render_template("sc_pieces_artists_add.j2")

## Edit Form
@app.route('/pieces_artists_edit', methods=['GET'])
def pieces_artists_edit():
    return render_template("sc_pieces_artists_edit.j2")

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
@app.route('/pieces_add', methods=['GET'])
def pieces_add():
    return render_template("sc_pieces_add.j2")

## Edit Form
@app.route('/pieces_edit', methods=['GET'])
def pieces_edit():
    return render_template("sc_pieces_edit.j2")

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
@app.route('/sales_add', methods=['GET'])
def sales_add():
    return render_template("sc_sales_add.j2")

## Edit Form
@app.route('/sales_edit', methods=['GET'])
def sales_edit():
    return render_template("sc_sales_edit.j2")

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
@app.route('/shipments_add', methods=['GET'])
def shipments_add():
    return render_template("sc_shipments_add.j2")

## Edit Form
@app.route('/shipments_edit', methods=['GET'])
def shipments_edit():
    return render_template("sc_shipments_edit.j2")

### Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1177))
    app.run(port=port, debug=True)