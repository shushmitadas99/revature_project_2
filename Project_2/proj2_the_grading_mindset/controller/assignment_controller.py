from flask import Blueprint, request, session

from exception.course_errors import CourseNotFoundError
from exception.student_errors import StudentNotFoundError
from exception.teacher_errors import TeacherNotFoundError
from model.assignment_model import Assignments
from service.assignment_service import AssignmentService

ac = Blueprint('assignment_controller', __name__)

assignment_service = AssignmentService()


@ac.route('/slogin/<s_id>/a', methods=['GET'])
def get_all_assignments_by_s_id(s_id):
    try:
        return {
            "assignments": assignment_service.get_all_assignments_by_s_id(s_id)
    }
    except StudentNotFoundError as e:
        return{
            "message": str(e)
        }, 404

@ac.route('/slogin/<s_id>/c/<c_id>/a', methods=['GET'])
def get_all_assignments_by_c_id(s_id, c_id):
    try:
        return {
            "assignments": assignment_service.get_all_assignments_by_c_id(s_id, c_id)
        }
    except StudentNotFoundError as e:
        return{
            "message": str(e)
        }, 404
    except CourseNotFoundError as e:
        return {
                   "message": str(e)
               }, 404

@ac.route('/slogin/<s_id>/c/<c_id>/a', methods=['POST'])
def add_assignments_to_c_id(s_id, c_id):
    c_json_dictionary = request.get_json()
    a_object = Assignments(None, c_id, None, c_json_dictionary["grade"], None)
    try:
        return assignment_service.add_assignments_to_c_id(s_id, c_id, a_object), 201
    except StudentNotFoundError as e:
        return{
            "message": str(e)
        }, 404
    except CourseNotFoundError as e:
        return {
                   "message": str(e)
               }, 404
@ac.route('/tlogin/<t_id>/a', methods=['GET'])
def get_all_assignments_by_t_id(t_id):
    try:
        return {
            "assignments": assignment_service.get_all_assignments_by_t_id(t_id)
    }
    except TeacherNotFoundError as e:
        return{
            "message": str(e)
        }, 404



@ac.route('/tlogin/<t_id>/c/<c_id>/a', methods=['GET'])
def get_all_assignments_by_t_id_and_c_id(t_id, c_id):
    try:
        return {
            "assignments": assignment_service.get_all_assignments_by_t_id_and_c_id(t_id, c_id)
        }

    except CourseNotFoundError as e:
        return {
                   "message": str(e)
               }, 404



@ac.route('/tlogin/<t_id>/c/<c_id>/a/<a_id>', methods=['PUT'])
def update_assignments_by_c_id_and_a_id(t_id, c_id, assn):
    try:
        a_json_dictionary = request.get_json()
        # print(a_json_dictionary['grade'])
        a_object = Assignments(None, None, None, a_json_dictionary['grade'], None)
        print(a_object.grade)
        return assignment_service.update_assignments_by_c_id_and_a_id(t_id, c_id, assn, a_object)

    except CourseNotFoundError as e:
        return {
            "message": str(e)
        }, 404
