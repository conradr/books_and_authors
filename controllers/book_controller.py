from flask import Blueprint, render_template, request, redirect
from repositories import author_repository as ar
from repositories import books_repository as br
from models.books_class import Book

book_blueprint = Blueprint("books", __name__)


@book_blueprint.route('/books')
def all_books():
    books = br.show_all_books()
    return render_template('books/books_index.html', books=books)

@book_blueprint.route("/books/edit_book/<int:id>")
def edit_book(id):
    book_to_update = br.select_book_by_id(id)
    return render_template("books/books_update.html", book = book_to_update)



@book_blueprint.route("/books/author/<int:id>")
def books_by_author(id):
    author = br.select_author_by_id(id)
    books_from_author = br.select_all_books_from_author(author)
    return render_template("books/books_by_author.html", books = books_from_author, author = author)


@book_blueprint.route("/books/author/<int:id>/new_book", methods = ["GET"])
def new_book_by_author_get(id):
    author = br.select_author_by_id(id)
    new_book = request.form
    return render_template("books/books_new.html", author = author)
    
@book_blueprint.route("/books/author/<int:id>/new_book", methods = ["POST"])
def new_book_by_author_post(id):
    new_book = Book(request.form["book_name"], br.select_author_by_id(id))
    br.insert_book(new_book)
    return redirect(f"/books/author/{id}")
    