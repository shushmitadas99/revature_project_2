class Course:
    def __init__(self, c_id, c_name, c_desc, s_id, t_id):
        self.c_id = c_id
        self.c_name = c_name
        self.c_desc = c_desc
        self.s_id = s_id
        self.t_id = t_id

    def to_dict(self):
        return {
            "c_id": self.c_id,
            "c_name": self.c_name,
            "c_desc": self.c_desc,
            "s_id": self.s_id,
            "t_id": self.t_id
        }

class SCourse:
    def __init__(self, c_id, t_name, t_email, c_name, c_desc):
        self.c_id = c_id
        self.t_name = t_name
        self.t_email = t_email
        self.c_name = c_name
        self.c_desc = c_desc

    def to_dict(self):
        return {
            "c_id": self.c_id,
            "t_name": self.t_name,
            "t_email": self.t_email,
            "c_name": self.c_name,
            "c_desc": self.c_desc
        }


class TCourse:
    def __init__(self, c_id, s_name, s_email, c_name, c_desc):
        self.c_id = c_id
        self.s_name = s_name
        self.s_email = s_email
        self.c_name = c_name
        self.c_desc = c_desc

    def to_dict(self):
        return {
            "c_id": self.c_id,
            "s_name": self.s_name,
            "s_email": self.s_email,
            "c_name": self.c_name,
            "c_desc": self.c_desc
        }
