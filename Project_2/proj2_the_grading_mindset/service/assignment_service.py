from dao.assignment_dao import AssignmentDao


class AssignmentService:

    def __init__(self):
        self.assignment_dao = AssignmentDao

    def get_all_assignments_by_username_and_course_id(self, course_id):
        list_of__assignment_object = self.assignment_dao.get_all_assignments_by_username_and_course_id(course_id, )

        list_of_assignment_dictionaries = []
        for assignment_obj in list_of__assignment_object:
            list_of_assignment_dictionaries.append(assignment_obj.dict())

        return list_of_assignment_dictionaries