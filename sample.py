import os, time

path = r"D:\file"
now = time.time()

for filename in os.listdir(path):
    
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            
            os.remove(os.path.join(path, filename))
    print()
for dirpath,dirnames,filenames in os.walk(path):
    print("Current path", dirpath)
    print("Current directories", dirnames)
    print("The new files are", filenames)
