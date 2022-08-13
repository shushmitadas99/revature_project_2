import pytest
from exception.course_errors import CourseNotFoundError
from exception.student_errors import StudentNotFoundError
from exception.teacher_errors import TeacherNotFoundError
from model import assignment_model
from model.assignment_model import Sassignments, Assignments
from service.assignment_service import AssignmentService
from service.student_service import StudentService


def test_get_all_assignments_by_s_id_positive_multiple(mocker):
    def mock_get_all_assignments_by_s_id(self, s_id, a_filter_by_c):
        return [
            Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science'),
            Sassignments(2, '2022-08-10 07:03:16.478', 'B', '2022-08-10 07:03:16.478', 'math')
        ]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_s_id', mock_get_all_assignments_by_s_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_s_id(s_id=1, a_filter_by_c=None)
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
    def mock_get_all_assignments_by_s_id(self, s_id, a_filter_by_c):
        return [Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science')]

    mocker.patch('dao.assignment_dao.AssignmentDao.get_all_assignments_by_s_id', mock_get_all_assignments_by_s_id)
    assignment_service = AssignmentService()
    actual = assignment_service.get_all_assignments_by_s_id(s_id=1, a_filter_by_c='science')
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
    def mock_get_all_assignments_by_s_id(self, s_id, a_filter_by_c):
        if s_id == "1" and a_filter_by_c == None:
            return [Sassignments(1, '2022-08-10 07:03:16.478', 'A', '2022-08-10 07:03:16.478', 'science')]
        else:
            return None

    mocker.patch("dao.assignment_dao.AssignmentDao.get_all_assignments_by_s_id", mock_get_all_assignments_by_s_id)
    assignment_service = AssignmentService()
    with pytest.raises(StudentNotFoundError) as excinfo:
        assignment_service.get_all_assignments_by_s_id(s_id=1000, a_filter_by_c=None)
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


def test_get_all_assignments_by_t_id_positive_multiple(mocker):
    def mock_get_all_assignments_by_t_id(self, t_id):
        return [
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


def test_add_assignments_to_c_id_positive(mocker):  # Test pass (if block commented)
    def mock_add_assignments_to_c_id(submitted, grade, grade_time, c_name):
        if submitted is None and grade is None and grade_time is None and c_name == "science":
            return None
    mocker.patch("dao.assignment_dao.AssignmentDao.add_assignments_to_c_id", mock_add_assignments_to_c_id)
    a_object_to_add = assignment_model.Sassignments(1, None, None, None, "science")

    def mock_add_assignments_to_c_id(self, s_id, c_id, a_object):
        if a_object == a_object_to_add and c_id == 1:
            return assignment_model.Sassignments(1, None, None, None, "science")
        else:
            return None

    mocker.patch("dao.assignment_dao.AssignmentDao.add_assignments_to_c_id", mock_add_assignments_to_c_id)
    assignment_service = AssignmentService()
    actual = assignment_service.add_assignments_to_c_id(a_object=a_object_to_add, s_id=1, c_id=1)
    assert actual == {
        "assn": 1,
        "submitted": None,
        "grade": None,
        "grade_time": None,
        "c_name": "science"
    }

def test_add_assignments_to_c_id_negative_s_id(mocker):  # Test fail
    def mock_get_s_by_id(self, s_id):
        if s_id == "1":
            return Sassignments(1, None, None, None, "science")
        else:
            return None
    mocker.patch("dao.student_dao.StudentDao.get_s_by_id", mock_get_s_by_id)
    student_service = StudentService()
    with pytest.raises(StudentNotFoundError) as excinfo:
        student_service.get_s_by_id("1000")
    assert str(excinfo.value) == "Student with the id 1000 was not found"

def test_add_assignments_to_c_id_negative_c_id(mocker): # Test fail
    a_object_to_add = assignment_model.Assignments(1, 1, None, None, None)

    def mock_add_assignments_to_c_id(self, s_id, c_id, a_object):
        if a_object.c_id == "1":
            return assignment_model.Assignments(1, 1, None, None, None)
        else:
            return None
    mocker.patch("dao.assignment_dao.AssignmentDao.add_assignments_to_c_id", mock_add_assignments_to_c_id)
    assignment_service = AssignmentService()
    with pytest.raises(CourseNotFoundError) as excinfo:
        assignment_service.add_assignments_to_c_id(a_object=a_object_to_add, s_id=1, c_id=1000)
    assert str(excinfo.value) == "Course with id 1000 was not found"

def test_update_assignments_by_c_id_and_a_id_positive(mocker):
    updated_a_object = Assignments(1, 1,  None, 'A', None)

    def mock_update_assignments_by_c_id_and_a_id(self, t_id, c_id, assn, a_object):
        if a_object.c_id == 1 and a_object.assn == 1:
            return Assignments(1, 1,  None, 'A', None)
        else:
            return None
    mocker.patch("dao.assignment_dao.AssignmentDao.update_assignments_by_c_id_and_a_id",
                 mock_update_assignments_by_c_id_and_a_id)
    assignment_service = AssignmentService()
    actual = assignment_service.update_assignments_by_c_id_and_a_id(a_object=updated_a_object, t_id=1,
                                                                    c_id=1, assn=1)
    assert actual == {
        "assn": 1,
        "c_id": 1,
        "submitted": None,
        "grade": "A",
        "self.grade_time": None
        }

def test_update_assignments_by_c_id_and_a_id_negative(mocker):
    updated_a_object = Assignments(8, 1, None, 'A', None)

    def mock_update_assignments_by_c_id_and_a_id(self, t_id, c_id, assn, a_object):
        if a_object.c_id == 1 and a_object.assn == 1:
            return Assignments(1, 1,  None, 'A', None)
        else:
            return None
    mocker.patch("dao.assignment_dao.AssignmentDao.update_assignments_by_c_id_and_a_id",
                 mock_update_assignments_by_c_id_and_a_id)
    assignment_service = AssignmentService()
    with pytest.raises(CourseNotFoundError) as excinfo:
        assignment_service.update_assignments_by_c_id_and_a_id(a_object=updated_a_object, t_id=1, c_id=100, assn=100)
    assert str(excinfo.value) == f"Course with c_id 100 and assignment with a_id 100 was not found"
