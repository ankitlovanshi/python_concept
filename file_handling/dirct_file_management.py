# os is a module that provide us to methods for the file and dictories

import os

# check the current working dirctory
print(os.getcwd())

# list all the files
print(os.listdir())

# change the dirctory
'''os.chdic("")'''

# make the dirctory
os.mkdir("test")

# rename the dirctory
os.rename("test", "new_one")

# remove file
os.remove("file.txt")

# remove dictory
os.rmdir("new_one")