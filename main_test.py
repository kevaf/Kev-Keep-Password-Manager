import unittest
from main import Users
from main import Credentials

class TestUsers(unittest.TestCase):
    
    """
    Test class that defines test cases for the Users class behaviours.
    """
    
    def setUp(self):
        """
        set up method to run before each test case
        """
        self.new_user = Users("kevaf", "kev1234")

    
    def test_init(self):
        """
        case to test if objects initialize correctly
        """
        self.assertEqual(self.new_user.main_user, "kevaf")
        self.assertEqual(self.new_user.main_password, "kev1234")
    
    def test_add_user(self):
        """
        test case to test if user has been added to user list
        """
        self.new_user.add_user() #saving a new user
        self.assertEqual(len(Users.users_list), 1)


class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Credentials class behaviours.
    """

    def setUp(self):
        """
        set up method to run before each test case on the TestCredentials class
        """
        self.new_credential = Credentials("Twitter", "KevOnEverything", "kev07")
    
    def tearDown(self):
        """
        tear down method that cleans up after each test is run
        """
        Credentials.credentials_list = []

    def test_initcred(self):
        """
        test case to check if new credentials initializes correctly
        """

        self.assertEqual(self.new_credential.account, "Twitter")
        self.assertEqual(self.new_credential.username, "KevOnEverything")
        self.assertEqual(self.new_credential.password, "kev07")
    
    def test_save_credential(self):
        """
        test case to test if new credential has been saved
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def test_multiple_save_credential(self):
        """
        test case to check if multiple credentials can be saved 
        """
        self.new_credential.save_credential()
        test_credential=Credentials("testacc", "testkev", "test123")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)





if __name__ == '__main__':
    unittest.main()