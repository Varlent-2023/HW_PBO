from user import User
from operator import Operator
from student import Student
from proffesor import Dosen
from payment import Billing
from course import Course
from attendance import Attendance

def main():
    operator = Operator("Admin", "adminpass")

    student = operator.create_user_account("4220230","studentpass", "E1234", "student")
    student1 = operator.create_user_account("4220231", "testtest", "student")
    professor = operator.create_user_account("2023", "F5678", "professor")

    # Courses
    dsp_course = Course("siwp1001", "Algorithma", "Introduction to programing and algorithms fundamental")
    pbo_course = Course("siwp2005", "PBO", "object oriented programming")

    #Enroll student and assign professor
    if student:
        student.enroll_in_course(dsp_course)
    if student1:
        student1.enroll_in_course(pbo_course)
    if professor:
        professor.teach_course(pbo_course)

    # Polymorphism
    for user in [student, student1, professor]:
        if user:
            login_status = user.login(user.get_user_id(), 'studentpass')
            print(f"User {user.get_user_id()} can log in: {login_status}")
            if isinstance(user, Student):
                user.set_grade('90')  # Set grade for student
                user.set_bill('5.000.000')  # Set bill for student
                print(f"Student {user.get_user_id()} memiliki nilai {user.get_grade()}")
                print(f"Student {user.get_user_id()} memiliki tagihan {user.get_bill()}")
                if dsp_course in user.get_courses():
                    print(f"Student {user.get_user_id()} berhasil enroll course {dsp_course.course_name}")
            elif isinstance(user, Dosen):
                print(f"Dosen {user.get_user_id()} berhasil login")

if __name__ == "__main__":
    main()
