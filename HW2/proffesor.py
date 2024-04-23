from user import User
from student import Student
from course import Course
from attendance import Attendance

class Dosen(User):
    def __init__ (self, user_id, password) -> None:
        super()._init_(user_id, password)
        self._dosenid = user_id
        self._course = []

    def add_course(self, course):
        self._course.append(course)
        return self._course

    def input_attendance(self, course, student, attendance_status):
        attendance = Attendance(course, student, attendance_status)
        return attendance

    def input_grade(self, student, course,grade):
        if not isinstance(student, Student):
            raise ValueError("Invalid student object")
        student.add_grade(course, grade)

    def update_schedule(self, student, new_schedule):
        if not isinstance(student, Student):
            raise ValueError("Invalid student object")
        student.update_schedule(new_schedule)