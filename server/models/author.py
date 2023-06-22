from .__init__ import db, validates, SerializerMixin

class Author(db.Model, SerializerMixin):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)

    books = db.relationship("Book", back_populates="author", cascade='all, delete-orphan')

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return (
            f"Author #{self.id}:"
            + f"Name: {self.name}"
        )