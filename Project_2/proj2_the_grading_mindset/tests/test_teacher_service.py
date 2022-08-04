import pytest
import pytest_mock
from service.teacher_service import TeacherService
from exception.login import LoginError
from model.teacher import Teacher


def test_teacher_login_positive(mocker):
    def mock_teacher_login(self, username, password):
        if username == "teacher1" and password == "password1":
            return Teacher(1, "teacher1", "password1", "Teacher One", "teacher1@email.com")
        else:
            return None

    mocker.patch("dao.teacher_dao.TeacherDao.get_teacher_by_username_and_password", mock_teacher_login)
    teacher_service = TeacherService()

    actual = teacher_service.teacher_login("teacher1", "password1")
    assert actual == {
        "password": "password1",
        "t_email": "teacher1@email.com",
        "t_id": 1,
        "t_name": "Teacher One",
        "username": "teacher1"
    }


def test_teacher_login_negative(mocker):
    def mock_teacher_login(self, username, password):
        if username == "teacher1" and password == "password1":
            return Teacher(1, "teacher1", "password1", "Teacher One", "teacher1@email.com")
        else:
            return None

    mocker.patch("dao.teacher_dao.TeacherDao.get_teacher_by_username_and_password", mock_teacher_login)
    teacher_service = TeacherService()

    with pytest.raises(LoginError) as excinfo:
        teacher_service.teacher_login("teacher11", "password11")
    assert str(excinfo.value) == "Invalid username and/or password for teacher"