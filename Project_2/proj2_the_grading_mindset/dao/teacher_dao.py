import os
import psycopg
from dotenv import dotenv_values
from model.teacher import Teacher

config = dotenv_values(".env")  # is a dict


class TeacherDao:
    def get_t_by_id(self, t_id):
        with psycopg.connect(host=config['db_url'], user=config['db_username'], password=config['db_password']) as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM teachers WHERE t_id = %s", (t_id,))

                t_row = cur.fetchone()
                if not t_row:
                    return None

                t_id = t_row[0]
                username = t_row[1]
                password = t_row[2]
                t_name = t_row[3]
                t_email = t_row[4]

                return Teacher(t_id, username, password, t_name, t_email)

    # for login logout and loginstatus endpoints
    def get_t_by_username_and_password(self, username, password):
        with psycopg.connect(host=config['db_url'], user=config['db_username'], password=config['db_password']) as conn:
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
