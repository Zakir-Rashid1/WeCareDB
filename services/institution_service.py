from database.connector import DBConnector
from entities.institution import Institution
from mysql.connector import Error

class InstitutionService:
    def __init__(self):
        self.db = DBConnector()


    # Create
    def create(self, institution):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = """
                    INSERT INTO institution(
                    student_id, present_class,
                    name_of_school
                    )
                    VALUES(%s, %s, %s)
                    """
            val = (institution.student_id, institution.present_class, institution.name_of_school)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'create' 'InstitutionService': {e}")
        finally:
            self.db.close(conn)

    # Read
    def read(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM institution WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            row = cursor.fetchone()
            if row:
                return Institution(*row)
            else:
                return None
        except Error as e:
            print(f"Error caused by 'read' in 'InstitutionService': {e}")
        finally:
            self.db.close(conn)

    # Update
    def update(self, institution):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = """
                    UPDATE institution SET 
                    present_class = %s, name_of_school = %s
                    WHERE student_id = %s
                    """
            val = (institution.present_class, institution.name_of_school, institution.student_id)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'update' in 'InsitutionService': {e}")
        finally:
            self.db.close(conn)

    # Delete
    def delete(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "DELETE FROM institution WHERE student_id = %s"
            val = (student_id,)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'delete' in 'InstitutionService': {e}")
        finally:
            self.db.close(conn)



    # Read detials of all the students
    def read_all(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            sql = "SELECT * FROM institution"
            cursor.execute(sql)
            rows = cursor.fetchall()

            institutions = []
            for row in rows:
                institution = Institution(student_id=row[0], present_class=row[1], name_of_school=row[2])
                institutions.append(institution)
            return institutions
        except Error as e:
            print(f"Error caused by 'read_all' in 'InstitutionService': {e}")
        finally:
            self.db.close(conn)
            

