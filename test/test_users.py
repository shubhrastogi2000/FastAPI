from Scripts.bottle import response

from .utils import *
from ..router.users import get_db, get_current_user
from fastapi import status
from ..models import Users

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username']=='shubhr263'
    assert response.json()['email'] == 'shubh@abc.com'
    assert response.json()['first_name'] == 'Shubh'
    assert response.json()['last_name'] == 'Rastogi'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(111)-111-1111'

def test_change_password_invalid_success(test_user):
    response = client.put("/user/password",json = {"password":"mnb12345", "new_password":"mnb123456"})
    assert response.status_code == 204

def test_change_password_success(test_user):
    response = client.put("/user/password",json = {"password":"qwerty", "new_password":"mnb123456"})
    assert response.status_code == 401
    assert response.json() == {'detail':'Error on password change'}

def test_change_phone(test_user):
    response = client.put("/user/phonenumber/2222222222")
    assert response.status_code == 204


