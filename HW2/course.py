from user import User

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, user):
        if not isinstance(user, User):
            raise ValueError("Invalid user object")
        if user not in self.students:
            self.students.append(user)
            return f"Student with user id {user.get_user_id()} has been enrolled in {self.course_name}."
        else:
            return f"Student with user id {user.get_user_id()} is already enrolled in {self.course_name}."

    def unenroll_student(self, user):
        if not isinstance(user, User):
            raise ValueError("Invalid user object")
        if user in self.students:
            self.students.remove(user)
            return f"Student with user id {user.get_user_id()} has been unenrolled from {self.course_name}."
        else:
            raise ValueError(f"Student with user id {user.get_user_id()} is not enrolled in {self.course_name}.")