import os
import runpy


path = os.getcwd()
path2 = ("." + path)
full = os.path.join(path, "database.py")
full = os.path.join(path, "system/stats.db")
exec(open('system/database.py').read())
