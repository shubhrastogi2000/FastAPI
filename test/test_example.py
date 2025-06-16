import pytest

def test_equal_or_not_equal():
    assert 3!=2
    assert 3==3

def test_is_instance():
    assert isinstance('this is string',str)
    assert not isinstance('10',int)

def test_boolean():
    validated = True
    assert validated is True
    assert ('hello'=='world') is False

def test_type():
    assert type('hello' is str)
    assert type('world' is not int)

def test_gt_ot_lt():
    assert 7>3
    assert 1<2

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False,False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)

class Student:
    def __init__(self,first_name:str,last_name:str,major:str,year:int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year

@pytest.fixture
def default_init():
    return Student('Shubh','Rastogi','CSE',2022)

def test_person_init(default_init):
    # p = Student('Shubh','Rastogi','CSE',2022)
    assert default_init.first_name =='Shubh', 'First Name is Shubh'
    assert default_init.last_name =='Rastogi', 'Last Name is Rastogi'
    assert default_init.major == 'CSE'
    assert default_init.year == 2022