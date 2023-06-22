from config import app, db, api

from models.author import Author
from models.book import Book
from models.tag import Tag
from models.user import User

from models.book_tag import BookTag
from models.review import Review

from blueprints.books import Books

api.add_resource(Books, "/books")

if __name__ == "__main__":
    app.run(debug=True, port=5555)