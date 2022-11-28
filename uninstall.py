import os

sure = input("Are you sure you would like to uninstall the BASIC interpreter y/n : ")
if sure.lower() == "y":
    print("Uninstalling files")
    os.system("sudo rm -r -f /usr/bin/basic")
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
    os.system("exec $SHELL")
else:
    print("Cancelled")
