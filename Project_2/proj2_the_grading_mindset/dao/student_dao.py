import os
import psycopg
from dotenv import dotenv_values
from model.student import Student

config = dotenv_values(".env")  # is a dict


class StudentDao:
    def get_s_by_id(self, s_id):

        with psycopg.connect(host=config.get('host'), user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:

                cur.execute("SELECT * FROM students WHERE s_id = %s", (s_id,))

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

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:

            with conn.cursor() as cur:

                cur.execute("select * from students where username = %s and password = %s",
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
