from dao.teacher_dao import TeacherDao
from exception.login import LoginError


class TeacherService:

    def __init__(self):
        self.teacher_dao = TeacherDao()

    def teacher_login(self, username, password):
        teacher_obj = self.teacher_dao.get_teacher_by_username_and_password(username, password)

        if teacher_obj is None:
            raise LoginError("Invalid username and/or password for teacher")

        return teacher_obj.to_dict()