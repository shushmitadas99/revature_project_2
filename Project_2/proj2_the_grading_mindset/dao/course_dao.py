import os

from dotenv import dotenv_values
import psycopg

import model.course as course

config = dotenv_values(".env")

class CourseDao:

    def get_all_cs_by_s_id(self, s_id):  # TODO: added c_id

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:
                # Shushmita's Database query:
                cur.execute("SELECT c.c_id, t.t_name, t.t_email, c.c_name, c.c_desc FROM teachers t "
                            "JOIN courses c ON t.t_id = c.t_id WHERE s_id = %s", (s_id,))

                list_cs = []

                for row in cur:
                    list_cs.append(course.SCourse(row[0], row[1], row[2], row[3], row[4]))

                return list_cs

    def add_c_to_s(self, c_object):

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:
                # Shushmita's Database query:
                cur.execute("INSERT INTO courses (c_name, c_desc, s_id, t_id) "
                            "VALUES (%s, %s, %s, %s) RETURNING *",
                            (c_object.c_name, c_object.c_desc,
                             c_object.s_id, c_object.t_id))

                reimb_row_inserted = cur.fetchone()
                conn.commit()

                return course.Course(reimb_row_inserted[0], reimb_row_inserted[1], reimb_row_inserted[2],
                                     reimb_row_inserted[3], reimb_row_inserted[4])

    def update_c_by_ids(self, c_object):

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:

                # Shushmita's Database query:
                cur.execute("UPDATE courses SET c_name = %s, c_desc = %s, t_id = %s "
                            "WHERE c_id= %s AND s_id = %s RETURNING *",
                            (c_object.c_name, c_object.c_desc, c_object.t_id, c_object.c_id, c_object.s_id))

                conn. commit()

                c_row_updated = cur.fetchone()
                if c_row_updated is None:
                    return None

                return course.Course(c_row_updated[0], c_row_updated[1], c_row_updated[2], c_row_updated[3],
                                     c_row_updated[4])

    def get_all_cs_by_t_id(self, t_id):

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:
                # Jace's Database query:
                # cur.execute("SELECT s_name, s_email, c_name, c_desc FROM project2.students s "
                #             "JOIN project2.courses c ON s.s_id = c.s_id WHERE t_id = %s", (t_id,))

                # Shushmita's Database query:
                cur.execute("SELECT c.c_id, s_name, s_email, c_name, c_desc FROM students s "
                            "JOIN courses c ON s.s_id = c.s_id WHERE t_id = %s", (t_id,))

                list_cs = []

                for row in cur:
                    list_cs.append(course.TCourse(row[0], row[1], row[2], row[3],row[4]))

                return list_cs

    def add_c_to_t(self, c_object):

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:
                # Please use the appropriate database query for testing endpoint:
                # That is comment out the other ones

                # Jace's Database query:
                # cur.execute("INSERT INTO project2.courses (c_id, c_name, c_desc, s_id, t_id) "
                #             "VALUES (%s, %s, %s, %s, %s) RETURNING *",
                #             (c_object.c_id, c_object.c_name, c_object.c_desc,
                #              c_object.s_id, c_object.t_id))

                # Shushmita's Database query:
                cur.execute("INSERT INTO courses (c_id, c_name, c_desc, s_id, t_id) "
                            "VALUES (%s, %s, %s, %s, %s) RETURNING *",
                            (c_object.c_id, c_object.c_name, c_object.c_desc,
                             c_object.s_id, c_object.t_id))

                reimb_row_inserted = cur.fetchone()
                conn.commit()

                return course.Course(reimb_row_inserted[0], reimb_row_inserted[1], reimb_row_inserted[2],
                                     reimb_row_inserted[3], reimb_row_inserted[4])

    def update_c_by_ids_t(self, c_object):

        with psycopg.connect(host=config.get('host'), port=config.get('port'), dbname=config.get('dbname'),
                             user=config.get('user'), password=config.get('password')) as conn:


            with conn.cursor() as cur:
                # Please use the appropriate database query for testing endpoint:
                # That is comment out the other ones

                # Jace's Database query:
                # cur.execute("UPDATE project2.courses SET c_name = %s, c_desc = %s, t_id = %s "
                #             "WHERE c_id= %s AND s_id = %s RETURNING *",
                #             (c_object.c_name, c_object.c_desc, c_object.t_id))

                # Shushmita's Database query:
                cur.execute("UPDATE proj2_tgm.courses SET c_name = %s, c_desc = %s, t_id = %s "
                            "WHERE c_id= %s AND s_id = %s RETURNING *",
                            (c_object.c_name, c_object.c_desc, c_object.t_id))

                conn. commit()

                c_row_updated = cur.fetchone()
                if c_row_updated is None:
                    return None

                return course.Course(c_row_updated[0], c_row_updated[1], c_row_updated[2], c_row_updated[3],
                                     c_row_updated[4])
