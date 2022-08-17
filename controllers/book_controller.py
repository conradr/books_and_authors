from flask import Blueprint, render_template
from repositories import author_repository as ar

book_blueprint = Blueprint("books", __name__)


@book_blueprint.route('/books')
def all_authors():
    authors = ar.show_all_authors()
    return render_template('books/books_index.html', authors=authors)
