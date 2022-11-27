from pathlib import Path
import sys
import os
from default import lines, Line


if __name__ == "__main__":
    p = sys.argv[1]
    if p == "-help":
        os.system("less /usr/bin/basic/README.md")
    elif p == "-uninstall":
        os.system("python3 /usr/bin/basic/uninstall.py")
    elif p == "-update":
        os.system("python3 /usr/bin/basic/update.py")
    elif p == "-updateTesting":
        os.system("python3 /usr/bin/basic/updateToTesting.py")
    elif p == "-example":
        os.system("python3 /usr/bin/basic/runBasic.py /usr/bin/basic/GUESSANUMBER.BAS")
    elif p == "-install":
        command = "sudo cp " + sys.argv[2] + " /usr/bin/basic/"
        os.system(command)
    else:    
        objects = []
        p = Path(p)
        file = p.read_text()

        commands = file.split("\n")
        while True:
            try:
                commands.remove("")
            except:
                break

        for l in commands:
            objects.append(Line(l))

        for l in lines:
            lines[l].run()
            break