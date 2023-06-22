from blueprints import Resource, Blueprint, make_response, g, abort 
from models import db
from models.book import Book

books_bp = Blueprint("books", __name__, url_prefix="/books")

class Books(Resource):
    def get(self): 
        books = [b.to_dict() for b in Book.query.all()]
        return make_response(books, 200)