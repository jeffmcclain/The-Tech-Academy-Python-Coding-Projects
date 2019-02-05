#
# Python:   3.7.1
#
# Author:   Jeff McClain
#
# Purpose:  The Tech Academy - Python Course Drill (pg100)
#           Write a script that will check a specific folder on the
#           hard drive, verify whether those files end with a ".txt"
#           file extensions and if they do, print those qualifying
#           file names and their corresponding modified time-stamps
#           to the console.

"""
        DRILL OBJECTIVES:
        -Your script will need to use Python 3 and the OS module.
        -Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.
        -Your script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
        -Your script will need to use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.
        -Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the console.
"""



import os
from datetime import datetime




dPath = 'C:\\Users\\Jefe\\myProjects\\Python\\The-Tech-Academy-Python-Coding-Projects\\dir_drill_1'
fList = os.listdir(dPath)


def get_list():
    for file in fList:
        if file.endswith('.txt'):
            txtList = os.path.join(dPath,file)
            time = datetime.fromtimestamp(os.path.getmtime(txtList))
            print('{} {}'.format(txtList,time))
            



    
if __name__ == '__main__':
    get_list()


    
    


















#if __name__ == '__main__':


