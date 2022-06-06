SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


-- Artists
CREATE OR REPLACE TABLE Artists
(
    id INT NOT NULL AUTO_INCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip CHAR(5) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO Artists 
(
    last_name,
    first_name,
    address,
    city,
    state,
    zip,
    phone
)

VALUES
(
    'Rindler',
    'Wolfgang',
    '800 W Campbell Rd',
    'Richardson',
    'TX',
    '75080',
    '8008892443'
),
(
    'Chihuly',
    'Dale',
    '509 NE Northlake Way',
    'Seattle',
    'WA',
    '98105',
    '2067818707'
),
(
    'Jackson',
    'Leslie',
    '509 NE Northlake Way',
    'Seattle',
    'WA',
    '98105',
    '2067818707'
),
(
    'Domont',
    'Jordan',
    '33 NW Park Ave',
    'Portland',
    'OR',
    '97209',
    '5034674909'
);


-- Mediums
CREATE OR REPLACE TABLE Mediums
(
    id INT NOT NULL AUTO_INCREMENT,
    medium VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO Mediums
(
    medium
)

VALUES
(
    'Oil'
),
(
    'Mixed'
),
(
    'Glass'
),
(
    'Digital'
);


-- Locations
CREATE OR REPLACE TABLE Locations
(
    id INT NOT NULL AUTO_INCREMENT,
    location VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip CHAR(5) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO Locations
(
    location,
    address,
    city,
    state,
    zip
)

VALUES
(
    'Studio Cascadia Seattle',
    '519 E Pine St',
    'Seattle',
    'WA',
    '98122'
),
(
    'Studio Cascadia Spokane',
    '1326 E Sprague Ave',
    'Spokane',
    'WA',
    '99202'
),
(
    'Studio Cascadia Portland',
    '22 SW 3rd Ave',
    'Portland',
    'OR',
    '97204'
);

-- Pieces
CREATE OR REPLACE TABLE Pieces 
(
    id INT NOT NULL AUTO_INCREMENT,
    location_id INT,
    medium_id INT,
    title VARCHAR(50) NOT NULL,
    year VARCHAR(50) NOT NULL,
    price DECIMAL NOT NULL,
    available TINYINT NOT NULL,
    hold TINYINT NOT NULL,
    commission TINYINT NOT NULL,
    style VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (location_id) REFERENCES Locations(id) ON DELETE CASCADE,
    FOREIGN KEY (medium_id) REFERENCES Mediums(id) ON DELETE CASCADE
);

INSERT INTO Pieces 
(
    location_id,
    medium_id,
    title,
    year,
    price,
    available,
    hold,
    commission,
    style
)

VALUES
(
    1,
    4,
    'Event Horizon',
    '2019',
    1300.00,
    0,
    0,
    0,
    'Futurism'
),
(
    2,
    3,
    'Flamingo Macchia',
    '2019',
    6000.00,
    0,
    0,
    0,
    'Abstract'
),
(
    2,
    3,
    'Seagrass Seaform',
    '2021',
    8000.00,
    0,
    0,
    0,
    'Abstract'
),
(
    2,
    2,
    'David Lynch',
    '2022',
    4500.00,
    1,
    0,
    0,
    'Portrait'
);

-- Pieces_Artists
CREATE OR REPLACE TABLE Pieces_Artists
(
    id INT NOT NULL AUTO_INCREMENT,
    artist_id INT,
    piece_id INT,
    PRIMARY KEY (id),
    CONSTRAINT FK_Artists_artist_id FOREIGN KEY (artist_id) REFERENCES Artists(id) ON DELETE CASCADE,
    CONSTRAINT FK_Pieces_pieces_id FOREIGN KEY (piece_id) REFERENCES Pieces(id) ON DELETE CASCADE
);

INSERT INTO Pieces_Artists
(
    artist_id,
    piece_id
)

VALUES
(
    1,
    1
),
(
    2,
    2
),
(
    3,
    2
),
(
    2,
    3
);

-- Customers
CREATE OR REPLACE TABLE Customers
(
    id INT NOT NULL AUTO_INCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip CHAR(5) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO Customers
(
    last_name,
    first_name,
    address,
    city,
    state,
    zip,
    phone
)

VALUES
(
    'Graham',
    'Lauren',
    '206 Julian Ave',
    'Honolulu',
    'HI',
    '96818',
    '555-960-8888'
),
(
    'Brownstein',
    'Carrie',
    '3244 NE 46th Ave',
    'Portland',
    'OR',
    '97213',
    '555-438-9999'
),
(
    'McCready',
    'Mike',
    '2708 65th Place SE',
    'Mercer Island',
    'WA',
    '98040',
    '555-545-2222'
);



-- Sales
CREATE OR REPLACE TABLE Sales
(
    id INT NOT NULL AUTO_INCREMENT,
    piece_id INT,
    customer_id INT,
    date DATETIME NOT NULL,
    amount DECIMAL NOT NULL,
    ship TINYINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES Customers(id) ON DELETE CASCADE,
    FOREIGN KEY (piece_id) REFERENCES Pieces(id) ON DELETE CASCADE
);

INSERT INTO Sales
(
    customer_id,
    piece_id,
    date,
    amount,
    ship
)

VALUES
(
    1,
    1,
    '2021-10-31 11:05',
    1300.00,
    1
),
(
    2,
    3,
    '2022-01-23 16:33',
    8000.00,
    1
),
(
    3,
    2,
    '2022-01-23 10:10',
    '6000.00',
    1
);


-- Payments
CREATE OR REPLACE TABLE Payments
(
    id INT NOT NULL AUTO_INCREMENT,
    sale_id INT,
    `date` DATETIME NOT NULL,
    `card` TINYINT NOT NULL,
    cash TINYINT NOT NULL,
    `check` TINYINT NOT NULL,
    card_number VARCHAR(50),
    exp_date DATE,
    amount VARCHAR(50) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (sale_id) REFERENCES Sales(id) ON DELETE CASCADE
);

INSERT INTO Payments
(
    sale_id,
    `date`,
    `card`,
    cash,
    `check`,
    card_number,
    exp_date,
    amount
)

VALUES
(
    1,
    '2021-10-30 14:30',
    0,
    1,
    0,
    NULL,
    NULL,
    1300.00
),
(
    2,
    '2022-01-23 16:30',
    0,
    0,
    1,
    NULL,
    NULL,
    8000.00
),
(
    3,
    '2022-01-23 10:05',
    0,
    0,
    1,
    NULL,
    NULL,
    3000.00
),
(
    3,
    '2022-01-23 10:08',
    0,
    1,
    0,
    NULL,
    NULL,
    3000.00
);


-- Shipments
CREATE OR REPLACE TABLE Shipments
(
    id INT NOT NULL AUTO_INCREMENT,
    sale_id INT,
    shipped TINYINT NOT NULL,
    delivered TINYINT NOT NULL,
    carrier VARCHAR(50) NOT NULL,
    tracking VARCHAR(50),
    PRIMARY KEY (id),
    FOREIGN KEY (sale_id) REFERENCES Sales(id) ON DELETE CASCADE
);

INSERT INTO Shipments
(
    sale_id,
    shipped,
    delivered,
    carrier,
    tracking
)

VALUES
(
    1,
    1,
    1,
    'Prime Hawaiian Movers',
    NULL
),
(
    2,
    1,
    1,
    'FedEx',
    '05218962519602'
),
(
    3,
    1,
    1,
    'FedEx',
    '05227994632790'
);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;
