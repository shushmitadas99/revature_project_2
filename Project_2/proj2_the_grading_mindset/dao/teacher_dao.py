from dotenv import dotenv_values

from model.teacher import Teacher
import psycopg

config = dotenv_values(".env")  # is a dict

class TeacherDao:

    # for login logout and loginstatus endpoints
    def get_teacher_by_username_and_password(self, username, password):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'], user=config['user'],
                       password=config['password']) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from teachers where username = %s and password = %s", (username, password))
                t_info = cur.fetchone()

                if t_info is None:
                    return None

                t_id = t_info[0]
                username = t_info[1]
                password = t_info[2]
                t_name = t_info[3]
                t_email = t_info[4]

                return Teacher(t_id, username, password, t_name, t_email)
