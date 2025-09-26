class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.name_id = (student_id, student_name)
        self.email = email 
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else set() 

    def __str__(self):
        return (f"Student ID: {self.name_id[0]}, "
                f"Student Name: {self.name_id[1]}, Email: {self.email}, "
                f"Student Grades: {self.grades if self.grades is not None else "None"}, "
                f"Courses: {self.courses if self.courses is not None else "None"}") 
    
    def calculate_gpa(self):
        if not self.grades:
            return None
        total = 0
        count = 0

        for score in self.grades.values():
            if isinstance(score, str):
                grade = score.upper()
                gpa = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}.get(grade, 0.0)
            else:
                if score >= 90:
                    gpa = 4.0
                elif score >= 80:
                    gpa = 3.0
                elif score >= 70:
                    gpa = 2.0
                elif score >= 60:
                    gpa = 1.0
                else:
                    gpa = 0.0
            total += gpa
            count += 1
        return round(total / count, 2) if count else None

class StudentRecords:
    def __init__(self):
        self.students = []
    
    def add_student(self, student_id, student_name, email, grades=None, courses=None):

        newstudent = Student(student_id, student_name, email, grades, courses)
        self.students.append(newstudent)
        
        return "Student added successfully"

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.name_id[0] == student_id:
                if email:
                    student.email = email 
                if grades:
                    student.grades = grades 
                if courses:
                    student.courses = courses
                return "Student updated successfully"
            return "Student not found"

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.name_id[0] == student_id:
                del self.students[i]
                return "Student deleted successfully"
        return "Student not found"

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.name_id[0] == student_id:
                student.courses.add(course)
                return "Course added successfully"
            return "Student not found"

    def search_student(self, student_id):
        for student in self.students: 
            if student.name_id[0] == student_id:
                return str(student)
            return "Student not found"

    def search_by_name(self, name):
        for student in self.students:
            if student.name_id[0] == name:
                student.courses.add(self.course)
                return "Course enrolled successfully"
        return "Student not found"

    def search_student(self, student_id):
        for student in self.students:
            if student.name_id[0] == student_id:
                return str(student)
        return "Student not found"

    def search_by_name(self, name):
        name = name.lower
        matches = [str(s) for s in self.students if name in s.name_id[1].lower()]
        return matches if matches else ["No matching students found"]
    
if __name__ == "__main__":
    records = StudentRecords()
    print(records.add_student(12345, "Cj", "12345@gmail.com"))
    print(records.update_student(12345,
    email="cj_123@gmail.com",
    grades={"ACP": "B", "OOP": "C","PATHfit": "A"},
    courses={"ACP", "OOP", "PATHFit"})) 
    print(records.search_student(12345))
    print(records.add_student(67890, "Onera", "Onera@gmail.com", {"ACP": "B", "OOP": "C"}, {"ACP", "OOP"}))
    print("Cj's GPA:", [student.calculate_gpa() for student in records.students if student.name_id[0] == 12345][0])
    print("Onera's GPA:", [student.calculate_gpa() for student in records.students if student.name_id[0] == 67890][0])
    print(records.delete_student(67890))
