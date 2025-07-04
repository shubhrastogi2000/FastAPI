from ..router.todos import get_db, get_current_user
from fastapi import status
from ..models import Todos
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

# ------------GET TODOS -----------
def test_read_all_auth(test_todo):
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'complete':False,'title':'Learn FastAPI','description':'Learning','id':1,'priority':5,'owner_id':1}]


def test_read_one_auth(test_todo):
    response = client.get("/todos/todo/1")    #("/todo/{todo_id}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'complete': False, 'title': 'Learn FastAPI', 'description': 'Learning', 'id': 1, 'priority': 5, 'owner_id': 1}

def test_read_one_auth_not_found():
    response = client.get("/todos/todo/999")
    assert response.status_code == 404
    assert response.json() == {'detail':'Todo not found'}

#----------- CREATING TODO TEST ------------------
def test_create_todo(test_todo):
    request_data = {
        'title':'New Todo',
        'description' : 'String',
        'priority':5,
        'complete':False
        # 'owner_id':1
    }

    response = client.post("/todos/todo",json = request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id==2).first()
    assert model.title == request_data.get('title')
    assert model.description == request_data.get('description')
    assert model.priority == request_data.get('priority')
    assert model.complete == request_data.get('complete')

# ------------UPDATE TODOS----------
def test_update_todos(test_todo):
    request_data = {
        'title':'Updated Title',
        'description': 'Updated Desc',
        'priority':3,
        'complete':False
    }

    response = client.put("/todos/todo/1",json = request_data)
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id==1).first()
    assert model.title == request_data.get('title')
    assert model.description == 'Updated Desc'

def test_update_todos_not_found(test_todo):
    request_data = {
        'title':'Updated Title',
        'description': 'Updated Desc',
        'priority':3,
        'complete':False
    }

    response = client.put("/todos/todo/999",json = request_data)
    assert response.status_code == 404
    assert response.json() == {'detail':'Todo Not Found'}


# ---------DELETE TODO -----------
def test_delete_todo(test_todo):
    response = client.delete("/todos/todo/1")
    assert response.status_code == 204
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id==1).first()
    assert model is None

def test_delete_todo_not_found(test_todo):
    response = client.delete("/todos/todo/999")
    assert response.status_code == 404
    assert response.json() == {'detail':'Todo Not Found'}