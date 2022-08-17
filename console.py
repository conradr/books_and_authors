from models.author_class import Author
from repositories.author_repository import insert

author = Author("Peter Pan")

insert(author)
