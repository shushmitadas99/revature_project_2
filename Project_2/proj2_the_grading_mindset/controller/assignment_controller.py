from flask import Blueprint, request, session


from service.assignment_service import AssignmentService

ac = Blueprint('assignment_controller', __name__)

assignment_service = AssignmentService()
@ac.route('/student/<s_id>/<course_id>/assignments')
def get_all_assignments_by_username_and_course_id(course_id):
    return {
        "assignments": assignment_service.get_all_assignments_by_username_and_course_id(course_id, )
    }
