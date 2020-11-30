"""
User registeration :
"""


import csv

username = "Homeless"
password = "123456"
person = "123456789"
ID ="2354531"

def find_user(x,y):
    AccessGrant = 0
    with open('data.csv', 'r') as data_file:
        for line in data_file:
            data = line.split(",")
            if data[0] == str(x):
                if data[1]== str(y):
                    AccessGrant = 1

    if AccessGrant == 1:
        return 1
    else:
        return 0


z = find_user(username,password)


def grantaccess(x):
    if x == 1:
        print("access granted")
    else:
        print("access denied")


grantaccess(z)
