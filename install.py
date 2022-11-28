import os

print("Making directory /usr/bin/basic")
os.system("sudo mkdir /usr/bin/basic")
print("Making directory /usr/bin/basic/extensions")
os.system("sudo mkdir /usr/bin/basic/extensions")
print("Installing files")
os.system("sudo cp ./* /usr/bin/basic")
os.system("sudo mv exampleExtension.py /usr/bin/basic/extensions/exampleExtension.py")
os.system("sudo rm /usr/bin/basic/exampleExtension.py")
print("Making alias basic=python3 /usr/bin/basic/runBasic.py")

with open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'r') as f:
    file = f.read() + "\n" + "alias basic='python3 /usr/bin/basic/runBasic.py'"
    f.close()
with open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'w') as f:
    f.write(file)
    f.close()
os.system("cd ~")
os.system(". ~/.bashrc")
print("Finished")
os.system("exec $SHELL")
