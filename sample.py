import os, time

path = r"D:\file"
now = time.time()

for filename in os.listdir(path):
    
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            
            os.remove(os.path.join(path, filename))
    
for dirpath in os.walk(path):
    print("Current path", dirpath)
for dirnames in os.walk(path):
    print("Current directories", dirnames)
for filenames in os.walk(path):
     print("The new files are", filenames)

