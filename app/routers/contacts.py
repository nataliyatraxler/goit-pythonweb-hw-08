from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from datetime import datetime, timedelta

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.post("/", response_model=schemas.ContactResponse)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

@router.get("/", response_model=list[schemas.ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    return db.query(models.Contact).all()

@router.get("/{contact_id}", response_model=schemas.ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    return {"message": "Contact deleted"}

# ✅ 🔍 Поиск по имени, фамилии или email
@router.get("/search/", response_model=list[schemas.ContactResponse])
def search_contacts(
    query: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    results = db.query(models.Contact).filter(
        (models.Contact.first_name.ilike(f"%{query}%")) |
        (models.Contact.last_name.ilike(f"%{query}%")) |
        (models.Contact.email.ilike(f"%{query}%"))
    ).all()

    if not results:
        raise HTTPException(status_code=404, detail="No contacts found")

    return results

# 🎂 Список контактов с ближайшими днями рождения
@router.get("/upcoming-birthdays/", response_model=list[schemas.ContactResponse])
def get_upcoming_birthdays(db: Session = Depends(get_db)):
    today = datetime.today().date()
    upcoming = today + timedelta(days=7)

    contacts = db.query(models.Contact).all()
    result = []

    for contact in contacts:
        bday = contact.birthday.replace(year=today.year)
        if today <= bday <= upcoming:
            result.append(contact)

    return result
