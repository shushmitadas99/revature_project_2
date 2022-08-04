import psycopg
from dotenv import dotenv_values

config = dotenv_values(".env")
from model.assignment_model import Assignment


class AssignmentDao:
    def get_all_assignments_by_username_and_course_id(self, course_id):
        with psycopg.connect(host=config['host'], port=config['port'], dname=config['dbname'],
                             user=config['user'], password=config['password']) as conn:
           with conn.cursor() as cur:
               cur.execute("select assignments.assn,assignments.submitted,assignments.grade,assignments.grade_time,"
                           "courses.c_name,courses.c_desc,courses.s_id from assignments  join courses"
                           " on assignments.c_id=courses.c_id and courses.s_id in(select s_id from courses"
                           "  where courses.c_id = %s);", (course_id, ));

               assignment_list = []

               for row in cur:
                assignment_list.append(Assignment(row[0], row[1], row[2], row[3]))

                return assignment_list
