class Assignment:
    def __init__(self, assn, submitted, grade, grade_time):
        self.assn = assn
        self.submitted = submitted
        self.grade = grade
        self.grade_time = grade_time


        def to_dict(self):
            return {
                "assn": self.assn,
                "submitted": self.submitted,
                "grade": self.grade,
                "self.grade_time": self.grade_time
            }