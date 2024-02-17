from mysql.connector import Error
from entities.student import Student
from database.connector import DBConnector

class StudentService:
    def __init__(self):
        self.db = DBConnector()

    # Create
    def create(self, student):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = """
                    INSERT INTO student(
                    student_id, student_fname,
                    student_lname, student_locality,
                    student_district, student_city,
                    student_state
                    )
                    VALUES(%s, %s, %s, %s, %s, %s, %s)
                    """
            val = (student.student_id, student.student_fname, student.student_lname,
                   student.student_locality, student.student_district, student.student_city, student.student_state)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'create' 'ExamService': {e}")
        finally:
            self.db.close(conn)

    # Read
    def read(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM student WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            row = cursor.fetchone()
            if row:
                return Student(*row)
            else:
                return None
        except Error as e:
            print(f"Error caused by 'read' in 'StudentService': {e}")
        finally:
            self.db.close(conn)

    # Update
    def update(self, student):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = """
                    UPDATE student SET 
                    student_fname = %s, student_lname = %s,
                    student_locality = %s, student_district = %s
                    WHERE student_id = %s
                    """
            val = (student.student_fname, student.student_lname,
                student.student_locality, student.student_district, student.student_id)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'update' in 'StudentService': {e}")
        finally:
            self.db.close(conn)

    # Delete
    def delete(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM student WHERE student_id = %s"
            val = (student_id,)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'delete' in 'StudentService': {e}")
        finally:
            self.db.close(conn)



    # Read detials of all the students
    def read_all(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM student"
            cursor.execute(sql)
            rows = cursor.fetchall()

            students = []
            for row in rows:
                student = Student(student_id=row[0], student_fname=row[1], student_lname=row[2], student_locality=row[3],
                                   student_district=row[4], student_city=row[5], student_state=row[6])
                students.append(student)
            return students
        except Error as e:
            print(f"Error caused by 'read_all' in 'StudentService': {e}")
        finally:
            self.db.close(conn)
            
