import os

print("Downloading updated repository as temporary files")
os.system("git clone --single-branch --branch testing https://github.com/liamcolangelo/BASIC.git tempBASIC")
print("Copying extensions")
os.system("sudo cp /usr/bin/basic/extensions tempExtensions")
print("Removing old files")
os.system("sudo rm -r -f /usr/bin/basic/*")
print("Copying new files")
os.system("sudo cp -a tempBASIC/. /usr/bin/basic/")
print("Reinstalling extensions")
os.system("sudo cp tempExtensions/* /usr/bin/basic/extensions/")
print("Removing temporary files")
os.system("cd ..")
os.system("rm -r -f tempBASIC")
os.system("rm -r -f tempExtensions")
print("Finished")