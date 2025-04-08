from sqlalchemy.orm import Session
from app import models, schemas


def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()


def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, contact_data: schemas.ContactUpdate):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        for key, value in contact_data.dict(exclude_unset=True).items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact


def delete_contact(db: Session, contact_id: int):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
