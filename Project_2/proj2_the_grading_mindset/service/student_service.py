import re
from dao.student_dao import StudentDao
from exception.login import LoginError


class StudentService:

    def __init__(self):
        self.student_dao = StudentDao()

    def student_login(self, username, password):
        student_obj = self.student_dao.get_student_by_username_and_password(username, password)

        if student_obj is None:
            raise LoginError("Invalid username and/or password for student")

        return student_obj.to_dict()
