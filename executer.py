



print("""
# T- Interpreter
# Version: 0.0.1 Alpha
# Created by Murilo
# Copyright © 2026
""")

with open("commands.cfg") as file:
    commands = file.read().split("=")

command_name = commands[0].strip()
command_output = commands[1].strip()               

with open("syntax.cfg") as file:
    syntax = file.read()

with open("TM.tm") as file:
    for linha in file:
        linha = linha.strip()

        if not linha:
            continue

        program = linha.split('"')

        command = program[0].strip()

        if len(program) > 1:
            message = program[1]
        else:
            message = ""

        if command == "ms":
            print(message)

        elif command == "nl_":
            print()

if command == "-help":
    print("""
T- Programming Language
Version: 0.0.2 Alpha

Commands:

ms "text" 
    Prints a message.

-help
    Shows this help.

nl_
   makes a space beetween the messages

Coming soon:
- var
- if
""")

elif command == "neofetch":
    print("""
     </################\>              T Minus (or T-)
             |#|                       interpreter: Python
             |#|                       version: 0.0.1 (techodemo)
             |#|    <o@@@@@@o>         made my Murilo
             |#|
             |#|
             |#|
                                     
""")

elif command == "sudo":
    print("""nice try buddy""")


elif command == "banana":
    print("""


   _
  - \_
  \,'.`-.
   |\ `. `.       
   ( \  `. `-.                        _,.-:\   made by Herman Hiddema (Shimrod)
    \ \   `.  `-._             __..--' ,-';/
     \ `.   `-.   `-..___..---'   _.--' ,'/
      `. `.    `-._        __..--'    ,' /
        `. `-_     ``--..''       _.-' ,'
          `-_ `-.___        __,--'   ,'
             `-.__  `----"""    """'"'
                  `--..____..--'

""")

elif not command == command_name:
    print("syntax error: 'ms' expetected")
