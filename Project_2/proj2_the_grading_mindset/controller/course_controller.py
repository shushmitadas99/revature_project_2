from flask import Blueprint, request
from model.course import Course
from service.course_service import CourseService
from exception.student_errors import StudentNotFoundError
from exception.course_errors import CourseNotFoundError
from exception.teacher_errors import TeacherNotFoundError

cc = Blueprint('course_controller', __name__)

course_service = CourseService()

@cc.route('/slogin/<s_id>/c', methods=['GET'])
def get_all_cs_by_s_id(s_id):
    try:
        return {
            "courses": course_service.get_all_cs_by_s_id(s_id)
        }
    except StudentNotFoundError as e:
        return {
                    "message": str(e)
                }, 404

@cc.route('/slogin/<s_id>/c', methods=['POST'])
def add_c_to_s(s_id):
    c_json_dictionary = request.get_json()
    c_object = Course(None, c_json_dictionary['c_name'], c_json_dictionary['c_desc'], s_id, c_json_dictionary['t_id'])
    try:
        return course_service.add_c_to_s(c_object), 201
    except StudentNotFoundError as e:
        return{
            "message": str(e)
        }, 404

@cc.route('/slogin/<s_id>/c/<c_id>', methods=['PUT'])
def update_c_by_ids(s_id, c_id):
    try:
        c_json_dictionary = request.get_json()
        c_object = Course(c_id, c_json_dictionary['c_name'], c_json_dictionary['c_desc'], s_id,
                          c_json_dictionary['t_id'])
        return course_service.update_c_by_ids(c_object), 201
    except StudentNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except CourseNotFoundError as e:
        return {
            "message": str(e)
        }, 404

@cc.route('/tlogin/<t_id>/c', methods=['GET'])
def get_all_cs_by_t_id(t_id):
    try:
        return {
            "courses": course_service.get_all_cs_by_t_id(t_id)
        }
    except TeacherNotFoundError as e:
        return {
                    "message": str(e)
                }, 404

@cc.route('/tlogin/<t_id>/c', methods=['POST'])
def add_c_to_t(t_id):
    c_json_dictionary = request.get_json()
    c_object = Course(None, c_json_dictionary['c_name'], c_json_dictionary['c_desc'], c_json_dictionary['s_id'], t_id)
    try:
        return course_service.add_c_to_s(c_object), 201
    except TeacherNotFoundError as e:
        return{
            "message": str(e)
        }, 404

@cc.route('/tlogin/<t_id>/c/<c_id>', methods=['PUT'])
def update_c_by_ids_t(t_id, c_id):
    try:
        c_json_dictionary = request.get_json()
        c_object = Course(c_id, c_json_dictionary['c_name'], c_json_dictionary['c_desc'], c_json_dictionary['s_id'],
                          t_id)
        return course_service.update_c_by_ids(c_object), 201
    except TeacherNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except CourseNotFoundError as e:
        return {
            "message": str(e)
        }, 404




