import os, time

path = r"D:\file"
now = time.time()

for filename in os.listdir(path):
    
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print()
            os.remove(os.path.join(path, filename))
            
path = "D:\file"
dir_list = os.listdir(path)
print("Recent files", path)
print(dir_list)
