def run(command):
    if "EXAMPLE" in command:
        print("This is an example extension")
    else:
        return False
    return True