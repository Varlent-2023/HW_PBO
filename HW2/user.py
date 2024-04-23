class User:
    def __init__(self, user_id, password, user_type):
        if not isinstance(user_id, str) or not isinstance(password, str) or not isinstance(user_type, str):
            raise ValueError("user_id, password, and user_type must be strings")
        self._user_id = user_id
        self._password = password
        self._user_type = user_type

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            return True
        else:
            return False

    def get_user_id(self):
        return self._user_id
    
    def logout(self):
        return False
    
    def get_user_type(self):
        return self._user_type
