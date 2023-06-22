from __init__ import db, validates, SerializerMixin

class BookTag(db.Model, SerializerMixin):
    __tablename__ = "book_tags"

    id = db.Column(db.Integer, primary_key=True)
    # unique columns

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))

    book = db.relationship("Book", back_populates="book_tags")
    tag = db.relationship("Tag", back_populates="book_tags")

    def __repr__(self):
        return (
            f"BookTag #{self.id}:"
            + f"Book: {self.book.title}"
            + f"Tag: {self.tag.name}"
        )