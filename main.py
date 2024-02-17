
from entities.student import Student
from services.student_service import StudentService
from entities.idproof import IDProof
from services.idproof_service import IDProofService
from entities.exam import Exam
from services.exam_service import ExamService
from entities.institution import Institution
from services.institution_service import InstitutionService
import os



class Main:
    def __init__(self):
        self.student_service = StudentService()
        self.id_proof_service = IDProofService()
        self.exam_service = ExamService()
        self.institution_service = InstitutionService()
        self.menu = {
            1: self.student_menu,
            2: self.idproof_menu,
            3: self.exam_menu,
            4: self.institution_menu,
            5: self.exit_program
        }


    def run(self):
        while True:
            os.system("clear")
            self.design("STUDENT MANAGEMENT SYSTEM")
            print("Choose any one")
            print(f"{1} Student Menu")
            print(f"{2} ID Proof Menu")
            print(f"{3} Exam Menu")
            print(f"{4} Institution Menu")
            print(f"{5} Exit Program")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 5:
                    self.menu[choice]()
                    break
                elif choice in self.menu:
                    self.menu[choice]()
                else:
                    print("Invalid Choice")
            except ValueError as e:
                print(f"Please enter a valid choice: {e}")


    # Student menu
    def student_menu(self):
        while True:
            os.system("clear")
            self.design("STUDENT MENU")
            print("Choose any one")
            print(f"{1} Add students")
            print(f"{2} Search by student id")
            print(f"{3} Display all the students")
            print(f"{4} Update details of students")
            print(f"{5} Delete a student")
            print(f"{6} Return to 'Main Menu'")
            

            choice_mapping = {
                1: self.add_students,
                2: self.search_student_by_id,
                3: self.print_all_students,
                4: self.update_student,
                5: self.delete_student,
                6: self.exit_program
            }

            try:
                choice = int(input("Enter your choice: "))
                if choice == 6:
                    choice_mapping[choice]()
                    break
                elif choice in choice_mapping:
                    choice_mapping[choice]()
                else:
                    print("Invalid choice range(1-6)")
            except ValueError:
                print("Invalid input, please enter a valid input")
    

    # ID proof menu
    def idproof_menu(self):
        while True:
            os.system("clear")
            self.design("STUDENT ID PROOF MENU")
            print("Select any one")
            print(f"{1} Add ID proof")
            print(f"{2} Search by ID proof")
            print(f"{3} Display all ID proofs")
            print(f"{4} Delete ID proof")
            print(f"{5} Return to 'Main Menu'")

            choice_mapping = {
                1: self.add_id_proof,
                2: self.search_id_proof_by_id,
                3: self.print_all_id_proofs,
                4: self.delete_idproof,
                5: self.exit_program
            }

            try:
                choice = int(input("Enter your choice: "))
                if choice == 5:
                    choice_mapping[choice]()
                    break
                elif choice in choice_mapping:
                    choice_mapping[choice]()
                else:
                    print("Invalid choice range(1-5)")
            except ValueError:
                print("Invalid input, please enter a valid input")



    # Exam menu
    def exam_menu(self):
            while True:
                os.system("clear")
                self.design("STUDENT EXAM MENU")
                print("Select any one")
                print(f"{1} Add exam")
                print(f"{2} Search exam")
                print(f"{3} Display all exam")
                print(f"{4} Update exam")
                print(f"{5} Delete exam")
                print(f"{6} Return to 'Main Menu'")

                choice_mapping = {
                    1: self.add_exam,
                    2: self.search_exam_by_student_id,
                    3: self.print_all_exams,
                    4: self.update_exam,
                    5: self.delete_exam,
                    6: self.exit_program
                }

                try:
                    choice = int(input("Enter your choice: "))
                    if choice == 6:
                        choice_mapping[choice]()
                        break
                    elif choice in choice_mapping:
                        choice_mapping[choice]()
                    else:
                        print("Invalid choice range(1-6)")
                except ValueError:
                    print("Invalid input, please enter a valid input")

    # Institution menu
    def institution_menu(self):
        while True:
            os.system("clear")
            self.design("STUDENT'S INSTITUTION MENU")
            print("Choose any one")
            print(f"{1} Add institution")
            print(f"{2} Search institution by student id")
            print(f"{3} Display all the institutions")
            print(f"{4} Update details of institutions")
            print(f"{5} Delete institution")
            print(f"{6} Return to 'Main Menu'")
            

            choice_mapping = {
                1: self.add_institutions,
                2: self.search_insittution_by_student_id,
                3: self.print_all_institutions,
                4: self.update_institution,
                5: self.delete_institution,
                6: self.exit_program
            }

            try:
                choice = int(input("Enter your choice: "))
                if choice == 6:
                    choice_mapping[choice]()
                    break
                elif choice in choice_mapping:
                    choice_mapping[choice]()
                else:
                    print("Invalid choice range(1-6)")
            except ValueError:
                print("Invalid input, please enter a valid input")
    


    def design(self, message):
        columns, _ = os.get_terminal_size()
        center = (columns - len(message)) // 8
        center_line = '=' * (center * 4)
        print(f'{center_line}\n{center * " "}{message}\n{center_line}')



            

    # ++++++++++++++++++++++++++++++++ STUDENT ENTITY ++++++++++++++++++++++++++++++++++++
    # Add n number of students
    def add_students(self):
        num_students = int(input("Enter number of students to add: "))
        student_details = [
        (
            int(input("Enter student id: ")),
            input("Enter first name: "),
            input("Enter last name: "),
            input("Enter locality: "),
            input("Enter district: "),
            input("Enter city: "),
            input("Enter state: ")
        )
        for _ in range(num_students)
    ]
    
        for student_detail in student_details:
            student = Student(*student_detail)
            self.student_service.create(student)

    # Search for a student
    def search_student_by_id(self):
        student_id_to_search = int(input("Search by student's id: "))
        found_student = self.student_service.read(student_id_to_search)
        if found_student:
            self.print_students(list([found_student]))
        else:
            print(f"Didn't found a student with student id {student_id_to_search}")
    
    # Print details of student
    def print_students(self, students):
        for student in students:
            print(f"\nStudent ID: {student.student_id}, First Name: {student.student_fname}")
            print(f"Last Name: {student.student_lname}, Locality: {student.student_locality}")
            print(f"District: {student.student_district}, City: {student.student_city}")
            print(f"State: {student.student_state}", end="\n\n")

    # Print all students
    def print_all_students(self):
        all_students = self.student_service.read_all()
        self.print_students(all_students)

    # Update student
    def update_student(self):
        student_id_to_search = int(input("Search by student's id: "))
        found_student = self.student_service.read(student_id_to_search)
        if found_student:
            found_student.student_fname = input("Enter new first name: ")
            found_student.student_lname = input("Enter new last name: ")
            found_student.student_locality = input("Enter new locality: ")
            found_student.student_district = input("Enter new district: ")
            # Update details
            self.student_service.update(found_student)
            print("\nUpdated details")
            self.print_students(list([found_student]))
        else:
            print(f"Didn't found a student with student id {student_id_to_search}")
    
    # Delete student
    def delete_student(self):
        student_id = int(input("Enter student ID: "))
        your_choice = int(input("\nDo you wanna to delete this students?(1/0): "))
        if your_choice:
            self.student_service.delete(student_id)
            print(f"Student deleated sucessfully!")
        else:
            pass





    # ++++++++++++++++++++++++++++++++ IDPROOF ENTITY ++++++++++++++++++++++++++++++++++++
    # Add n number of id proofs
    def add_id_proof(self):
        num_id_proofs = int(input("Enter number of id proofs to add: "))
        id_proof_details = [
        (
            int(input("Enter student ID number: ")),
            input("ID type: "),
            input("ID expiry date: "),
            input("Studnets ID: "),
        )
        for _ in range(num_id_proofs)
    ]
    
        for id_proof_detail in id_proof_details:
            id_proof = IDProof(*id_proof_detail)
            self.id_proof_service.create(id_proof)

    # Search by id proof
    def search_id_proof_by_id(self):
        idproof_id = int(input("Search ID by ID number: "))
        found_idproof = self.id_proof_service.read(idproof_id)
        if found_idproof:
            self.print_id_proofs(list([found_idproof]))
        else:
            print(f"Didn't found ID proof with ID number {idproof_id}")
    

    # Print all id proofs
    def print_all_id_proofs(self):
        all_id_proofs = self.id_proof_service.read_all()
        self.print_id_proofs(all_id_proofs)


    # Print details of id proofs
    def print_id_proofs(self, id_proofs):
        for id_proof in id_proofs:
            print(f"\nID Number: {id_proof.id_number}, ID Type: {id_proof.id_type}")
            print(f"ID Expiry Date: {id_proof.id_expiry_date}, Student ID: {id_proof.student_id}", end="\n")

    # Delete idproof
    def delete_idproof(self):
        id_number = int(input("Enter ID number: "))
        your_choice = int(input("\nDo you wanna to delete this ID proof?(1/0): "))
        if your_choice:
            self.id_proof_service.delete(id_number)
            print(f"ID proof deleated sucessfully!")
        else:
            pass


    # ++++++++++++++++++++++++++++++++ EXAM ENTITY ++++++++++++++++++++++++++++++++++++
    # Add n number of exams
    def add_exam(self):
        num_exams = int(input("Enter number of exams to add: "))
        exam_details = [
        (
            int(input("Enter student id: ")),
            input("Enter exam type: "),
            int(input("Enter rank: ")),
            int(input("Enter exam marks: ")),
        )
        for _ in range(num_exams)
    ]
    
        for exam_detail in exam_details:
            exam = Exam(*exam_detail)
            self.exam_service.create(exam)

    # Search for exam
    def search_exam_by_student_id(self):
        student_id_to_search = int(input("Search by student's id: "))
        found_student = self.exam_service.read(student_id_to_search)
        if found_student:
            self.print_exam(list([found_student]))
        else:
            print(f"Didn't found a student with student id {student_id_to_search}")
    
    # Print details of exams
    def print_exam(self, exams):
        for exam in exams:
            print(f"\nStudent ID: {exam.student_id}, Exam Type: {exam.exam_type}")
            print(f"Exam Rank: {exam.exam_rank}, Exam Marks: {exam.exam_marks}", end="\n")

    # Print all exams
    def print_all_exams(self):
        all_exams = self.exam_service.read_all()
        self.print_exam(all_exams)

    # Update exam
    def update_exam(self):
        student_id_to_search = int(input("Search by student's id: "))
        found_exam = self.exam_service.read(student_id_to_search)
        if found_exam:
            found_exam.exam_type = input("Enter new exam type: ")
            found_exam.exam_rank = input("Enter new exam rank: ")
            found_exam.exam_marks = input("Enter new exam marks: ")
            # Update details
            self.exam_service.update(found_exam)
            print("\nUpdated details")
            self.print_exam(list([found_exam]))
        else:
            print(f"Didn't found a student with student id {student_id_to_search}")
    
    # Delete exam
    def delete_exam(self):
        student_id = int(input("Enter student ID: "))
        your_choice = int(input("\nDo you wanna to delete this exam?(1/0): "))
        if your_choice:
            self.exam_service.delete(student_id)
            print(f"Exam deleated sucessfully!")
        else:
            pass



    # ++++++++++++++++++++++++++++++++ INSTITUTION ENTITY ++++++++++++++++++++++++++++++++++++
        """
        student_id
        present_class
        name_of_school

        """
    # Add n number of institutions
    def add_institutions(self):
        num_institutions = int(input("Enter number of institutions to add: "))
        institution_details = [
        (
            int(input("Enter student id: ")),
            input("Enter present class: "),
            input("Enter name of school: "),
        )
        for _ in range(num_institutions)
    ]
    
        for institution_detail in institution_details:
            institution = Institution(*institution_detail)
            self.institution_service.create(institution)
    

    # Search for an institution
    def search_insittution_by_student_id(self):
        student_id_to_search = int(input("Search institution by student's id: "))
        found_institution = self.institution_service.read(student_id_to_search)
        if found_institution:
            self.print_institution(list([found_institution]))
        else:
            print(f"Didn't found an institution with student id {student_id_to_search}")
    
    # Print details of institution
    def print_institution(self, institutions):
        for institution in institutions:
            print(f"\nStudent ID: {institution.student_id}, Present Class: {institution.present_class}")
            print(f"Last Name: {institution.name_of_school}", end="\n\n")

    # Print all institution
    def print_all_institutions(self):
        all_institutions = self.institution_service.read_all()
        self.print_institution(all_institutions)


    # Update institution
    def update_institution(self):
        student_id_to_search = int(input("Search by student's id: "))
        found_institution = self.institution_service.read(student_id_to_search)
        if found_institution:
            found_institution.present_class = input("Enter new present class: ")
            found_institution.name_of_school = input("Enter new name of school: ")
            # Update details
            self.institution_service.update(found_institution)
            print(f"\nUpdated details are:")
            self.print_institution(list([found_institution]))
        else:
            print(f"Didn't found a student with student id {student_id_to_search}")
    
    # Delete student
    def delete_institution(self):
        student_id = int(input("Enter student ID: "))
        your_choice = int(input("\nDo you wanna to delete this institution?(1/0): "))
        if your_choice:
            self.institution_service.delete(student_id)
            print(f"Institution deleated sucessfully!")
        else:
            pass


    # Exit program
    def exit_program(self):
        print("Exiting program")






    

if __name__ == "__main__":
    main = Main()
    main.run()