# An interpreter for the BASIC programming language written in Python
### Written by Liam Colangelo

This is an interpreter for the BASIC prgramming language.
Instead of using an emulator for an Atari or Commodore computer, this program can be used instead.
This will only work in the command line, so none of the color changing or sprite features have been added at this time.
The program will also only work on linux and possibly macOS(not tested).

List of commands:
* `REM` : Comments
* `PRINT()` : Self-explanatory
* `GOTO` : Go to a specific line
* Variables are initialized with a "=" sign.
* `IF test_case THEN code` statements where a test can include "=" or "<>"(not equal) for strings and numbers. "<",
    ">", "<=", and ">=" will all work for numbers.
* Math: `+ - / * % **`
* To run a multiple commads on the same line, just separate them with a " : "
* `INT()` : Floors a floating-point number
* `STR()` : Converts a number into a string
* `+` can also be used for concatenation between strings and variables.
* `INPUT(MESSAGE); VAR` : is used to to take user input. VAR is the variable that it is assigned to. MESSAGE will be printed on the same line before input is taken.
  
*Note: Lines are separated by individual lines. There is no end-of-line symbol other than a break.*

*Note: Much of this program relies on spacing. Make sure that there is a **SINGLE** space separating each part of a line.*


To use:
* Ensure that you have python3 installed on your computer
* Run the install.py script to install the program in /usr/bin/basic
* Run the python basic interpreter by using the 'basic' command in the terminal followed by the name of the file you want to run.
* Ex) basic GUESSANUMBER.BAS


Use `basic -help` to open README.md

Use `basic -uninstall` to run uninstall.py
