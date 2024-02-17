
from mysql.connector import Error
from database.connector import DBConnector
from entities.idproof import IDProof


class IDProofService:
    def __init__(self):
        self.db = DBConnector()

    #Create
    def create(self, id_proof):
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            sql = """
                    INSERT INTO idproof(
                    id_number, id_type, 
                    id_expiry_date, student_id
                    )
                    VALUES(%s, %s, %s, %s)
                    """
            val = (id_proof.id_number, id_proof.id_type, id_proof.id_expiry_date, id_proof.student_id)
            cursor.execute(sql, val)
            conn.commit()

        except Error as e:
            print(f"Error caused by 'create' in 'IDProofService': {e}")
        finally:
            self.db.close(conn)

    # Read
    def read(self, id_number):
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            sql = "SELECT * FROM idproof WHERE id_number = %s"
            cursor.execute(sql, (id_number,))
            row = cursor.fetchone()
            if row:
                return IDProof(*row)
            else:
                return None
        except Error as e:
            print(f"Error caused by 'read' in 'IDProofService': {e}")
        finally:
            self.db.close(conn)
        
            
    # Delete
    def delete(self, id_number):
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            sql = "DELETE FROM idproof WHERE id_number = %s"
            val = (id_number,)
            cursor.execute(sql, val)
            conn.commit()
        except Error as e:
            print(f"Error caused by 'delete' in 'IDProofService': {e}")
        finally:
            self.db.close(conn)

    # Read all
    def read_all(self):
        conn = self.db.connect()
        cursor = conn.cursor()

        try:
            sql = "SELECT * FROM idproof"
            cursor.execute(sql)
            rows = cursor.fetchall()

            id_proofs = []
            for row in rows:
                id_proof = IDProof(id_number=row[0], id_type=row[1], id_expiry_date=row[2], student_id=row[3])
                id_proofs.append(id_proof)
            return id_proofs
        except Error as e:
            print("Error caused by 'read_all' in 'IDProofService': {e}")
        finally:
            self.db.close(conn)


