import os, time

path = r"D:\file"
now = time.time()

for filename in os.listdir(path):
    
    if os.path.getmtime(os.path.join(path, filename)) < now - 2 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))
            
import os
import zipfile

def zipdir(path, ziph):
# ziph is zipfile handle
for root, dirs, files in os.walk(path):
for file in files:
ziph.write(os.path.join(root, file),
os.path.relpath(os.path.join(root, file),
os.path.join(path, '..')))

zipf = zipfile.ZipFile('Other.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('tmp/', zipf)
zipf.close()
