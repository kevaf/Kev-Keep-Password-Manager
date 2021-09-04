
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

    @classmethod
    def show_users(cls):
        return cls.users_list


class Credentials:

    credentials_list =[]

    def __init__(self, account, username, password):

        self.account = account
        self.username = username
        self.password = password

    @classmethod
    def confirm_user(cls, main_user, main_password):
        """
        method to check if selection matches object in user list
        """
        current_user = ""

        for user in Users.users_list:
        
            if (user.main_user == main_user and user.main_password==main_password):
                current_user==user.main_user
        
        return current_user

    
