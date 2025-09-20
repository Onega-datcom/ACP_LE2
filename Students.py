class Student:
        def __init__(self, student_id, student_name, email, grades=None, courses=None):
        # 👉 initialize attributes here
                self.student_id = (id, name)
                self.student_name = student_name
                self.email = email
                self.grades = {subject:score}
                self.courses = {"IT211", "CS121", "CpE405", "CS211"}
                pass

        def __str__(self):
        # 👉 return formatted string of student info
                return (f"ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}" )
        
class StudentRecords:
        def __init__(self, students):
        # 👉 initialize empty list for students
        self.students = []
