/*
Group: 7
Lauren Graham and Kevin Hayden
Sample data manupulation queries

Including SELECT, INSERT, UPDATE, DELETE

Throughout this document, the colon character (:) is used to 
preceded variables that will have data from the backend 
programming language.

*/


--SELECT

--Search by id and display the information
SELECT * FROM Artists WHERE id == :id;
SELECT * FROM Pieces WHERE id == :id;
SELECT * FROM Mediums WHERE id == :id;
SELECT * FROM Customers WHERE id == :id;
SELECT * FROM Locations WHERE id == :id;
SELECT * FROM Sales where id == :id;
SELECT * FROM Payments WHERE id == :id;
SELECT * FROM Shipments Where id == :id;


-get all artists with their current pieces to list
SELECT artist_id, piece_id, CONCAT(first_name,' ',last_name) AS name, CONCAT(title,', ',year) AS piece
FROM Artists
INNER JOIN artists_pieces ON Artists.id = Artists_Pieces.artist_id
INNER JOIN Pieces ON Pieces.id = Artists.Pieces.piece_id
ORDER BY piece, name ASC


--get all pieces of a certain medium
SELECT id, title
FROM Pieces
WHERE medium_id == :id_from_dropdown
ORDER BY Medium, ASC


--get all artists' data to populate a dropdown for associating with a medium
SELECT artist_id AS id, last_name, first_name FROM Artists
--get all mediums to populate a dropdown for associating with artists
SELECT medium_id AS id, class FROM Mediums


--INSERT

--Add a new artist
INSERT INTO Artists (last_name, first_name, address, city, state, zip, phone) VALUES (:last_name, :first_name, :address, :city, :state, :zip, :phone);

--Add a new piece
INSERT INTO Pieces (location_id, medium_id, title, year) VALUES
(:location_id_from_dropdown, :medium_id_from_dropdown, :title, :year);

--Add a new medium
INSERT INTO Mediums (class) VALUES
(:class);

--Add a new location
INSERT INTO Locations (location, address, city, state, zip) VALUES
(:location, :address, :city, :state, :zip);

--Add a new customer
INSERT INTO Customers (last_name, first_name, address, city, state, zip, phone) VALUES
(:last_name, :first_name, :address, :city, :state_from_dropdown, :zip, :phone);

--Add a new Sale
INSERT INTO Sales (customer_id, piece_id, date, amount, ship) VALUES
(:customer_id_from_dropdown, :piece_id_from_dropdown, :date, :amount, :ship_from_dropdown);

--Add a new Payment
INSERT INTO Payments (sale_id, date, card, cash, check, card_number, exp_date, amount) VALUES
(:sale_id_from_dropdown, :date, :card_from_dropdown, :cash_from_dropdown, :check_from_dropdown, :card_number, :exp_date, :amount);

--Add a new Shipment
INSERT INTO Shipments (sale_id, shipped, delivered, carrier, tracking) VALUES
(:sale_id_from_dropdown, :shipped_from_dropdown, :delivered_from_dropdown, :carrier, :tracking);



--UPDATE

--associate an artist with a piece (M-to-M relationship addition)
INSERT INTO Artists_Pieces (artist_id, piece_id) VALUES
(:artist_id_from_dropdown_menu, :piece_id_from_dropdown_menu)

--dis-associate a piece from an artist (M-to-M relationship deletion)
DELETE FROM Pieces_Artists WHERE artist_id = :artist_id_selected_from_piece_and_artist_list AND piece_id = :piece_id_selected_from_piece_and_artist_list

--update artist info
UPDATE Artists SET last_name = :last_name, first_name = :first_name, address = :address, city = :city, state = :state_from_dropdown, zip = :zip, phone = :phone WHERE id = :artist_id_from_update_form

--update piece info
UPDATE Pieces SET location_id = :location_id_from_dropdown, medium_id = :medium_id_from_dropdown, title = :title, year = :year WHERE id = :piece_id_from_update_form


--update location info
UPDATE Locations SET location = :location, address = :address, city = :city, state = :state_from_dropdown, zip = :zip WHERE id = :location_id_from_update_form

--update customer info
UPDATE Customers Set last_name = :last_name, first_name = :first_name, address = address, city = :city, state = :state_from_dropdown, zip = :zip, phone = :phone WHERE id = :customer_id_from_update_form

--update shipment info
UPDATE Shipments Set sale_id = :sale_id_from_dropdown, shipped = :shipped_from_dropdown, delivered = :delivered_from_dropdown, carrier = :carrier, tracking = :tracking WHERE id = :shipment_id_from_update_form



--DELETE

--delete a piece
DELETE FROM Pieces WHERE id = :piece_id_from_pieces_page

--delete an artist
DELETE FROM Artists WHERE id = :artist_id_from_artists_page

--delete a medium
DELETE FROM Mediums WHERE id = :medium_id_from_mediums_page

--delete a location
DELETE FROM Locations WHERE id = :location_id_from_locations_page

--delete a customer
DELETE FROM Customers WHERE id = :customer_id_from_customers_page

--delete a sale
DELETE FROM Sales WHERE id = :sale_id_from_sales_page

--delete a payment
DELETE FROM Payments WHERE id = :payment_id_from_payments_page

--delete a shipment
DELETE FROM Shipments WHERE id = :shipment_id_from_shipments_page








