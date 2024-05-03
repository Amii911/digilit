# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from models import User


def seed():
    # delete current data
    User.query.delete()
    
    # create admin user for testing and debugging
    admin = User(username="admin", admin=True)
    admin.password_hash = 'admin'

    db.session.add(admin)
    db.session.commit()

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
