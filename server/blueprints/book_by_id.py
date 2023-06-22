from blueprints import Resource, Blueprint, make_response, g, abort 
from models import db
from models.book import Book

class BookById(Resource):
    def get(self):
        return "Book by id!"