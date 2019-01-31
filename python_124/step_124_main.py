# Python Version:   3.7.1
#
# Author:           Jeff McClain
#
# Description:      - Python Drill Step 124 -
#                   Write a script that provides the user with a GUI that
#                   includes two buttons allowing the user to browse their
#                   system and select a source directory and desitnation
#                   directory- showing selected directory paths in their own
#                   corresponding text fields.
#                   Next, provide a button to execute a function that iterates
#                   through the source directory, checking for the existence
#                   of ".txt" files and paste them within the selected
#                   destination directory.
#                   Finally, the script records the file names that were moved
#                   and their corrensponding modified time-stamps into a db and
#                   print out the ".txt" files and time-stamps to console.
#
# Requirements:     -Script will need to use Python 3, the Tkinter module,
#                   and the OS module.
#                   -Script will need to use the listdir() method from
#                   the OS module to iterate through all files within a specific directory.
#                   -Script will need to use the path.join() method from the
#                   OS module to concatenate the file name to its file path,
#                   forming an absolute path.
#                   -Script will need to use the getmtime() method from
#                   the OS module to find out the latest date the file has been
#                   created or last modified.
#                   -Script will need to create a database to record the qualifying
#                   file and corresponding modified time-stamp.
#                   -Script will need print each file ending with a “.txt” file
#                   extension and its corresponding mtime to the console.
#                   -Script will need to use the move() method from the Shutil
#                   module to cut all qualifying files and paste them within the
#                   destination directory.


import os
import sqlite3
import shutil
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        global source_path, dest_path, source
         

        source_path = str()
        dest_path = str()

        # create window
        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(600,200))
        self.master.title('Select Files...')
        self.master.config(bg='#DCDCDC')

        # call function to center window
        center_window(self,600,200)

        # define grid size
        grid_size(self,master)

        # call function to load widgets
        load_gui(self)

        # call function to create database
        create_db(self)

        

# center GUI in user's screen
def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

# define grid size and weight
def grid_size(self,master):
    rows = 0
    columns = 0
    while rows < 5:
        master.rowconfigure(rows,weight=1)
        rows += 1
        while columns < 4:
            master.columnconfigure(columns,weight=1)
            columns += 1

# create widgets within GUI window
def load_gui(self):
    self.lbl_source = tk.Label(self.master,text='SOURCE DIRECTORY:',bg='#DCDCDC')
    self.lbl_source.grid(row=0,column=0,columnspan=2,padx=(30,0),pady=(10,0),sticky=N+W)
    self.lbl_dest = tk.Label(self.master,text='DESTINATION DIRECTORY:',bg='#DCDCDC')
    self.lbl_dest.grid(row=2,column=0,columnspan=2,padx=(30,0),pady=(10,0),sticky=N+W)

    
    self.txt_source = tk.Entry(self.master,width=50,textvariable=source_path)
    self.txt_source.grid(row=1,column=1,columnspan=3,padx=(0,20),pady=(10,10),sticky=N+S+W+E)
    self.txt_dest = tk.Entry(self.master,width=50,textvariable=dest_path)
    self.txt_dest.grid(row=3,column=1,columnspan=3,padx=(0,20),pady=(10,10),sticky=N+S+W+E) 

    
    self.btn_src = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: source_dir(self.txt_source))
    self.btn_src.grid(row=1,column=0,padx=(30,0),sticky=W)
    self.btn_dest = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: dest_dir(self.txt_dest))
    self.btn_dest.grid(row=3,column=0,padx=(30,0),sticky=W)
    self.btn_exe = tk.Button(self.master,width=12,height=2,text='EXECUTE',command=lambda: list_dir(self))
    self.btn_exe.grid(row=4,column=3,padx=(0,20),pady=(0,10),sticky=E)

# allows user to select a source directory from their computer
# and print to GUI
def source_dir(self):
    source_path = filedialog.askdirectory()
    self.insert(0,source_path)
    print(source_path)

# allows user to select a destination directory from their computer
# and print path to GUI
def dest_dir(self):
    dest_path = filedialog.askdirectory()
    self.insert(0,dest_path)
    print(dest_path)


# create database in sqlite3
def create_db(self):
    conn = sqlite3.connect('python_124.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_fileList( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT, \
            col_timestamp TEXT \
            );')
        # save changes & close database connection
        conn.commit()
    conn.close()
            


# upon 'EXECUTE' this function will iterate thru source dir, print
# path & timestamp of '.txt' files, copy these files to the chosen  
# destination dir and insert files & timestamps into the db
def list_dir(self):
    # iterate through destination directory in search for '.txt'
    # files, creating a list of these files and corresponding
    # timestamp
    source = self.txt_source.get()
    fList = os.listdir(source)
    txtList = []
    for file in fList:
        if file.endswith('.txt'):
            txtList = os.path.join(source,file)
            time = datetime.fromtimestamp(os.path.getmtime(txtList))
            print('{} {}'.format(txtList,time))
    move_files(self)        
    

    '''# connect to db and insert '.txt' file and timestamp info    
    conn = sqlite3.connect('python_124.db')
    with conn:
        cur = conn.cursor()
        for entry in txtList:
            cur.execute(INSERT INTO tbl_fileList (col_file,col_timestamp) VALUES(?,?),(file,time))
        conn.commit()
    conn.close()'''

# call function to move '.txt' files to chosen destination directory


# move '.txt' files to a new directory using
# the move() method from the Shutil module

def move_files(self):
    source = self.txt_source.get()
    destination = self.txt_dest.get()
    txtList = os.path.join(source)
    for file in txtList:
        if file.endswith('.txt'):
            shutil.move(source + file, destination)
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


