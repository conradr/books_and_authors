from flask import Blueprint, render_template
from repositories import author_repository as ar
from repositories import books_repository as br

book_blueprint = Blueprint("books", __name__)


@book_blueprint.route('/books')
def all_books():
    books = br.show_all_books()
    return render_template('books/books_index.html', books=books)
