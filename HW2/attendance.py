import datetime
from user import User

class Attendance:
    def __init__(self, user, date, is_present):
        self._user = user
        self._date = date
        self._is_present = is_present

    @staticmethod
    def get_current_date():
        return datetime.datetime.now()

    def mark_attendance(self, is_present):
        self._is_present = is_present
        self._date = self.get_current_date()
        return f"Attendance marked for user {self._user.get_user_id()} on {self._date}. Present: {self._is_present}"