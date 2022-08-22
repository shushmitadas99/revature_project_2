import pytest
import pytest_mock
from dotenv import dotenv_values
import model.course as course
from model.student import Student
from model.teacher import Teacher
from service.course_service import CourseService
from exception.course_errors import CourseNotFoundError
from exception.student_errors import StudentNotFoundError
from exception.teacher_errors import TeacherNotFoundError


config = dotenv_values(".env")


def test_get_all_cs_by_s_id_positive_multiple(mocker):
    def mock_get_all_cs_by_s_id(self, s_id):
        return [course.SCourse(1, 'teacher1', 'teacher1@email.com', 'science', 'chemistry'),
                course.SCourse(2, 'teacher2', 'teacher2@email.com', 'math', 'algebra')]
    mocker.patch('dao.course_dao.CourseDao.get_all_cs_by_s_id', mock_get_all_cs_by_s_id)
    course_service = CourseService()
    actual = course_service.get_all_cs_by_s_id(s_id=2)
    assert actual == [
        {
            "c_id": 1,
            "t_name": 'teacher1',
            "t_email": 'teacher1@email.com',
            "c_name": 'science',
            "c_desc": 'chemistry',
        },
        {
            "c_id": 2,
            "t_name": 'teacher2',
            "t_email": 'teacher2@email.com',
            "c_name": 'math',
            "c_desc": 'algebra',
        }
    ]


def test_get_all_cs_by_s_id_positive_single(mocker):
    def mock_get_all_cs_by_s_id(self, s_id):
        return [course.SCourse(1, 'teacher1', 'teacher1@email.com', 'science', 'chemistry')]

    mocker.patch('dao.course_dao.CourseDao.get_all_cs_by_s_id', mock_get_all_cs_by_s_id)
    course_service = CourseService()
    actual = course_service.get_all_cs_by_s_id(s_id=1)
    assert actual == [
        {
            "c_id": 1,
            "t_name": 'teacher1',
            "t_email": 'teacher1@email.com',
            "c_name": 'science',
            "c_desc": 'chemistry',
        }
    ]


def test_get_all_cs_by_s_id_negative(mocker):
    def mock_get_all_cs_by_s_id(self, s_id):
        if s_id == "1":
            return [course.SCourse(1, 'teacher1', 'teacher1@email.com', 'science', 'chemistry')]
        else:
            return None
    mocker.patch("dao.course_dao.CourseDao.get_all_cs_by_s_id", mock_get_all_cs_by_s_id)
    course_service = CourseService()
    with pytest.raises(StudentNotFoundError) as excinfo:
        course_service.get_all_cs_by_s_id(s_id=1000)
    assert str(excinfo.value) == f"Student with id 1000 was not found"


def test_add_c_to_s_positive(mocker):
    def mock_get_s_by_id(self, s_id):
        return Student(1, "student1", "password1", "Student One", "student1@email.com")
    def mock_add_c_to_s(c_name, c_desc, s_id, t_id):
        if c_name == "science" and c_desc == "chemistry" and s_id == 1 and t_id == 1:
            return None
    mocker.patch("dao.course_dao.CourseDao.add_c_to_s", mock_add_c_to_s)
    mocker.patch("dao.student_dao.StudentDao.get_s_by_id", mock_get_s_by_id)
    c_object_to_add = course.Course(None, "science", "chemistry", 1, 1)

    def mock_add_c_to_s(self, c_object):
        if c_object == c_object_to_add:
            return course.Course(1, "science", "chemistry", 1, 1)
        else:
            return None

    mocker.patch("dao.course_dao.CourseDao.add_c_to_s", mock_add_c_to_s)
    course_service = CourseService()
    actual = course_service.add_c_to_s(c_object_to_add)
    assert actual == {
        "c_id": 1,
        "c_name": "science",
        "c_desc": "chemistry",
        "s_id": 1,
        "t_id": 1
    }


