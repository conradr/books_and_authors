from db.run_sql import run_sql


def select_author_by_id():
    pass


def delete_author_by_id():
    pass


def update_author_by_id():
    pass


def insert(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING id"
    values = [author.name]
    run_sql(sql, values)

    return author


def show_all_authors():
    sql = "SELECT * from authors"
    return run_sql(sql)
