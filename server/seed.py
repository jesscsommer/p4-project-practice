from faker import Faker
from random import randint, choice as rc

from config import app, db

from models.author import Author
from models.book import Book
from models.tag import Tag
from models.user import User

from models.book_tag import BookTag
from models.review import Review

fake = Faker()

with app.app_context(): 

    print("Deleting all records ...")

    Author.query.delete()
    Book.query.delete()
    Tag.query.delete()
    User.query.delete()

    BookTag.query.delete()
    Review.query.delete()

    # Creating initial tables 

    print("Creating authors ...")
    authors = []
    for _ in range(10):
        author = Author(
            name=fake.name(),
            bio=fake.paragraph()
        )

        authors.append(author)
    db.session.add_all(authors)

    print("Creating books ...")
    books = []
    genres = ["Poetry", "Fantasy", "Historical Fiction", "Memoir", 
                "Literary Fiction", "Horror", "Drama"]
    for _ in range(20):
        book = Book(
            title=fake.sentence(nb_words=3), 
            genre=rc(genres),
            description=fake.paragraph(),
            bio=fake.paragraph()
        )
        book.author = rc(authors)
        books.append(book)
    
    db.session.add_all(books)

    print("Creating tags ...")
    tags = []
    for _ in range(10): 
        tag = Tag(
            name=fake.sentence(nb_words=1)
        )
        tags.append(tag)
    
    db.session.add_all(tags)

    print("Creating users ...")
    users = []
    usernames = []

    for _ in range(15):
        username = fake.first_name()
        while username in usernames:
            username = fake.first_name()
        usernames.append(username)

        user = User(
            username=username
        )
        user.password_hash = user.userame + "password"

        users.append(user)

    db.session.add_all(users)

    # Creating join tables 
    print("Creating book_tags ...")
    book_tags = []

    for _ in range(50):
        book_tag = BookTag(
            book=rc(books),
            tag=rc(tags)
        )
        book_tags.append(book_tag)
    
    db.session.add_all(book_tags)

    print("Creating reviews ...")
    reviews = []
    
    for _ in range(50):
        review = Review(
            rating=randint(0,5),
            comment=fake.paragraph(),
            book=rc(books),
            user=rc(users)
        )
        reviews.append(review)

    db.session.add_all(reviews)

    print("Committing to db ...")
    
    db.session.commit()

    print("Complete")
