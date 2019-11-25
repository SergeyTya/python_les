import os.path
path = "/home/elvis/tst/"
flist = []
for cur_dir, dirs, files in os.walk(path):
  if any(f[-3:] == '.py' for f in files): flist.append(cur_dir[len(path):])
flist.sort()
print(flist)

with open("FileSys_output.txt", "w") as ofile:
    ofile.writelines("\n".join(flist))
