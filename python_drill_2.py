#
# Python:   3.7.1
#
# Author:   Jeff McClain
#
# Purpose:  The Tech Academy - Python Course Drill (pg103)
#           Write a script that creates a database and adds
#           new data into that database.

"""
            DRILL REQUIREMENTS:
            -Your script will need to use Python 3 and the sqlite3 module.
            -Your database will require 2 fields, an auto-increment primary integer field and a field with the data type of string.
            -Your script will need to read from the supplied list of file names at the bottom of this page and determine only the files from the list which ends with a “.txt” file extension.
            -Next, your script should add those file names from the list ending with “.txt” file extension within your database.
            -Finally, your script should legibly print the qualifying text files to the console.
"""


import os
import sqlite3

# create and connect to db
conn = sqlite3.connect('drill_2.db')
cur = conn.cursor()
# supplied list of files
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# declare list to store results of get_list()
txtList = []

# iterate through fileList, selecting '.txt' files and insert into new list
def get_list():
        for file in fileList:
            if file.endswith('.txt'):
                txtList.append(file)
        return txtList
get_list()
print('Your current list of ".txt" files: {}'.format(txtList))

# while connected to db- create table, commit to db, close db
with conn:    
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_drill( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT \
        )')
    conn.commit()
    # add file names to tbl_drill in db
    for entry in txtList:
        cur.execute('INSERT INTO tbl_drill(col_files) VALUES(?)',(entry,))
    conn.commit()
conn.close()


if __name__ == '__main__':
        get_list()




