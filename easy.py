import os

directory = 'file/Boot/Camera Roll/Microsoft/Saved Pictures/Screenshots/cpp'

os.system("find " + directory + " -mtime +60 -print")
os.system("find " + directory + " -mtime +60 -delete")
