import unittest
import mysql.connector
from main import account_exists

def is_int(x):
    return type(x)== int

class TestQuerys(unittest.TestCase):
    def test_is_integer(self):
        self.assertTrue(is_int(3))

    def test_account_exists(self):
        connection = mysql.connector.connect(host = 'localhost',
                                        database = 'example',
                                        user = 'root',
                                        password = 'Y+kTRisJ')
        acct_num = 1111111
        self.assertFalse(account_exists(connection, acct_num))


if __name__ == '__main__':

    unittest.main()