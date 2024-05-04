# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User


with app.app_context():
    # delete current data
    User.query.delete()
    db.session.commit()

    # Seed users
    users = []

    user1 = User(username='Amii1234', _password_hash='testprettytest')
    users.append(user1)

    user2 = User(username='Amyy5678', _password_hash='tetest')
    users.append(user2)

    db.session.add_all(users)
    db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
