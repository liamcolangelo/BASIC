from pathlib import Path
import sys
from random import random

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

    def run(self):
        if self.check():
            for i in self.commands:
                i = i.replace("RND(1) ", str(random()))
                """
                try:
                    i.replace("RND(1) ", str(Random()))
                except Exception as error:
                    print("RND(1) Error")
                    print(error)
                    """
                if "PRINT" in i:
                    if "\"" in i:
                        printValue = self.commands[self.commands.index(i)].split(" \"")
                        printValue.remove(printValue[0])
                        printValueString = ""
                        for s in printValue:
                            printValueString = printValueString + s

                        printValueString = printValueString.replace("\"", "")
                        print(printValueString)

                    else:
                        printValue = self.commands[self.commands.index(i)].split(" ")
                        print(vars[printValue[1]])

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
                    else:
                        try:
                            float(i[1])
                            vars[i[0]] = i[1]
                            continue
                        except Exception as error:
                            print("Variable error on line: " + str(self.lineNum))
                            print(error)
                            ####### Remove Later #######
                            vars[i[0]] = i[1]
                            ############################
                    
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
        if type(second) != str and type(second) != str:
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