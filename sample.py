import os, time

path = r"D:\file"
now = time.time()

for filename in os.listdir(path):
    
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print("Old files are deleted")
            os.remove(os.path.join(path, filename))
    print(filename)
