#list all built in fuctions of python using loop by loop

import builtins

for i in dir(builtins):
    if not i.startswith("__"):
        print(i)
    
