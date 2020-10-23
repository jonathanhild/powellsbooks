-- Copyright (c) 2020 Jonathan Hildenbrand 
-- This software is released under the MIT License. https://opensource.org/licenses/MIT
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    isbn13 TEXT NOT NULL,
    publisher TEXT NOT NULL,
    publication_date TEXT,
    series TEXT,
    series_num INTEGER,
    pages INTEGER,
    avg_customer_rating REAL,
    customer_ratings INTEGER,
    publisher_comment TEXT
);
CREATE TABLE IF NOT EXISTS author(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS author_book(
    author_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES author(id),
    FOREIGN KEY (book_id) REFERENCES book(id)
);
CREATE TABLE IF NOT EXISTS synopsis_review(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    synopsis_type TEXT NOT NULL,
    synopsis_blurb TEXT NOT NULL,
    synopsis_source TEXT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES book(id)
);
CREATE TABLE IF NOT EXISTS reader_review(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(
        rating BETWEEN 0 AND 5
    ),
    review_blurb TEXT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES book(id)
);
CREATE TABLE IF NOT EXISTS staff(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS staff_pick(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    pick_blurb TEXT NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES staff(id),
    FOREIGN KEY (book_id) REFERENCES book(id)
);
CREATE TABLE IF NOT EXISTS top_five(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    staff_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    year INTEGER NOT NULL,
    rank INTEGER NOT NULL,
    FOREIGN KEY (staff_id) REFERENCES staff(id),
    FOREIGN KEY (book_id) REFERENCES book(id)
);