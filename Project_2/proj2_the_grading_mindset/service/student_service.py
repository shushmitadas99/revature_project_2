import re
from dao.student_dao import StudentDao
from exception.login import LoginError
from exception.student_errors import StudentNotFoundError


class StudentService:

    def __init__(self):
        self.student_dao = StudentDao()

    def get_s_by_id(self, s_id):
        s_object = self.student_dao.get_s_by_id(s_id)
        if not s_object:
            raise StudentNotFoundError(f"Student with the id {s_id} was not found")
        return s_object.to_dict()

    def s_login(self, username, password):
        s_obj = self.student_dao.get_s_by_username_and_password(username, password)

        if s_obj is None:
            raise LoginError("Invalid username and/or password for student")

        return s_obj.to_dict()
