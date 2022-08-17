DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;


CREATE TABLE authors (
    name VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id)
);