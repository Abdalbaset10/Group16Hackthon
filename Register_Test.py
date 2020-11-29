import unittest
import Register
import csv

find_user_flag = 0

with open('data.csv', 'r') as data_file:
    for line in data_file:
        data = line.split(",")



class Test_find_User(unittest.TestCase):
    def test_user_exist(self):
        self.assertEqual(Register.find_user('315198564'),data[6],"should be True")


if __name__ == '__main__':
    unittest.main()
