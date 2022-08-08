from dao.assignment_dao import AssignmentDao
from dao.student_dao import StudentDao
from exception.course_errors import CourseNotFoundError
from exception.student_errors import StudentNotFoundError
from exception.student_errors import StudentNotFoundError


class AssignmentService:

    def __init__(self):
        self.assignment_dao = AssignmentDao()
        self.student_dao = StudentDao()

    def get_all_assignments_by_s_id(self, s_id):

        # if self.assignment_dao.get_all_assignments_by_s_id(s_id) is None:
        #     raise StudentNotFoundError()

        list_of_assignment_object = self.assignment_dao.get_all_assignments_by_s_id(s_id)
        if not list_of_assignment_object:
            raise StudentNotFoundError()

        list_of_assignment_dictionaries = []

        for assignment_obj in list_of_assignment_object:
            list_of_assignment_dictionaries.append(assignment_obj.to_dict())

        return list_of_assignment_dictionaries

    def get_all_assignments_by_c_id(self, s_id, c_id):
        list_of_assignment_object = self.assignment_dao.get_all_assignments_by_c_id(s_id, c_id)
        if not list_of_assignment_object:
            raise CourseNotFoundError(f"Course with course_id {c_id} was not found")

        list_of_assignment_dictionaries = []

        for assignment_obj in list_of_assignment_object:
            list_of_assignment_dictionaries.append(assignment_obj.to_dict())

        return list_of_assignment_dictionaries

    def add_assignments_to_c_id(self, s_id, c_id, c_object):
        if self.student_dao.get_s_by_id(s_id) is None:
            raise StudentNotFoundError(f"Student with id {s_id} was not found")

        added_new_assignment = self.assignment_dao.add_assignments_to_c_id(s_id, c_id, c_object)
        if not added_new_assignment:
            raise CourseNotFoundError(f"Student with course_id{c_id} was not found")

        return added_new_assignment.to_dict()
    def update_assignments_by_c_id_and_a_id(self, t_id, c_id, a_id, a_object):
        updated_assignment_object = self.assignment_dao.update_assignments_by_c_id_and_a_id(t_id, c_id, a_id, a_object)
        # if updated_assignment_object is None:
        #     raise CourseNotFoundError(f"Course with {c_object.id} was not found")
        if updated_assignment_object is None:
            raise CourseNotFoundError(f"Course with c_id {c_id} and assignment with a_id {a_id} was not found")

        return updated_assignment_object.to_dict()
