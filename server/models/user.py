from sqlalchemy.ext.hybrid import hybrid_property

from __init__ import db, validates, SerializerMixin
from config import bcrypt

class User(db.Model, SerializerMixin):
    pass