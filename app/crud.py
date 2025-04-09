from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas

def create_contact(db: Session, contact: schemas.ContactCreate):
    """Create and store a new contact in the database."""
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    """Retrieve a list of contacts with optional pagination."""
    return db.query(models.Contact).offset(skip).limit(limit).all()


def get_contact(db: Session, contact_id: int):
    """Retrieve a single contact by ID."""
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, contact_data: schemas.ContactUpdate):
    """Update an existing contact by ID."""
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        return None

    for key, value in contact_data.dict(exclude_unset=True).items():
        setattr(contact, key, value)
    db.commit()
    db.refresh(contact)
    return contact


def delete_contact(db: Session, contact_id: int):
    """Delete a contact by ID."""
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        return None
    db.delete(contact)
    db.commit()
    return True


def search_contacts(db: Session, query: str):
    """Search contacts by first name, last name, or email (case-insensitive)."""
    return db.query(models.Contact).filter(
        (models.Contact.first_name.ilike(f"%{query}%")) |
        (models.Contact.last_name.ilike(f"%{query}%")) |
        (models.Contact.email.ilike(f"%{query}%"))
    ).all()


def get_upcoming_birthdays(db: Session):
    """Get contacts whose birthdays fall within the next 7 days, including leap year handling."""
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    contacts = db.query(models.Contact).all()

    upcoming = []
    for contact in contacts:
        try:
            bday = contact.birthday.replace(year=today.year)
        except ValueError:
            # Handle 29 February for non-leap years
            bday = contact.birthday.replace(year=today.year, day=28)

        if today <= bday <= next_week:
            upcoming.append(contact)

    return upcoming
