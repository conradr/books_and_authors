
from db.run_sql import run_sql
from models.books_class import Book
from repositories.author_repository import select_author_by_id


def select_book_by_id(id):
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    query_result = run_sql(sql, values)[0]
    book = Book(query_result["name"], select_author_by_id(query_result["author_id"]), query_result["id"])
    print(book.__dict__)
    return book


def select_all_books_from_author(author):
    sql = "SELECT * FROM books WHERE author_id = %s"
    values = [author.id]
    query_result = run_sql(sql, values)
    book_list = []
    for result in query_result:
        book_list.append(Book(result["name"], author, result["id"]))
    return book_list


def delete_book(book):
    sql = "DELETE FROM books WHERE id = %s"
    values = [book.book_id]
    run_sql(sql, values)


def update_book(book):
    sql = "UPDATE books SET name = %s, author_id = %s WHERE id = %s"
    values = [book.name, book.author.id, book.book_id]
    run_sql(sql, values)


def insert_book(book):
    sql = "INSERT INTO books (name, author_id) VALUES (%s, %s) RETURNING id"
    values = [book.name, book.author.id]
    run_sql(sql, values)


def show_all_books():
    sql = "SELECT * FROM books"
    books = run_sql(sql)
    list_output = []
    for book in books:
        book = Book(book['name'], select_author_by_id(book['author_id']), id=book["id"])
        list_output.append(book)
    return list_output
