from dao.teacher_dao import TeacherDao
from exception.login import LoginError


class TeacherService:

    def __init__(self):
        self.teacher_dao = TeacherDao()

    def t_login(self, username, password):
        t_obj = self.teacher_dao.get_t_by_username_and_password(username, password)

        if t_obj is None:
            raise LoginError("Invalid username and/or password for teacher")

        return t_obj.to_dict()