from user import User

class Student(User):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)
        self._StudentID = user_id
        self._grade = {}
        self._schedule = {}
        self._payment_bill = {}
        self._payment_status = False

    def add_grade(self, course, grade):
        self._grade[course] = grade

    def view_grades(self):
        return self._grades
    
    def view_schedule(self):
        return self._schedule
    
    def view_payment_bill(self):
        return self._payment_bill
    
    def confirm_payment(self, payment):
        if payment:
            self._payment_status = True
        
    def view_payment_status(self):
        return self._payment_status