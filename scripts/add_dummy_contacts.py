import sys
import os
from faker import Faker
from datetime import datetime
from random import randint


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal 
from app.models import Contact         


fake = Faker()

def add_dummy_contacts(n=5):
    """
    Add n fake contacts to the database using Faker.
    """
    db = SessionLocal() 
    for _ in range(n):
        
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.phone_number(),
            birthday=fake.date_of_birth(minimum_age=20, maximum_age=50)
        )
        db.add(contact)  
    db.commit()  
    db.close()   
    print(f"✅ {n} test contacts added.")

if __name__ == "__main__":
    add_dummy_contacts()
