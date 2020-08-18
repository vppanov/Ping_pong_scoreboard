import os
import runpy


path = os.getcwd()
print(path)
path2 = ("." + path)
full = os.path.join(path, "database.py")
print(full)
full = os.path.join(path, "system/stats.db")
print(full)

#exec(open('system/database.py').read())