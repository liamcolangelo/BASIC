from pathlib import Path
import sys
from random import random
from math import floor
import os

lines  = {}
objects = []
vars = {}

class Line(object):
    def __init__(self, line):
        line = line.split(" ")
        self.lineNum = int(line[0])
        lines[self.lineNum] = self
        line.remove(line[0])
        self.commands = []
        if "IF" in line[0]:
            line.remove(line[0])
            self.ifStatement = str(line[0] + " " + line[1] + " " + line[2])
            for i in range(4):
                line.remove(line[0])
        else:
            self.ifStatement = True
        if not ":" in line:
            lineString = ""
            for i in line:
                lineString = lineString + i + " "
            self.commands.append(lineString)
        else:
            lineString = ""
            for i in line:
                lineString  = lineString + i + " "
            line = lineString.split(" : ")
            for i in line:
                self.commands.append(i)

    def getVar(self, var):
        if var in vars:
            return vars[var]
        else:
            return None

    def run(self):
        if self.check():
            for i in self.commands:
                i = i.replace("RND(1) ", str(random()))
                if "INT(" in i and not "PRINT" in i:
                    i2 = i.replace("(", "@")
                    i2 = i2.replace(")", "@")
                    i2 = i2.split("@")
                    value = i2[1]
                    var = value
                    if value in vars:
                        value = vars[value]
                    intValue = floor(float(value))
                    i = i.replace("INT(" + str(var) + ")", str(intValue))
                if "STR(" in i:
                    i2 = i.replace("(", "@")
                    i2 = i2.replace(")", "@")
                    i2 = i2.split("@")
                    value = i2[1]
                    var = value
                    if value in vars:
                        value = vars[value]
                    stringValue = "\"" + str(value) + "\""
                    i = i.replace("STR(" + str(var) + ")", stringValue)
                if " ** " in i and not "\"" in i:
                    i2 = i.split(" ")
                    location = i2.index("**")
                    value1init = i2[location - 1]
                    value2init = i2[location + 1]
                    value1 = value1init
                    value2 = value2init
                    if self.getVar(value1init) != None:
                        value1 = self.getVar(value1init)
                    if self.getVar(value2init) != None:
                        value2 = self.getVar(value2init)
                    value = float(value1) ** float(value2)
                    i = i.replace((str(value1init) + " ** " + str(value2init)), (" \"" + str(value) + "\""))
                elif " * " in i and not "\"" in i:
                    i2 = i.split(" ")
                    location = i2.index("*")
                    value1init = i2[location - 1]
                    value2init = i2[location + 1]
                    value1 = value1init
                    value2 = value2init
                    if self.getVar(value1init) != None:
                        value1 = self.getVar(value1init)
                    if self.getVar(value2init) != None:
                        value2 = self.getVar(value2init)
                    value = float(value1) * float(value2)
                    i = i.replace((str(value1init) + " * " + str(value2init)), (" \"" + str(value) + "\""))
                elif " / " in i and not "\"" in i:
                    i2 = i.split(" ")
                    location = i2.index("/")
                    value1init = i2[location - 1]
                    value2init = i2[location + 1]
                    value1 = value1init
                    value2 = value2init
                    if self.getVar(value1init) != None:
                        value1 = self.getVar(value1init)
                    if self.getVar(value2init) != None:
                        value2 = self.getVar(value2init)
                    value = float(value1) / float(value2)
                    i = i.replace((str(value1init) + " / " + str(value2init)), (" \"" + str(value) + "\""))
                elif " % " in i and not "\"" in i:
                    i2 = i.split(" ")
                    location = i2.index("%")
                    value1init = i2[location - 1]
                    value2init = i2[location + 1]
                    value1 = value1init
                    value2 = value2init
                    if self.getVar(value1init) != None:
                        value1 = self.getVar(value1init)
                    if self.getVar(value2init) != None:
                        value2 = self.getVar(value2init)
                    value = float(value1) % float(value2)
                    i = i.replace((str(value1init) + " % " + str(value2init)), (" \"" + str(value) + "\""))
                elif " + " in i and not "\"" in i:
                    i2 = i.split(" ")
                    location = i2.index("+")
                    value1init = i2[location - 1]
                    value2init = i2[location + 1]
                    value1 = value1init
                    value2 = value2init
                    if self.getVar(value1init) != None:
                        value1 = self.getVar(value1init)
                    if self.getVar(value2init) != None:
                        value2 = self.getVar(value2init)
                    value = float(value1) + float(value2)
                    i = i.replace((str(value1init) + " + " + str(value2init)), (" \"" + str(value) + "\""))
                elif " - " in i and not "\"" in i:
                    i2 = i.split(" ")
                    location = i2.index("-")
                    value1init = i2[location - 1]
                    value2init = i2[location + 1]
                    value1 = value1init
                    value2 = value2init
                    if self.getVar(value1init) != None:
                        value1 = self.getVar(value1init)
                    if self.getVar(value2init) != None:
                        value2 = self.getVar(value2init)
                    value = float(value1) - float(value2)
                    i = i.replace((str(value1init) + " - " + str(value2init)), (" \"" + str(value) + "\""))
                elif " + " in i:
                    i2 = i.split(" + ")
                    if "=" in i2[0]:
                        i2[0] = i2[0].split(" = ")
                        i2[0] = i2[0][1]
                    else:
                        i2[0] = i2[0][(i2[0].index(" ") + 1) :]
                    value1 = i2[0]
                    value2 = i2[1]
                    value1init = value1
                    value2init = value2
                    value1 = value1.strip()
                    value2 = value2.strip()
                    if not "\"" in value1:
                        value1 = self.getVar(value1)
                    else:
                        value1 = value1.replace("\"", "")
                    if not "\"" in value2:
                        value2 = self.getVar(value2)
                    else:
                        value2 = value2.replace("\"", "")
                    value = str(value1) + str(value2)
                    i = i.replace((value1init + " + " + value2init), ("\"" + value + "\""))

                if "PRINT" in i:
                    if "\"" in i:
                        printValue = i.split(" \"")
                        printValue.remove(printValue[0])
                        printValueString = ""
                        for s in printValue:
                            printValueString = printValueString + s

                        printValueString = printValueString.replace("\"", "")
                        print(printValueString)

                    else:
                        printValue = i.split(" ")
                        try:
                            try:
                                printValueString = vars[printValue[1]].replace("\"", "")
                            except AttributeError:
                                printValueString = vars[printValue[1]]
                            print(printValueString)
                        except:
                            print(printValue[1])

                elif "GOTO" in i:
                    GOTOLine = i.split(" ")
                    GOTOLine = int(GOTOLine[1])
                    lines[GOTOLine].run()
                    break

                elif " = " in i:
                    i_init = i
                    i = i.split(" = ")
                    if "\"" in i[1]:
                        i[1] = i[1].replace("\"", "")
                        vars[i[0]] = i[1].replace("  ", " ")
                    elif i[1] in vars:
                        vars[i[0]] = vars[i[1]]
                    else:
                        try:
                            float(i[1].strip())
                            vars[i[0]] = i[1]
                        except Exception as error:
                            print("Variable error on line: " + str(self.lineNum))
                            print(error)
                    i = i_init
                    
                elif "INPUT(" in i:
                    i = i.split("(")
                    i = i[1].split("; ")
                    if "\"" in i[0]:
                        printValue = i[0][1:(len(i[0]) - 2)]
                        inputValue = input(printValue)
                    else:
                        inputValue = input()
                    vars[i[1].strip()] = inputValue

                elif "REM" in i:
                    pass

                elif "END" in i:
                    sys.exit()

                else:
                    pass
        self.nextLine()

    def nextLine(self):
        for line in lines:
            if lines[line].lineNum > self.lineNum:
                lines[line].run()
                break
            else:
                pass

    def check(self):
        if type(self.ifStatement) == bool:
            return True
        statement = self.ifStatement.split(" ")
        first = statement[0]
        second = statement[2]
        operand = statement[1]
        if not "\"" in first:
            try:
                first = vars[first]
            except:
                pass
            try:
                first = float(first)
            except:
                pass
        else:
            first = first.replace("\"", "")
        if not "\"" in second:
            try:
                second = vars[second]
            except:
                pass
            try:
                second = float(second)
            except:
                pass
        else:
            second = second.replace("\"", "")
        if operand == "=" and second == first:
            return True
        elif operand == "<>" and second != first:
            return True
        if type(first) != str and type(second) != str:
            if operand == ">" and first > second:
                return True
            elif operand == "<" and first < second:
                return True
            elif operand == "<=" and first <= second:
                return True
            elif operand == ">=" and first >= second:
                return True
        return False




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
    else:
        pass


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