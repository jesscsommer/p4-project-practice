from sqlalchemy.ext.hybrid import hybrid_property

from __init__ import db, validates, SerializerMixin, association_proxy
from config import bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)

    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")
    books = association_proxy("reviews", "book")

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # add password logic 
    
    def __repr__(self):
        return (
            f"User #{self.id}: {self.username}"
        )