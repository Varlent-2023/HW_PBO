from user import User
from payment import Billing
from student import Student
from proffesor import Dosen

class Operator(User):
    def __init__ (self, user_id, password) -> None:
        super().__init__(user_id, password)
        self._operatorid = user_id

    def createBilling(self, *args):
        new_bill = Billing (*args)
        return new_bill

    def create_user_account(self, user_id, user_type, *args):  
        if user_type == "student":
            return Student(*args)
        elif user_type == "Dosen":
            return Dosen(*args)
        elif user_type == "operator":
            pass
        else:
            return None
        
    def confirm_payment(self, student, payment):
        if not isinstance(student, Student):
            raise ValueError("Invalid student object")
        student.confirm_payment(payment)
