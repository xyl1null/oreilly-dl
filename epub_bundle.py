import os
from shutil import make_archive
import sys

for line in sys.stdin:
    a = line.split("\n")[0]
    break
make_archive(a,"zip")
os.rename(a + ".zip", os.path.join(a + ".epub"))
print("generated!")
