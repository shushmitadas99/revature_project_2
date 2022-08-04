import pytest
import pytest_mock
from dotenv import dotenv_values
import model.course as course
from model.student import Student
from service.student_service import StudentService
from service.course_service import CourseService
from exception.student_errors import StudentNotFoundError

config = dotenv_values(".env")

def test_get_all_cs_by_s_id_positive_multiple(mocker):
    # def mock_get_s_by_id(self, s_id):
    #     if s_id == "2":
    #         return Student(2, "student2", "password2", "Student Two", "student2@email.com")
    #     else:
    #         return None
    # mocker.patch("dao.student_dao.StudentDao.get_s_by_id", mock_get_s_by_id)
    # student_service = StudentService()
    # actual = student_service.get_s_by_id("2")
    # assert actual == {
    #     "password": "password2",
    #     "s_email": "student2@email.com",
    #     "s_id": 2,
    #     "s_name": "Student Two",
    #     "username": "student2"
    # }
    def mock_get_all_cs_by_s_id(self, s_id):
        return [course.SCourse('teacher1', 'teacher1@email.com', 'science', 'chemistry'),
                course.SCourse('teacher2', 'teacher2@email.com', 'math', 'algebra')]
    mocker.patch('dao.course_dao.CourseDao.get_all_cs_by_s_id', mock_get_all_cs_by_s_id)
    course_service = CourseService()
    actual = course_service.get_all_cs_by_s_id(s_id=2)
    assert actual == [
        {
            "t_name": 'teacher1',
            "t_email": 'teacher1@email.com',
            "c_name": 'science',
            "c_desc": 'chemistry',
        },
        {
            "t_name": 'teacher2',
            "t_email": 'teacher2@email.com',
            "c_name": 'math',
            "c_desc": 'algebra',
        }
    ]

def test_get_all_cs_by_s_id_positive_single(mocker):
    def mock_get_all_cs_by_s_id(self, s_id):
        return [course.SCourse('teacher1', 'teacher1@email.com', 'science', 'chemistry')]

    mocker.patch('dao.course_dao.CourseDao.get_all_cs_by_s_id', mock_get_all_cs_by_s_id)
    course_service = CourseService()
    actual = course_service.get_all_cs_by_s_id(s_id=1)
    assert actual == [
        {
            "t_name": 'teacher1',
            "t_email": 'teacher1@email.com',
            "c_name": 'science',
            "c_desc": 'chemistry',
        }
    ]

def test_get_all_cs_by_s_id_negative(mocker):
    def mock_get_s_by_id(self, s_id):
        if s_id == "1":
            return Student(1, "student1", "password1", "Student One", "student1@email.com")
        else:
            return None
    mocker.patch("dao.student_dao.StudentDao.get_s_by_id", mock_get_s_by_id)
    student_service = StudentService()
    with pytest.raises(StudentNotFoundError) as excinfo:
        student_service.get_s_by_id("1000")
    assert str(excinfo.value) == "Student with the id 1000 was not found"
