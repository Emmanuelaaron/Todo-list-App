import unittest
from users import Details

class UserDetails(unittest.TestCase):
    def setUp(self):
        self.users = Details()
    
    def test_creation(self):
        self. assertIsInstance(self.users, Details)

    def test_Pass_word(self):
        password = 'passWord9'
        # len(password) = 9
        self.assertTrue(self.users.pass_word_len(password)>4)
        self.assertTrue(self.users.password(any(c.isupper() for c in password)))
        self.assertTrue(self.users.password(any(c.islower() for c in password)))
        self.assertTrue(self.users.password(any(c.isdigit() for c in password)))

    def test_user_name(self):
        userName = "Emmanuel"
        name = "Emmanuelaaron"
        self.assertTrue(self.users.user_name_len(userName) > 4)
        self.assertTrue(self.users.userName(userName) is not self.users.name(name))

    # def test_Age_(self):
    #     self.assertTrue(self.oop.Age(age.isdigit()))
    #     self.assertTrue(self.oop.Age(age > 0))



