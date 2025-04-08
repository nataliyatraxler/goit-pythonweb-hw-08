from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import date

from app import models, schemas, crud
from app.database import get_db

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.post("/", response_model=schemas.ContactResponse)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)


@router.get("/", response_model=List[schemas.ContactResponse])
def get_contacts(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    first_name: Optional[str] = Query(None),
    last_name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
    birthday: Optional[date] = Query(None)
):
    query = db.query(models.Contact)

    if first_name:
        query = query.filter(models.Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(models.Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.filter(models.Contact.email.ilike(f"%{email}%"))
    if birthday:
        query = query.filter(models.Contact.birthday == birthday)

    return query.offset(skip).limit(limit).all()


@router.get("/{contact_id}", response_model=schemas.ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/{contact_id}", response_model=schemas.ContactResponse)
def update_contact(
    contact_id: int, contact_data: schemas.ContactUpdate, db: Session = Depends(get_db)
):
    contact = crud.update_contact(db, contact_id, contact_data)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    crud.delete_contact(db, contact_id)
    return {"message": "Contact deleted"}
