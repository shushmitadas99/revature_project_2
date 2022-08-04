from dotenv import dotenv_values

from model.student import Student
import psycopg

config = dotenv_values(".env")  # is a dict

class StudentDao:
    def get_s_by_id(self, s_id):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'], user=config['user'],
                             password=config['password']) as conn:

            with conn.cursor() as cur:
                # Jace's Database Query:
                cur.execute("SELECT * FROM project2.students WHERE s_id = %s", (s_id,))

                # Shushmita's Database query:
                # cur.execute("select * from proj2_tgm.students where s_id = %s", (s_id,))

                s_row = cur.fetchone()
                if not s_row:
                    return None

                s_id = s_row[0]
                username = s_row[1]
                password = s_row[2]
                s_name = s_row[3]
                s_email = s_row[4]

                return Student(s_id, username, password, s_name, s_email)

    # for login logout and loginstatus endpoints
    def get_s_by_username_and_password(self, username, password):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'], user=config['user'],
                             password=config['password']) as conn:
            with conn.cursor() as cur:
                # Please use the appropriate database query for testing endpoint:
                # That is comment out the other ones

                # Jace's Database query:
                # cur.execute("select * from project2.students where username = %s and password = %s",
                # (username, password))

                # Shushmita's Database query:
                cur.execute("select * from proj2_tgm.students where username = %s and password = %s",
                            (username, password))

                s_info = cur.fetchone()

                if s_info is None:
                    return None

                s_id = s_info[0]
                username = s_info[1]
                password = s_info[2]
                s_name = s_info[3]
                s_email = s_info[4]

                return Student(s_id, username, password, s_name, s_email)
