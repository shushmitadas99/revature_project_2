from flask import Blueprint, request, session
from exception.login import LoginError
from service.student_service import StudentService
from model.student import Student
from exception.student_errors import StudentNotFoundError

sc = Blueprint('student_controller', __name__)

student_service = StudentService()

@sc.route('/s/<s_id>', methods=['GET'])
def get_s_by_id(s_id):
    try:
        return student_service.get_s_by_id(s_id)
    except StudentNotFoundError as e:
        return{
            "message": str(e)
        }, 404

@sc.route('/slogin', methods=['POST'])
def s_login():
    request_body_dict = request.get_json()

    username = request_body_dict['username']
    password = request_body_dict['password']

    try:
        student_dict = student_service.s_login(username, password)
        session['s_info'] = student_dict

        return student_dict, 200
    except LoginError as e:
        return {
            "message": str(e)
        }, 400


@sc.route('/sloginstatus', methods=['GET'])
def s_loginstatus():
    if session.get('s_info') is not None:
        return{
            "message": "You are logged in",
            "logged_in_student": session.get('s_info')
        }, 200

    else:
        return{
            "message": "You are not logged in"
        }, 400


@sc.route('/slogout', methods=['POST'])
def s_logout():
    session.clear()
    return {
        "message": "Successfully logged out"
    }, 200
