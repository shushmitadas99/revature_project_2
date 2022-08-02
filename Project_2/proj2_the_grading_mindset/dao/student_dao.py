from dotenv import dotenv_values

from model.student import Student
import psycopg

config = dotenv_values(".env")  # is a dict

class StudentDao:

    # for login logout and loginstatus endpoints
    def get_student_by_username_and_password(self, username, password):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'], user=config['user'],
                       password=config['password']) as conn:
            with conn.cursor() as cur:
                cur.execute("select * from students where username = %s and password = %s", (username, password))
                s_info = cur.fetchone()

                if s_info is None:
                    return None

                s_id = s_info[0]
                username = s_info[1]
                password = s_info[2]
                s_name = s_info[3]
                s_email = s_info[4]

                return Student(s_id, username, password, s_name, s_email)
