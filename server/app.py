from config import app, db, api

from models.author import Author
from models.book import Book
from models.tag import Tag
from models.user import User

from models.book_tag import BookTag
from models.review import Review

from blueprints.books import Books
from blueprints.book_by_id import BookById
from blueprints.authors import Authors
from blueprints.author_by_id import AuthorById
from blueprints.reviews import Reviews
from blueprints.review_by_id import ReviewById
from blueprints.users import Users
from blueprints.user_by_id import UserById
from blueprints.tags import Tags
from blueprints.book_tags import BookTags

api.add_resource(Books, "/books")
api.add_resource(BookById, "/books/<int:id>")
api.add_resource(Authors, "/authors")
api.add_resource(AuthorById, "/authors/<int:id>")
api.add_resource(Reviews, "/reviews")
api.add_resource(ReviewById, "/reviews/<int:id>")
api.add_resource(Users, "/users")
api.add_resource(UserById, "/users/<int:id>")
api.add_resource(Tags, "/tags")
api.add_resource(BookTags, "/book_tags")

if __name__ == "__main__":
    app.run(debug=True, port=5555)