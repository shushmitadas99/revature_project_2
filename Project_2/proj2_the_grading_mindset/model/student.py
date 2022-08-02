class Student:
    def __init__(self, s_id, username, password, s_name, s_email):
        self.s_id = s_id
        self.username = username
        self.password = password
        self.s_name = s_name
        self.s_email = s_email

    def to_dict(self):
        return {
            "s_id": self.s_id,
            "username": self.username,
            "password": self.password,
            "s_name": self.s_name,
            "s_email": self.s_email
        }