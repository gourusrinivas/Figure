import os
from time import time

p='D:\file'
result=[os.remove(file) for file in (os.path.join(path, file) for path, _, files in os.walk(p) for file in files) if os.stat(file).st_mtime < time() - 7 * 86400]
print(result)
