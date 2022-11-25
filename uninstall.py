import os

sure = input("Are you sure you would like to uninstall the BASIC interpreter y/n : ")
if sure.lower() == "y":
    print("Uninstalling GUESSANUMBER.BAS")
    os.system("sudo rm /usr/bin/basic/GUESSANUMBER.BAS")
    print("Uninstalling install.py")
    os.system("sudo rm /usr/bin/basic/install.py")
    print("Uninstalling README.md")
    os.system("sudo rm /usr/bin/basic/README.md")
    print("Uninstalling runBasic.md")
    os.system("sudo rm /usr/bin/basic/runBasic.py")
    print("Uninstalling uninstall.py")
    os.system("sudo rm /usr/bin/basic/uninstall.py")
    print("Removing basic directory")
    os.system("sudo rmdir /usr/bin/basic")
    print("Removing basic alias")
    with open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'r') as f:
        file = f.read()
        file = file.replace("\nalias basic='python3 /usr/bin/basic/runBasic.py'", "")
        f.close()
    with open(os.path.join(os.path.expanduser('~'), '.bashrc'), 'w') as f:
        f.write(file)
        f.close()
    os.system(". ~/.bashrc")
    print("Finished")
    os.system("exec bash")
else:
    print("Cancelled")
