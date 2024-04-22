import datetime
from user import User

class Attendance(User):
    def __init__(self, user_id, password, date, Absent):
        super()._init_(user_id, password)
        self._date = date
        self._Absent = Absent

    @staticmethod
    def get_current_date():
        return datetime.datetime.now()

    def mark_attendance(self, user_id):
        date = self.get_current_date()
        return f"Attendance marked for user {user_id} on {date}"