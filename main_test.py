import unittest
from main import Users

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


if __name__ == '__main__':
    unittest.main()