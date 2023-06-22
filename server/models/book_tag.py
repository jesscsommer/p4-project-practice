from __init__ import db, validates, SerializerMixin

class BookTag(db.Model, SerializerMixin):
    __tablename__ = "book_tags"

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))