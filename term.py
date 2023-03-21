
import sys

import subprocess
import keyboard
import time

# cmd_str = "arm-none-eabi-addr2line -faps -e ./bin/hot.package.elf


def cmd_menu():

    cmd_str = input(
        "(1) for Build, (2) for MU, (3) for Brain Terminal, (4) for Stack Trace \n")

    if cmd_str == "e":
        sys.exit()

    elif cmd_str == "1":
        subprocess.run("pros build", shell=True)

    elif cmd_str == "2":
        subprocess.run("pros mu", shell=True)

    elif cmd_str == "3":
        print("\n Entering Terminal... (e) to escape ")
        p = subprocess.Popen("pros terminal", shell=True)
        while (not keyboard.is_pressed("e")):
            time.sleep(0.1)
        p.kill()

    elif cmd_str == "4":

        print("Enter Addresses to Translate. \n")
        str = ""
        while True:
            try:
                line = input()
            except EOFError:
                break
            str += line

        str = str.split(" ")

        p = subprocess.run(
            "arm-none-eabi-addr2line -faps -e ./bin/hot.package.elf", shell=True)

        arr = []
        for line in str:
            arr[str.index(line)] = subprocess.run(line, shell=True).stdout

        p.terminate()
        p = subprocess.run(
            "arm-none-eabi-addr2line -faps -e ./bin/cold.package.elf", shell=True)

        for line in str:
            if "??" in arr[str.index(line)]:
                arr[str.index(line)] = subprocess.run(line, shell=True).stdout

        print(arr)

    else:
        print("INVALID ENTRY")
        cmd_menu()

    print("\n Thy command has been finished \n")


def main():
    while True:
        cmd_menu()


main()
