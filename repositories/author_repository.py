from db.run_sql import run_sql
from models.author_class import Author
from models.books_class import Book


def select_author_by_id(id):
    author = None
    sql = "SELECT * from authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['name'], result['id'])
        print(author.name)
        return author


def delete_author_by_id(id):
    sql = "DELETE FROM authors WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update_author_by_id(author):
    sql = "UPDATE authors SET (name) = (%s) WHERE id = %s"
    values = [author.name, author.id]
    run_sql(sql, values)


def save_author(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING id"
    values = [author.name]
    results = run_sql(sql, values)
    author_id = results[0]['id']
    author.id = author_id
    return author


def show_all_authors():
    sql = "SELECT * from authors"
    return run_sql(sql)


def authors_books(author):
    books = []
    sql = "SELECT * from authors WHERE id = %s"
    values = [author.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['book.name'], row['author.id'],
                    row['book.id'], row['id'])
        books.append(book)
    return books
