import os
import psycopg
from datetime import datetime
from dotenv import dotenv_values
from model.assignment_model import Assignments, Sassignments, Tassignments

config = dotenv_values(".env")
import datetime

class AssignmentDao:

    current_time = datetime.datetime.now()
    print(current_time)

    def get_all_assignments_by_s_id(self, s_id):
        with psycopg.connect(host=os.getenv('db_url'), user=os.getenv('db_username'), password=os.getenv('db_password')) as conn:
            with conn.cursor() as cur:

                cur.execute("select a.assn,a.submitted,a.grade,a.grade_time,c.c_name from assignments a join courses c on a.c_id = c.c_id and c.s_id in (select s_id from courses  where courses.s_id = %s)", (s_id, ))

                assignment_list = []

                for row in cur:

                    my_assignment_obj = Sassignments(row[0], row[1], row[2], row[3], row[4])
                    assignment_list.append(my_assignment_obj)

                return assignment_list

    def get_all_assignments_by_c_id(self, s_id, c_id):
        with psycopg.connect(host=os.getenv('db_url'), user=os.getenv('db_username'), password=os.getenv('db_password')) as conn:
            with conn.cursor() as cur:
                cur.execute("select a.assn, a.submitted, a.grade, a.grade_time, c.c_name, c.c_desc, c.s_id from assignments a join courses c on a.c_id = c.c_id and c.c_id in(select c_id from courses  where courses.c_id = %s and courses.s_id = %s)", (c_id, s_id))

                assignment_list = []

                for row in cur:

                    my_assignment_obj = Sassignments(row[0], row[1], row[2], row[3], row[4])
                    assignment_list.append(my_assignment_obj)

                return assignment_list

    def add_assignments_to_c_id(self, s_id, c_id, a_object):
        with psycopg.connect(host=os.getenv('db_url'), user=os.getenv('db_username'), password=os.getenv('db_password')) as conn:

            with conn.cursor() as cur:
                cur.execute("select * from courses where s_id = %s and c_id = %s", (s_id, c_id))
                assignments_new = cur.fetchone()
                if assignments_new is None:
                    return None
                else:

                    cur.execute("INSERT INTO assignments (c_id, grade) VALUES (%s, %s) RETURNING *", (c_id, a_object.grade))

                assignment_row_inserted = cur.fetchone()
                conn.commit()

                return Assignments(assignment_row_inserted[0], assignment_row_inserted[1], assignment_row_inserted[2],
                                     assignment_row_inserted[3], assignment_row_inserted[4])

    def get_all_assignments_by_t_id(self, t_id):
        with psycopg.connect(host=os.getenv('db_url'), user=os.getenv('db_username'), password=os.getenv('db_password')) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "select a.assn,a.submitted,a.grade,a.grade_time,c.c_name from assignments a join courses c on "
                    "a.c_id = c.c_id and c.s_id in (select t_id from courses  where courses.t_id = %s)",
                    (t_id,))

                assignment_list = []

                for row in cur:
                    my_assignment_obj = Sassignments(row[0], row[1], row[2], row[3], row[4])
                    assignment_list.append(my_assignment_obj)

                return assignment_list



    def get_all_assignments_by_t_id_and_c_id(self, t_id, c_id):
        with psycopg.connect(host=os.getenv('db_url'), user=os.getenv('db_username'), password=os.getenv('db_password')) as conn:
                    with conn.cursor() as cur:
                        cur.execute("select a.assn, s.s_name, c.c_name,c.c_desc, a.submitted, a.grade, a.grade_time from "
                                    " assignments a inner join courses c on a.c_id = c.c_id "
                                    "inner join teachers t on t.t_id =c.t_id "
                                    "inner join students s on s.s_id = c.s_id "
                                    "where c.t_id = %s and c.c_id = %s order by s.s_name", (t_id, c_id))

                        assignment_list = []

                        for row in cur:

                            my_assignment_obj = Tassignments(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                            assignment_list.append(my_assignment_obj)

                        return assignment_list


    def update_assignments_by_c_id_and_a_id(self, t_id, c_id, assn, a_object):
        with psycopg.connect(host=os.getenv('db_url'), user=os.getenv('db_username'), password=os.getenv('db_password')) as conn:
            current_time = datetime.datetime.now()
            print(a_object.grade)
            # print(current_time)
            with conn.cursor() as cur:
                cur.execute("update assignments set grade = %s, grade_time = %s where assn = %s and c_id = %s returning *", (a_object.grade, current_time, assn, c_id))

                conn.commit()

                a_row_updated = cur.fetchone()
                if a_row_updated is None:
                    return None

                return Assignments(a_row_updated[0], a_row_updated[1], a_row_updated[2], a_row_updated[3],
                             a_row_updated[4])
