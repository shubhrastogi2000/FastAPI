#reusable code
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from ..database import Base
from ..main import app
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, Users
from ..router.auth import bcrypt_context

# temporary Database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./testdb.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False},
                       poolclass=StaticPool,
                       )
TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base.metadata.create_all(bind = engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# dummy data
def override_get_current_user():
    return {'username':'shubhr263','id':1,"user_role":'admin'}

client = TestClient(app)

@pytest.fixture()
def test_todo():
    todo = Todos(
        title = "Learn FastAPI",
        description = "Learning",
        priority = 5,
        complete = False,
        owner_id = 1
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()

@pytest.fixture
def test_user():
    user = Users(
        username = "shubhr263",
        email = 'shubh@abc.com',
        first_name = 'Shubh',
        last_name = 'Rastogi',
        hashed_password = bcrypt_context.hash("mnb12345"),
        role = 'admin',
        phone_number = '(111)-111-1111'
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()