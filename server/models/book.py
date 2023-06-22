from .__init__ import db, validates, SerializerMixin

class Book(db.Model, SerializerMixin):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    #add a validation for genre (approved / acceptable list)
    avg_rating = db.Column(db.Integer)
    description = db.Column(db.String)

    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    author = db.relationship("Author", back_populates="books")

    reviews = db.relationship("Review", back_populates="book", cascade="all, delete-orphan")
    book_tags = db.relationship("BookTag", back_populates="book", cascade="all, delete-orphan")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    serialize_only=('id', 'title', 'genre', 'author')
    serialize_rules=('-reviews.book', '-book_tags.book', '-author.books')

    def __repr__(self):
        return (
            f"Book #{self.id}:"
            + f"Title: {self.title}"
            + f"Author: {self.author}"
        )
    