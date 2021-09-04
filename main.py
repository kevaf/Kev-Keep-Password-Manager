
class Users:
    """
    Class that generates new instances of Users
    """
    users_list = []

    def __init__(self, main_user, main_password):
        
        self.main_user = main_user
        self.main_password = main_password
    
    def add_user(self):
        """
        method that adds a new user object to users
        """
        Users.users_list.append(self)

