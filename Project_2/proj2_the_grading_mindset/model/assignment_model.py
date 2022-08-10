class Assignments:
    def __init__(self, assn, c_id, submitted, grade, grade_time):
        self.assn = assn
        self.c_id = c_id
        self.submitted = submitted
        self.grade = grade
        self.grade_time = grade_time

    def to_dict(self):
        return {
            "assn": self.assn,
            "c_id": self.c_id,
            "submitted": self.submitted,
            "grade": self.grade,
            "self.grade_time": self.grade_time
            }


class Sassignments:
    def __init__(self, assn, submitted, grade, grade_time, c_name):
        self.assn = assn
        self.submitted = submitted
        self.grade = grade
        self.grade_time = grade_time
        self.c_name = c_name

    def to_dict(self):
        return {
            "assn": self.assn,
            "submitted": self.submitted,
            "grade": self.grade,
            "grade_time": self.grade_time,
            "c_name": self.c_name

            }

class Tassignments:
    def __init__(self, assn, s_name, c_name, c_desc, submitted, grade, grade_time):
        self.assn = assn
        self.s_name = s_name
        self.c_name = c_name
        self.c_desc = c_desc
        self.submitted = submitted
        self.grade = grade
        self.grade_time = grade_time


    def to_dict(self):
        return {
            "assn": self.assn,
            "s_name": self.s_name,
            "c_name": self.c_name,
            "c_desc": self.c_desc,
            "submitted": self.submitted,
            "grade": self.grade,
            "grade_time": self.grade_time,


            }

