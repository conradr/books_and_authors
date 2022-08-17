from db.run_sql import run_sql


def insert(book):
    sql = "INSERT INTO books (name, author) VALUES (%s %s) RETURNING id"
    values = [books.name, author]
    run_sql(sql, values)

    return book


def show_all_authors():
    sql = "SELECT * from authors"
    return run_sql(sql)
