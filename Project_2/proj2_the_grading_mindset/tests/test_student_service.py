import pytest
import pytest_mock
from service.student_service import StudentService
from exception.login import LoginError
from model.student import Student


def test_s_login_positive(mocker):
    def mock_s_login(self, username, password):
        if username == "student1" and password == "password1":
            return Student(1, "student1", "password1", "Student One", "student1@email.com")
        else:
            return None
    mocker.patch("dao.student_dao.StudentDao.get_s_by_username_and_password", mock_s_login)
    student_service = StudentService()

    actual = student_service.s_login("student1", "password1")
    assert actual == {
        "password": "password1",
        "s_email": "student1@email.com",
        "s_id": 1,
        "s_name": "Student One",
        "username": "student1"
    }


def test_s_login_negative(mocker):
    def mock_s_login(self, username, password):
        if username == "student1" and password == "password1":
            return Student(1, "student1", "password1", "Student One", "student1@email.com")
        else:
            return None

    mocker.patch("dao.student_dao.StudentDao.get_s_by_username_and_password", mock_s_login)
    student_service = StudentService()

    with pytest.raises(LoginError) as excinfo:
        student_service.s_login("student11", "password11")
    assert str(excinfo.value) == "Invalid username and/or password for student"
