import sys
import os
from faker import Faker
from datetime import datetime
from random import randint

# Add the parent directory to the path so we can import from 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal  # Import the DB session
from app.models import Contact         # Import the Contact model

# Initialize Faker instance to generate dummy data
fake = Faker()

def add_dummy_contacts(n=5):
    """
    Add n fake contacts to the database using Faker.
    """
    db = SessionLocal()  # Create a new DB session
    for _ in range(n):
        # Create a fake contact
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            birthday=fake.date_of_birth(minimum_age=20, maximum_age=50)
        )
        db.add(contact)  # Add contact to the session
    db.commit()  # Commit all changes to the DB
    db.close()   # Close the session
    print(f"✅ {n} test contacts added.")

if __name__ == "__main__":
    add_dummy_contacts()
