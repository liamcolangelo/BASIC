import os

print("Making directory /usr/bin/basic")
os.system("sudo mkdir /usr/bin/basic")
print("Making file install.py")
os.system("sudo cp install.py /usr/bin/basic/install.py")
print("Making file runBasic.py")
os.system("sudo cp runBasic.py /usr/bin/basic/runBasic.py")
print("Making file README.md")
os.system("sudo cp README.md /usr/bin/basic/README.md")
print("Making file GUESSANUMBER.BAS")
os.system("sudo cp GUESSANUMBER.BAS /usr/bin/basic/GUESSANUMBER.BAS")
print("Making file uninstall.py")
os.system("sudo cp uninstall.py /usr/bin/basic/uninstall.py")
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
os.system("exec bash")
