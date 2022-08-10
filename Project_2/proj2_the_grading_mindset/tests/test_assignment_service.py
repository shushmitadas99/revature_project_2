import pytest
import pytest_mock
from dotenv import dotenv_values
import model.course as course
from datetime import datetime, timezone

from exception.course_errors import CourseNotFoundError
from exception.student_errors import StudentNotFoundError
from exception.teacher_errors import TeacherNotFoundError
from model import assignment_model
from model.assignment_model import Sassignments, Assignments
from model.student import Student
from model.teacher import Teacher
from service.assignment_service import AssignmentService
from service.student_service import StudentService

# current_time = datetime.datetime.now()
# print(current_time)

def test_get_all_assignments_by_s_id_positive_multiple(mocker):
    def mock_get_all_assignments_by_s_id(self, s_id):
        return [
            # Sassignments(row[0], row[1], row[2], row[3], row[4])
            Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science'),
            Sassignments(2, '2022-08-10 07:03:16.478', 'B', '2022-08-10 07:03:16.478', 'math')
        ]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_s_id', mock_get_all_assignments_by_s_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_s_id(s_id=1)
    assert actual == [
        {
            "assn": 1,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'A',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'science'
        },
        {
            "assn": 2,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'B',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'math'
        }
    ]

def test_get_all_assignments_by_s_id_positive_single(mocker):
    def mock_get_all_assignments_by_s_id(self, s_id):
        return [Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science')]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_s_id', mock_get_all_assignments_by_s_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_s_id(s_id=1)
    assert actual == [
        {
            "assn": 1,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'A',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'science'
        }
    ]


def test_get_all_assignments_by_s_id_negative(mocker):
    def mock_get_all_assignments_by_s_id(self, s_id):
        if s_id == "1":
            return [Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science')]
        else:
            return None

    mocker.patch("dao.assignment_dao.AssignmentDao.get_all_assignments_by_s_id", mock_get_all_assignments_by_s_id)
    assignment_service = AssignmentService()
    with pytest.raises(StudentNotFoundError) as excinfo:
        assignment_service.get_all_assignments_by_s_id(s_id=1000)
    assert str(excinfo.value) == f"Student with id 1000 was not found"


def test_get_all_assignments_by_c_id_positive_multiple(mocker):
    def mock_get_all_assignments_by_c_id(self, s_id, c_id):
        return [
            Sassignments(2, '2022-08-10 07:03:16.478', None, '2022-08-10 07:03:16.478', 'science'),
            Sassignments(3, '2022-08-10 09:35:54.944', None, '2022-08-10 09:35:54.944', 'science')
        ]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_c_id', mock_get_all_assignments_by_c_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_c_id(s_id=2, c_id=2)
    assert actual == [
        {
            "assn": 2,
            "submitted": "2022-08-10 07:03:16.478",
            "grade": None,
            "grade_time": "2022-08-10 07:03:16.478",
            "c_name": "science"
        },
        {
            "assn": 3,
            "submitted": "2022-08-10 09:35:54.944",
            "grade": None,
            "grade_time": "2022-08-10 09:35:54.944",
            "c_name": "science",
        }
    ]


def test_get_all_assignments_by_c_id_positive_single(mocker):
    def mock_get_all_assignments_by_c_id(self, s_id, c_id):
        return [Sassignments(1, '2022-08-10 07:03:16.478', None, '2022-08-10 07:03:16.478', 'science')]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_c_id', mock_get_all_assignments_by_c_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_c_id(s_id=1, c_id=1)
    assert actual == [
        {
            "assn": 1,
            "submitted": "2022-08-10 07:03:16.478",
            "grade": None,
            "grade_time": "2022-08-10 07:03:16.478",
            "c_name": "science"
        }
    ]


def test_get_all_assignments_by_c_id_negative(mocker):
    def mock_get_all_assignments_by_c_id(self, s_id, c_id):
        if s_id == 1 and c_id == 1:
            return [Sassignments(1, '2022-08-10 07:03:16.478', None, '2022-08-10 07:03:16.478', 'science')]
        else:
            return None

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_c_id', mock_get_all_assignments_by_c_id)
    assignment_service = AssignmentService()
    with pytest.raises(CourseNotFoundError) as excinfo:
        assignment_service.get_all_assignments_by_c_id(s_id=1, c_id=1000)
    assert str(excinfo.value) == f"Course with course_id 1000 was not found"


# FIXME: TypeError: add_assignments_to_c_id() missing 1 required positional argument: 'a_object'
# def test_add_assignments_to_c_id_positive(mocker):
#     def mock_add_assignments_to_c_id(c_id, submitted, grade, grade_time):
#         if c_id == 1 and submitted == 2022 and grade is None and grade_time is None:
#             return None
#         # assn, c_id, submitted, grade, grade_time
#     mocker.patch("dao.assignment_dao.AssignmentDao.add_assignments_to_c_id", mock_add_assignments_to_c_id)
#     a_object_to_add = assignment_model.Assignments(None, 1, 2022, None, None)
#
#     def mock_add_assignments_to_c_id(self, c_id, a_object):
#         if a_object == a_object_to_add and c_id == 1:
#             return assignment_model.Assignments(1, 1, 2022, None, None)
#         else:
#             return None
#
#     mocker.patch("dao.assignment_dao.AssignmentDao.add_assignments_to_c_id", mock_add_assignments_to_c_id)
#     assignment_service = AssignmentService()
#     actual = assignment_service.add_assignments_to_c_id(a_object_to_add, c_id=1)
#
#     assert actual == {
#         "assn": 1,
#         "c_id": 1,
#         "submitted": 2022,
#         "grade": None,
#         "grade_time": None
#     }


def test_get_all_assignments_by_t_id_positive_multiple(mocker):
    def mock_get_all_assignments_by_t_id(self, t_id):
        return [
            # Sassignments(row[0], row[1], row[2], row[3], row[4])
            Sassignments(2, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science'),
            Sassignments(3, '2022-08-10 07:03:16.478', 'B', '2022-08-10 07:03:16.478', 'science'),
            Sassignments(4, '2022-08-10 07:03:16.478', 'B', '2022-08-10 07:03:16.478', 'science'),
        ]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_t_id', mock_get_all_assignments_by_t_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_t_id(t_id=1)
    assert actual == [
        {
            "assn": 2,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'A',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'science'
        },
        {
            "assn": 3,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'B',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'science'
        },
        {
            "assn": 4,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'B',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'science'
        }
    ]


def test_get_all_assignments_by_t_id_positive_single(mocker):
    def mock_get_all_assignments_by_t_id(self, t_id):
        return [Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science')]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_t_id', mock_get_all_assignments_by_t_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_t_id(t_id=1)
    assert actual == [
        {
            "assn": 1,
            "submitted": '2022-08-10 07:03:16.478',
            "grade": 'A',
            "grade_time": '2022-08-10 07:03:16.478',
            "c_name": 'science'
        }
    ]


def test_get_all_assignments_by_t_id_negative(mocker):
    def mock_get_all_assignments_by_t_id(self, t_id):
        if t_id == "1":
            return [Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science')]
        else:
            return None

    mocker.patch("dao.assignment_dao.AssignmentDao.get_all_assignments_by_t_id", mock_get_all_assignments_by_t_id)
    assignment_service = AssignmentService()
    with pytest.raises(TeacherNotFoundError) as excinfo:
        assignment_service.get_all_assignments_by_t_id(t_id=1000)
    assert str(excinfo.value) == f"Teacher with id 1000 was not found"