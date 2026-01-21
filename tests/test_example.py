import pytest

def test_pass_fail():
    assert 3==3
    assert 3!=2

class Students:
    def __init__(self,first_name : str ,last_name : str ,age : int ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age



# def test_person_initialization():
#     p =Students('John' , 'Doe' , 30 )
#     assert p.first_name == 'John' ,'first name should be john'
#     assert p.last_name == 'Doe' ,'last name should be doe'
#     assert p.age == 30 ,'age should be 30'
#
#

@pytest.fixture
def default_employee():
    return Students('John' , 'Doe' , 30 )


def test_person_initialization(default_employee):
    assert default_employee.first_name == 'John' ,'first name should be john'
    assert  default_employee.last_name == 'Doe' ,'last name should be doe'
    assert default_employee.age == 30 ,'age should be 30'


