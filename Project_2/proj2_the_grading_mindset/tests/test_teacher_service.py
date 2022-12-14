import pytest
import pytest_mock
from service.teacher_service import TeacherService
from exception.login import LoginError
from model.teacher import Teacher
import exception.teacher_errors as te


def test_t_login_positive(mocker):
    def mock_t_login(self, username, password):
        if username == "teacher1" and password == "password1":
            return Teacher(1, "teacher1", "password1", "Teacher One", "teacher1@email.com")
        else:
            return None

    mocker.patch("dao.teacher_dao.TeacherDao.get_t_by_username_and_password", mock_t_login)
    teacher_service = TeacherService()

    actual = teacher_service.t_login("teacher1", "password1")
    assert actual == {
        "password": "password1",
        "t_email": "teacher1@email.com",
        "t_id": 1,
        "t_name": "Teacher One",
        "username": "teacher1"
    }


def test_t_login_negative(mocker):
    def mock_t_login(self, username, password):
        if username == "teacher1" and password == "password1":
            return Teacher(1, "teacher1", "password1", "Teacher One", "teacher1@email.com")
        else:
            return None

    mocker.patch("dao.teacher_dao.TeacherDao.get_t_by_username_and_password", mock_t_login)
    teacher_service = TeacherService()

    with pytest.raises(LoginError) as excinfo:
        teacher_service.t_login("teacher11", "password11")
    assert str(excinfo.value) == "Invalid username and/or password for teacher"

def test_get_t_by_id_positive(mocker):
    def mock_get_t_by_id(self, t_id):
        if t_id == "1":
            return Teacher(1, "teacher1", "password1", "Teacher One", "teacher1@email.com")
        else:
            return None
    mocker.patch("dao.teacher_dao.TeacherDao.get_t_by_id", mock_get_t_by_id)
    teacher_service = TeacherService()
    actual = teacher_service.get_t_by_id("1")
    assert actual == {
        "password": "password1",
        "t_email": "teacher1@email.com",
        "t_id": 1,
        "t_name": "Teacher One",
        "username": "teacher1"
    }

def test_get_t_by_id_negative(mocker):
    def mock_get_t_by_id(self, t_id):
        if t_id == "1":
            return Teacher(1, "student1", "password1", "Student One", "student1@email.com")
        else:
            return None
    mocker.patch("dao.teacher_dao.TeacherDao.get_t_by_id", mock_get_t_by_id)
    teacher_service = TeacherService()
    with pytest.raises(te.TeacherNotFoundError) as excinfo:
        teacher_service.get_t_by_id("1000")
    assert str(excinfo.value) == "Teacher with the id 1000 was not found"
