import os
import cmd

def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("There is no help yet.")
        else:
            execute_command(command)