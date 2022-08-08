from datetime import datetime, timezone

import psycopg
from dotenv import dotenv_values

config = dotenv_values(".env")
import datetime

from model.assignment_model import Assignments, Sassignments

class AssignmentDao:

         # dt = datetime.now(timezone.utc)
    current_time = datetime.datetime.now()
  # print(dt1)
    print(current_time)

    def get_all_assignments_by_s_id(self, s_id):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'],
                             user=config['user'], password=config['password']) as conn:
            with conn.cursor() as cur:

                cur.execute("select a.assn,a.submitted,a.grade,a.grade_time,c.c_name from assignments a join courses c on a.c_id = c.c_id and c.s_id in (select s_id from courses  where courses.s_id = %s)", (s_id, ))

                assignment_list = []

                for row in cur:

                    my_assignment_obj = Sassignments(row[0], row[1], row[2], row[3], row[4])
                    assignment_list.append(my_assignment_obj)

                return assignment_list

    def get_all_assignments_by_c_id(self, s_id, c_id):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'],
                                     user=config['user'], password=config['password']) as conn:
            with conn.cursor() as cur:
                cur.execute("select a.assn, a.submitted, a.grade, a.grade_time, c.c_name, c.c_desc, c.s_id from assignments a join courses c on a.c_id = c.c_id and c.c_id in(select c_id from courses  where courses.c_id = %s and courses.s_id = %s)", (c_id, s_id))

                assignment_list = []

                for row in cur:

                    my_assignment_obj = Sassignments(row[0], row[1], row[2], row[3], row[4])
                    assignment_list.append(my_assignment_obj)

                return assignment_list

    def add_assignments_to_c_id(self, s_id, c_id, c_object):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'], user=config['user'],
                             password=config['password']) as conn:

            with conn.cursor() as cur:
                cur.execute("select * from courses where s_id = %s and c_id = %s", (s_id, c_id))
                assignments_new = cur.fetchone()
                if assignments_new is None:
                    return None
                else:

                    cur.execute("INSERT INTO assignments (c_id, grade) VALUES (%s, %s) RETURNING *", (c_id, c_object.grade))

                assignment_row_inserted = cur.fetchone()
                conn.commit()

                return Assignments(assignment_row_inserted[0], assignment_row_inserted[1], assignment_row_inserted[2],
                                     assignment_row_inserted[3], assignment_row_inserted[4])

    def update_assignments_by_c_id_and_a_id(self, t_id, c_id, a_id,  a_object):
        with psycopg.connect(host=config['host'], port=config['port'], dbname=config['dbname'], user=config['user'],
                             password=config['password']) as conn:
            current_time = datetime.datetime.now()
            print(a_object.grade)
            # print(current_time)
            with conn.cursor() as cur:
                cur.execute("update assignments set grade = %s, grade_time = %s where assn = %s and c_id = %s returning *", (a_object.grade, current_time, a_id, c_id))

                conn.commit()

                a_row_updated = cur.fetchone()
                if a_row_updated is None:
                    return None

                return Assignments(a_row_updated[0], a_row_updated[1], a_row_updated[2], a_row_updated[3],
                             a_row_updated[4])