def test_add_c_to_s_negative(mocker):
    def mock_get_s_by_id(self, s_id):
        return None

    c_object_to_add = course.Course(None, "history", "renaissance", 10, 1)

    def mock_add_c_to_s(self, c_object):
        if not c_object != c_object_to_add:
            return course.Course(None, "history", "renaissance", 10, 1)

    mocker.patch("dao.course_dao.CourseDao.add_c_to_s", mock_add_c_to_s)
    mocker.patch("dao.student_dao.StudentDao.get_s_by_id", mock_get_s_by_id)
    course_service = CourseService()
    with pytest.raises(StudentNotFoundError) as excinfo:
        course_service.add_c_to_s(c_object_to_add)
    assert str(excinfo.value) == f"Student with id {c_object_to_add.s_id} was not found"


def test_update_c_by_ids_positive(mocker):
    update_c_object = course.Course(2, "p.e", "swimming", 2, 1)

    def mock_update_c_by_ids(self, c_object):
        if c_object.c_id == 2 and c_object.s_id == 2 and c_object.t_id == 1:
            return course.Course(2, "p.e", "swimming", 2, 1)
            # will replace "science" and "chemistry" for s_id == 2 and t_id == 1
        else:
            return None
    mocker.patch("dao.course_dao.CourseDao.update_c_by_ids", mock_update_c_by_ids)
    course_service = CourseService()
    actual = course_service.update_c_by_ids(update_c_object)
    assert actual == {
        "c_id": 2,
        "c_name": "p.e",
        "c_desc": "swimming",
        "s_id": 2,
        "t_id": 1
    }


def test_update_c_by_ids_negative(mocker):
    update_c_object = course.Course(12, "p.e", "swimming", 2, 1)

    def mock_update_c_by_ids(self, c_object):
        if c_object.c_id == 2 and c_object.s_id == 2 and c_object.t_id == 1:
            return course.Course(2, "p.e", "swimming", 2, 1)
        else:
            return None
    mocker.patch("dao.course_dao.CourseDao.update_c_by_ids", mock_update_c_by_ids)
    course_service = CourseService()
    with pytest.raises(CourseNotFoundError) as excinfo:
        course_service.update_c_by_ids(update_c_object)
    assert str(excinfo.value) == f"Course with {update_c_object.c_id} was not found"


def test_get_all_cs_by_t_id_positive_multiple(mocker):
    def mock_get_all_cs_by_t_id(self, t_id):
        return [course.TCourse(2, 'student2', 'student1@email.com', 'math', 'algebra'),
                course.TCourse(4, 'student2', 'student2@email.com', 'english', 'academic')]
    mocker.patch('dao.course_dao.CourseDao.get_all_cs_by_t_id', mock_get_all_cs_by_t_id)
    course_service = CourseService()
    actual = course_service.get_all_cs_by_t_id(t_id=2)
    assert actual == [
        {
            "c_id": 2,
            "s_name": 'student2',
            "s_email": 'student1@email.com',
            "c_name": 'math',
            "c_desc": 'algebra'
        },
        {
            "c_id": 4,
            "s_name": 'student2',
            "s_email": 'student2@email.com',
            "c_name": 'english',
            "c_desc": 'academic'
        }
    ]


def test_get_all_cs_by_t_id_positive_single(mocker):
    def mock_get_all_cs_by_t_id(self, s_id):
        return [course.TCourse(1, 'student1', 'student1@email.com', 'science', 'chemistry')]

    mocker.patch('dao.course_dao.CourseDao.get_all_cs_by_t_id', mock_get_all_cs_by_t_id)
    course_service = CourseService()
    actual = course_service.get_all_cs_by_t_id(t_id=1)
    assert actual == [
        {
            "c_id": 1,
            "s_name": 'student1',
            "s_email": 'student1@email.com',
            "c_name": 'science',
            "c_desc": 'chemistry',
        }
    ]


