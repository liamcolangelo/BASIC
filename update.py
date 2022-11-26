import os

print("Downloading updated repository as temporary files")
os.system("git clone https://github.com/liamcolangelo/BASIC.git tempBASIC")
print("Copying new files")
os.system("sudo cp -a tempBASIC/. /user/bin/basic/")
print("Removing temporary files")
os.system("cd ..")
os.system("rm -r -f tempBASIC")
print("Finished")