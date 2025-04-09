from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/contacts", tags=["Contacts"])

#  Create contact
@router.post("/", response_model=schemas.ContactResponse)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)

#  Get all contacts
@router.get("/", response_model=list[schemas.ContactResponse])
def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_contacts(db, skip=skip, limit=limit)

#  Get contact by ID
@router.get("/{contact_id}", response_model=schemas.ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

#  Update contact
@router.put("/{contact_id}", response_model=schemas.ContactResponse)
def update_contact(contact_id: int, contact: schemas.ContactUpdate, db: Session = Depends(get_db)):
    updated = crud.update_contact(db, contact_id, contact)
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated

#  Delete contact
@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_contact(db, contact_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted"}

#  Search contacts
@router.get("/search/", response_model=list[schemas.ContactResponse])
def search_contacts(query: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    results = crud.search_contacts(db, query)
    if not results:
        raise HTTPException(status_code=404, detail="No contacts found")
    return results

#  Upcoming birthdays
@router.get("/upcoming-birthdays/", response_model=list[schemas.ContactResponse])
def get_upcoming_birthdays(db: Session = Depends(get_db)):
    return crud.get_upcoming_birthdays(db)
