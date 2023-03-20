# what is Package?
# Package is the collection of modules. Modules are basically python files.

import os
import shutil

print(os.getcwd())

shutil.disk_usage("/")
print(shutil.disk_usage("/"))

total, used, free = shutil.disk_usage("/")

print("Total disk space is:",total // (2**30),"GB")
print("Used disk space is:",used // (2**30),"GB")
print("Free disk space is:",free // (2**30),"GB")