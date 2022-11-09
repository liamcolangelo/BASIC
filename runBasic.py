from pathlib import Path
import sys
from random import random
from math import floor

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
                if "INT(" in i:
                    i2 = i.replace("(", "@")
                    i2 = i2.replace(")", "@")
                    i2 = i2.split("@")
                    value = i2[1]
                    var = value
                    if value in vars:
                        value = vars[value]
                    intValue = floor(float(value))
                    i = i.replace("INT(" + str(var) + ")", str(intValue))
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
                    i = i.split(" = ")
                    if "\"" in i[1]:
                        i[1] = i[1].replace("\"", "")
                        vars[i[0]] = i[1].strip()
                        continue
                    elif "INPUT()" in i[1]:
                        inValue = input()
                        try: 
                            inValue = float(inValue)
                        except:
                            inValue = "\"" + str(inValue) + "\""
                        vars[i[0]] = inValue
                        continue
                    elif i[1] in vars:
                        vars[i[0]] = vars[i[1]]
                    else:
                        try:
                            float(i[1].strip())
                            vars[i[0]] = i[1]
                            continue
                        except Exception as error:
                            print("Variable error on line: " + str(self.lineNum))
                            print(error)
                    
                elif "INPUT()" in i:
                    input()

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
                first = int(first)
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
                second = int(second)
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
    p = input("Enter BASIC file name: ")
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