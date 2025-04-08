# Contacts API with FastAPI, PostgreSQL, and SQLAlchemy

This project is a simple RESTful API for managing contacts. It is built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, and includes basic CRUD functionality. The project also demonstrates how to seed the database with test data using a script.

---

## 🚀 Features

- Create, read, update, and delete (CRUD) contacts
- View interactive API documentation with Swagger UI
- Store and manage data in a PostgreSQL database
- Clean and modular project structure
- Simple test data seeding script

---

## 🛠 Tech Stack

- **FastAPI** — modern Python web framework
- **SQLAlchemy** — ORM for database interactions
- **PostgreSQL** — relational database
- **Pydantic** — data validation
- **Uvicorn** — ASGI server
- **Faker** — for generating test data

---

## 📁 Project Structure

```
goit-pythonweb-hw-08/
├── app/
│   ├── __init__.py
│   ├── main.py              # App entry point
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # CRUD operations
│   ├── database.py          # DB engine and session
│   └── routers/
│       └── contacts.py      # API routes for contacts
├── scripts/
│   └── add_dummy_contacts.py  # Add test contacts
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run the Project

### 1. Clone the repo

```bash
git clone https://github.com/nataliyatraxler/goit-pythonweb-hw-08.git
cd goit-pythonweb-hw-08
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Make sure PostgreSQL is running and a database named `contacts_db` exists:

```bash
createdb contacts_db
```

Grant access to user `fastapi_user` or update `DATABASE_URL` in `database.py`:

```python
DATABASE_URL = "postgresql://fastapi_user:mysecret@localhost/contacts_db"
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs) to access Swagger UI.

---

## 🧪 Add Dummy Contacts

You can seed the database with 5 fake contacts:

```bash
PYTHONPATH=. python scripts/add_dummy_contacts.py
```

---

## 📮 API Endpoints

| Method | Endpoint         | Description          |
| ------ | ---------------- | -------------------- |
| GET    | `/contacts/`     | Get all contacts     |
| GET    | `/contacts/{id}` | Get a contact by ID  |
| POST   | `/contacts/`     | Create a new contact |
| PUT    | `/contacts/{id}` | Update a contact     |
| DELETE | `/contacts/{id}` | Delete a contact     |

---

## 🧼 Example Contact JSON

```json
{
  "first_name": "Alice",
  "last_name": "Johnson",
  "email": "alice.johnson@example.com",
  "phone": "+1234567890",
  "birthday": "1990-05-15"
}
```

---

## 🧑‍🏫 Author

Nataliya Traxler

---

## 📝 License

MIT License. Use it freely for learning or as a boilerplate.