def test_get_all_cs_by_t_id_negative(mocker):
    def mock_get_all_cs_by_t_id(self, t_id):
        if t_id == "1":
            return [course.TCourse(1, 'student1', 'student1@email.com', 'science', 'chemistry')]
        else:
            return None
    mocker.patch("dao.course_dao.CourseDao.get_all_cs_by_t_id", mock_get_all_cs_by_t_id)
    course_service = CourseService()
    with pytest.raises(TeacherNotFoundError) as excinfo:
        course_service.get_all_cs_by_t_id(t_id=1000)
    assert str(excinfo.value) == f"Teacher with id 1000 was not found"


def test_add_c_to_t_positive(mocker):
    def mock_get_t_by_id(self, t_id):
        return Teacher(1, "student1", "password1", "Student One", "student1@email.com")

    def mock_add_c_to_t(c_name, c_desc, s_id, t_id):
        if c_name == "science" and c_desc == "chemistry" and s_id == 1 and t_id == 1:
            return None
    mocker.patch("dao.course_dao.CourseDao.add_c_to_t", mock_add_c_to_t)
    mocker.patch("dao.teacher_dao.TeacherDao.get_t_by_id", mock_get_t_by_id)
    c_object_to_add = course.Course(None, "science", "chemistry", 1, 1)

    def mock_add_c_to_t(self, c_object):
        if c_object == c_object_to_add:
            return course.Course(1, "science", "chemistry", 1, 1)
        else:
            return None

    mocker.patch("dao.course_dao.CourseDao.add_c_to_t", mock_add_c_to_t)
    course_service = CourseService()
    actual = course_service.add_c_to_t(c_object_to_add)
    assert actual == {
        "c_id": 1,
        "c_name": "science",
        "c_desc": "chemistry",
        "s_id": 1,
        "t_id": 1
    }

def test_add_c_to_t_negative(mocker):
    def mock_get_t_by_id(self, t_id):
        return None

    c_object_to_add = course.Course(None, "history", "renaissance", 1, 10)

    def mock_add_c_to_t(self, c_object):
        if not c_object != c_object_to_add:
            return course.Course(None, "history", "renaissance", 1, 10)

    mocker.patch("dao.course_dao.CourseDao.add_c_to_t", mock_add_c_to_t)
    mocker.patch("dao.teacher_dao.TeacherDao.get_t_by_id", mock_get_t_by_id)
    course_service = CourseService()
    with pytest.raises(TeacherNotFoundError) as excinfo:
        course_service.add_c_to_t(c_object_to_add)
    assert str(excinfo.value) == f"Teacher with id {c_object_to_add.t_id} was not found"


def test_update_c_by_ids_t_positive(mocker):
    update_c_object = course.Course(2, "p.e", "swimming", 2, 1)

    def mock_update_c_by_ids_t(self, c_object):
        if c_object.c_id == 2 and c_object.s_id == 2 and c_object.t_id == 1:
            return course.Course(2, "p.e", "swimming", 2, 1)
            # will replace "science" and "chemistry" for s_id == 2 and t_id == 1
        else:
            return None
    mocker.patch("dao.course_dao.CourseDao.update_c_by_ids_t", mock_update_c_by_ids_t)
    course_service = CourseService()
    actual = course_service.update_c_by_ids_t(update_c_object)
    assert actual == {
        "c_id": 2,
        "c_name": "p.e",
        "c_desc": "swimming",
        "s_id": 2,
        "t_id": 1
    }


def test_update_c_by_ids_t_negative(mocker):
    update_c_object = course.Course(12, "p.e", "swimming", 2, 1)

    def mock_update_c_by_ids_t(self, c_object):
        if c_object.c_id == 2 and c_object.s_id == 2 and c_object.t_id == 1:
            return course.Course(2, "p.e", "swimming", 2, 1)
        else:
            return None
    mocker.patch("dao.course_dao.CourseDao.update_c_by_ids_t", mock_update_c_by_ids_t)
    course_service = CourseService()
    with pytest.raises(CourseNotFoundError) as excinfo:
        course_service.update_c_by_ids_t(update_c_object)
    assert str(excinfo.value) == f"Course with {update_c_object.c_id} was not found"

