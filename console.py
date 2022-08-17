from models.author_class import Author
from models.books_class import Book
from repositories.author_repository import *
from repositories.books_repository import *

author1 = Author("Joe Mcfee")
book1 = Book("Chamber of Secrets", author1)

save_author(author1)
save_book(book1)

# save_author(author)
