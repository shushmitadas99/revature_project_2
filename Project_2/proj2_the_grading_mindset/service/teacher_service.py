from dao.teacher_dao import TeacherDao
from exception.login import LoginError
from exception.teacher_errors import TeacherNotFoundError


class TeacherService:

    def __init__(self):
        self.teacher_dao = TeacherDao()

    def get_t_by_id(self, t_id):
        t_object = self.teacher_dao.get_t_by_id(t_id)
        if not t_object:
            raise TeacherNotFoundError(f"Teacher with the id {t_id} was not found")
        return t_object.to_dict()

    def t_login(self, username, password):
        t_obj = self.teacher_dao.get_t_by_username_and_password(username, password)

        if t_obj is None:
            raise LoginError("Invalid username and/or password for teacher")

        return t_obj.to_dict()