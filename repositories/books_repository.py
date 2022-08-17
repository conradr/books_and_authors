from db.run_sql import run_sql


def select_book_by_id():
    pass


def delete_book_by_id():
    pass


def update_book_by_id():
    pass


def save_book(book):
    # sql = "INSERT INTO books (name, author_id) VALUES (%s %s) RETURNING id"
    # values = [book.name, book.author.id]
    # results = run_sql(sql, values)
    # id = results[0]['id']
    # book.id = id
    # return book


def show_all_books():
    sql = "SELECT * from authors"
    return run_sql(sql)
