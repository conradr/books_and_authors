from db.run_sql import run_sql


def insert(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING id"
    values = [author.name]
    run_sql(sql, values)

    return author


def show_all_authors():
    sql = "SELECT * from authors"
    return run_sql(sql)
