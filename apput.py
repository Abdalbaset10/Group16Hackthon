import unittest
import pyrebase
import os
import sys
import time
import os.path as op
from functools import partial
from kivy.clock import Clock
from kivy.tests.common import GraphicUnitTest
from kivy.uix.screenmanager import Screen

firebaseConfig = {
            'apiKey': "AIzaSyAxS1KDjH4OQrbw-k050yGJHQ8giCuyFDU",
            'authDomain': "project16-f346d.firebaseapp.com",
            'databaseURL': "https://project16-f346d-default-rtdb.firebaseio.com/",
            'projectId': "project16-f346d",
            'storageBucket': "project16-f346d.appspot.com",
            'messagingSenderId': "237946682699",
            'appId': "1:237946682699:web:59b0610e150f5c42b7bcce",
            'measurementId': "G-W8TSC422XT"}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

class FinduseTestCase(unittest.TestCase):
    def test_userid(self):
        from myapp import find_user
        self.assertEqual(1,find_user('209102250'),"User in the data base")
        self.assertEqual(0, find_user('1111111'),"User is not in the data base")

    def test_username(self):
        from myapp import username_exist
        self.assertEqual(1,username_exist('moradM'),"user name exists in data base")
        self.assertEqual(0, username_exist('ZZZZZ'),"user name doesnt exist in data base")

    def test_granaccess(self):
        from myapp import grantAccess
        self.assertEqual(1,grantAccess('abd10','123456'),"Grant access")
        self.assertEqual(0, grantAccess('abd10', '6548'), "Wrong password")

    def test_currentuser(self):
        from myapp import currentUser
        self.assertEqual('209102250',currentUser('abd10'),"returned the username ")
        self.assertNotEqual('123456',currentUser('abd10'),"not the username of this id")

class myScreen(Screen):
    from myapp import MyProfile
    def __init__(self,**kwargs):
        super()




if __name__ == '__main__':
    unittest.main()
