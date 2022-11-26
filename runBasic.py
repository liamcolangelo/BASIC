from pathlib import Path
import sys
import os
from default import lines, Line


if __name__ == "__main__":
    p = sys.argv[1]
    if p == "-help":
        os.system("less /usr/bin/basic/README.md")
        sys.exit()
    elif p == "-uninstall":
        os.system("python3 /usr/bin/basic/uninstall.py")
        sys.exit()
    elif p == "-update":
        os.system("python3 /usr/bin/basic/update.py")
        sys.exit()
    elif p == "-updateTesting":
        os.system("python3 /usr/bin/basic/updateToTesting.py")
        sys.exit()
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