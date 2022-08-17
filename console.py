from models.author_class import Author
from models.books_class import Book
from repositories.author_repository import select_author_by_id, save_author
from repositories.books_repository import insert_book, select_book_by_id, select_all_books_from_author_by_author_id, delete_book, update_book

author = Author("Peter Pan")
save_author(author)


# insert(author)
book = select_book_by_id(1)
insert_book(Book("High as a kite",author))
book.name = "OOOOH MY GAAAWD"
books_by_author = select_all_books_from_author_by_author_id(1)
update_book(book)
updated_book = select_book_by_id(1)

print(updated_book.__dict__)
