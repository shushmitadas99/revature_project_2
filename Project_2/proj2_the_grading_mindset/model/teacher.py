class Teacher:
    def __init__(self, t_id, username, password, t_name, t_email):
        self.t_id = t_id
        self.username = username
        self.password = password
        self.t_name = t_name
        self.t_email = t_email

    def to_dict(self):
        return {
            "t_id" : self.t_id,
            "username": self.username,
            "password": self.password,
            "t_name": self.t_name,
            "t_email": self.t_email
        }