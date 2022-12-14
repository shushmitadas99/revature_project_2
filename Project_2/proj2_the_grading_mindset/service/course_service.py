from dao.course_dao import CourseDao
from dao.student_dao import StudentDao
from dao.teacher_dao import TeacherDao
from exception.student_errors import StudentNotFoundError
from exception.course_errors import CourseNotFoundError
from exception.teacher_errors import TeacherNotFoundError

class CourseService:

    def __init__(self):
        self.teacher_dao = TeacherDao()
        self.course_dao = CourseDao()
        self.student_dao = StudentDao()

    def get_all_cs_by_s_id(self, s_id):
        if self.course_dao.get_all_cs_by_s_id(s_id) is None:  # added new correction instead of above if block
            raise StudentNotFoundError(f"Student with id {s_id} was not found")
        return list(map(lambda y: y.to_dict(), self.course_dao.get_all_cs_by_s_id(s_id)))

    def add_c_to_s(self, c_object):
        if self.student_dao.get_s_by_id(c_object.s_id) is None:
            raise StudentNotFoundError(f"Student with id {c_object.s_id} was not found")
        added_new_c = self.course_dao.add_c_to_s(c_object)
        return added_new_c.to_dict()

    def update_c_by_ids(self, c_object):
        updated_c_object = self.course_dao.update_c_by_ids(c_object)
        if updated_c_object is None:
            raise CourseNotFoundError(f"Course with {c_object.c_id} was not found")

        return updated_c_object.to_dict()

    def get_all_cs_by_t_id(self, t_id):
        if self.course_dao.get_all_cs_by_t_id(t_id) is None:
            raise TeacherNotFoundError(f"Teacher with id {t_id} was not found")
        return list(map(lambda y: y.to_dict(), self.course_dao.get_all_cs_by_t_id(t_id)))

    def add_c_to_t(self, c_object):
        if self.teacher_dao.get_t_by_id(c_object.t_id) is None:
            raise TeacherNotFoundError(f"Teacher with id {c_object.t_id} was not found")
        added_new_c = self.course_dao.add_c_to_t(c_object)
        return added_new_c.to_dict()

    def update_c_by_ids_t(self, c_object):
        updated_c_object = self.course_dao.update_c_by_ids_t(c_object)
        if updated_c_object is None:
            raise CourseNotFoundError(f"Course with {c_object.c_id} was not found")

        return updated_c_object.to_dict()
