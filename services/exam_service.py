from database.connector import DBConnector
from entities.exam import Exam
from mysql.connector import Error



class ExamService:
    def __init__(self):
        self.db = DBConnector()

    # Create
    def create(self, exam):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = """
                    INSERT INTO exam(
                    student_id, exam_type,
                    exam_rank, exam_marks
                    )
                    VALUES(%s, %s, %s, %s)
                    """
            val = (exam.student_id, exam.exam_type,
                   exam.exam_rank, exam.exam_marks)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'create' in 'ExamService': {e}")
        finally:
            self.db.close(conn)

    # Read
    def read(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM exam WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            row = cursor.fetchone()
            if row:
                return Exam(*row)
            else:
                return None
        except Error as e:
            print(f"Error caused by 'read' in 'ExamService': {e}")
        finally:
            self.db.close(conn)


    # Update
    def update(self, exam):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = """
                    UPDATE exam SET 
                    exam_type = %s, exam_rank = %s,
                    exam_marks = %s
                    WHERE student_id = %s
                    """
            val = (exam.exam_type, exam.exam_rank,
                    exam.exam_marks, exam.student_id)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'update' in 'ExamService': {e}")
        finally:
            self.db.close(conn)

    # Delete
    def delete(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM exam WHERE student_id = %s"
            val = (student_id,)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'delete' in 'ExamService': {e}")
        finally:
            self.db.close(conn)



    # Read detials of all the students
    def read_all(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM exam"
            cursor.execute(sql)
            rows = cursor.fetchall()

            exams = []
            for row in rows:
                exam = Exam(student_id=row[0], exam_type=row[1], exam_rank=row[2], exam_marks=row[3])
                exams.append(exam)
            return exams
        except Error as e:
            print(f"Error caused by 'read_all' in 'ExamService': {e}")
        finally:
            self.db.close(conn)