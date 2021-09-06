import random
import string

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
    def confirm_user(cls, main_user, main_password):
        """
        method to check if selection matches object in user list
        """
        current_user = ""

        for user in Users.users_list:
        
            if (user.main_user == main_user and user.main_password==main_password):
                current_user=user.main_user
        
        return current_user


    @classmethod
    def show_users(cls):
        return cls.users_list


class Credentials:

    credentials_list =[]

    def __init__(self, account, username, password):

        self.account = account
        self.username = username
        self.password = password

    

    def save_credential(self):
        """
        Method to add new credentials to credentials lists
        """
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        """
        Method that removes a credential from credentials lists 
        """

        Credentials.credentials_list.remove(self)
    

    @classmethod
    def find_by_account(cls, account):
        """
        method to search for credential details by account name
        """

        for cred in cls.credentials_list:
            if (cred.account == account):
                return cred
    
    @classmethod
    def display_credentials(cls):
        '''
        Class method to display the list of saved credentials
        '''
        return cls.credentials_list


    def create_random_password(length=10):
        """
        method to auto generate password for users
        """

        password = string.ascii_lowercase + string.digits + string.ascii_uppercase + "':@!#$%^&*"
        return ''.join(random.choice(password) for _ in range(length))

    # @classmethod
    # def display_credentials(self):
    #     """
        
    #     """
    # pass