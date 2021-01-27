import glob
import pathlib
#print(glob.glob("../connections/*py"))
#py = pathlib.Path('../connections/').glob("*.py")
#for file in py:
#    print(file)
import os
x = [i[2] for i in os.walk('../connections/')]
x[0].remove('__init__.py')
print(x[0])
