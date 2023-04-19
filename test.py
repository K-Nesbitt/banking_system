import unittest
import mysql.connector
from main import account_exists, acct_details

# def is_int(x):
#     return type(x)== int

class TestQuerys(unittest.TestCase):
    # def test_is_integer(self):
    #     self.assertTrue(is_int(3))

    def test_account_exists(self):
        conn = mysql.connector.connect(host = 'localhost',
                                database = 'example',
                                user = 'root',
                                password = 'Y+kTRisJ')

        self.assertTrue(account_exists(connection=conn, acct_num=1234567))
        conn.close()

    def test_account_not_exists(self):
        conn = mysql.connector.connect(host = 'localhost',
                                database = 'example',
                                user = 'root',
                                password = 'Y+kTRisJ')

        self.assertFalse(account_exists(connection=conn, acct_num= 1111111))
        conn.close()

    def test_no_acct_details(self):
        conn = mysql.connector.connect(host = 'localhost',
                                database = 'example',
                                user = 'root',
                                password = 'Y+kTRisJ')

        self.assertEqual(acct_details(connection=conn, 
                                       acct_info=(1111111, 1111)), 
                                       None)
        
        conn.close()

if __name__ == '__main__':

    unittest.main()