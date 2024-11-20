CREATE TABLE IF NOT EXISTS guests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    arrival_date TEXT NOT NULL,
    departure_date TEXT NOT NULL,
    room_number INTEGER,
    phone_number TEXT
);

