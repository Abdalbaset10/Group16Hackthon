"""
User registeration :
"""


import csv

username = "Homeless"
password = "123456"
person = "123456789"


def find_user(x,y):
    find_user_flag = 0
    with open('data.csv', 'r') as data_file:
        for line in data_file:
            data = line.split(",")
            if data[3] == str(x) and data[2]==str(y):
                find_user_flag = 1
            else:
                print()
    if find_user_flag == 1:
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
