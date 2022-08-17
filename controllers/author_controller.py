from flask import Blueprint, render_template, request, redirect
from repositories import author_repository as ar
from models.author_class import Author

book_blueprint = Blueprint("books", __name__)


@book_blueprint.route('/authors')
def all_authors():
    authors = ar.show_all_authors()
    return render_template('authors/authors_index.html', authors=authors)


@book_blueprint.route('/authors', methods=['POST'])
def new_author():
    author_name = request.form['author_name']
    author = Author(author_name)
    ar.save_author(author)
    authors = ar.show_all_authors()
    return render_template('authors/authors_index.html', authors=authors)


@book_blueprint.route('/authors/<id>', methods=['POST'])
def save_updated_author(id):
    author_name = request.form['author_name']
    author = Author(author_name)
    ar.update_author_by_id(author)
    return render_template('authors/authors_index.html', authors=authors)


@book_blueprint.route('/authors/<id>/update', methods=['GET'])
def update_author(id):
    author = ar.select_author_by_id(id)
    ar.update_author_by_id(author)
    return render_template('authors/authors_edit.html', author=author)


@book_blueprint.route('/authors/new')
def new_task():
    author_list = ar.show_all_authors()
    return render_template('authors/authors_new.html')
