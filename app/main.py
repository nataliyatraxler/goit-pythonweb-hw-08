from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import contacts

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contacts API")
app.include_router(contacts.router)
