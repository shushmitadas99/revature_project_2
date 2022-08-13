from flask import Blueprint, request, session
from exception.login import LoginError
from exception.teacher_errors import TeacherNotFoundError
from service.teacher_service import TeacherService
from model.teacher import Teacher

tc = Blueprint('teacher_controller', __name__)

teacher_service = TeacherService()

@tc.route('/t/<t_id>', methods=['GET'])
def get_t_by_id(t_id):
    try:
        return teacher_service.get_t_by_id(t_id)
    except TeacherNotFoundError as e:
        return{
            "message": str(e)
        }, 404

@tc.route('/tlogin', methods=['POST'])
def t_login():
    request_body_dict = request.get_json()

    username = request_body_dict['username']
    password = request_body_dict['password']

    try:
        teacher_dict = teacher_service.t_login(username, password)
        session['t_info'] = teacher_dict

        return teacher_dict, 200
    except LoginError as e:
        return {
            "message": str(e)
        }, 400


@tc.route('/tloginstatus', methods=['GET'])
def t_loginstatus():
    if session.get('t_info') is not None:
        return{
            "message": "You are logged in",
            "logged_in_teacher": session.get('t_info')
        }, 200

    else:
        return{
            "message": "You are not logged in"
        }, 400


@tc.route('/tlogout', methods=['POST'])
def t_logout():
    session.clear()
    return {
        "message": "Successfully logged out"
    }, 200
