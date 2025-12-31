# os is the built in module of python
import os
#specify your directory here in place of '.'
contents = os.listdir(".")
print("Contents of the directory:")
for item in contents:
    print(item)
