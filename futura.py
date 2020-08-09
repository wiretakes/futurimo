# Futu-rimo Libraries v1.01
# Written by wiretakes
# 2020 (C) wiretakes
 
def version():
    print(""" ______      __  __        ______      __  __        ______        __        __    __        ______       
/\  ___\    /\ \/\ \      /\__  _\    /\ \/\ \      /\  == \      /\ \      /\ "-./  \      /\  __ \      
\ \  __\    \ \ \_\ \     \/_/\ \/    \ \ \_\ \     \ \  __<      \ \ \     \ \ \-./\ \     \ \ \/\ \     
 \ \_\       \ \_____\       \ \_\     \ \_____\     \ \_\ \_\     \ \_\     \ \_\ \ \_\     \ \_____\    
  \/_/        \/_____/        \/_/      \/_____/      \/_/ /_/      \/_/      \/_/  \/_/      \/_____/""")
    print("\nFuturimo (a.k.a Project:FUTURA)  v1.01\n  Created by wiretakes\n    2020 (C) wiretakes")
def changelog():
    print("\nWARNING: This is an earlier version of Futurimo. In and Out modules are just int and str based.\nAnything could change in the later builds.\n")
def wop():
    print("This section of this library is still in development.")
    exit()

class Futu:
    def __init__(self):
        self.futura = null
    def version():
        print("Futu v1.02\nCreated by wiretakes. 2020 (C) wiretakes\n - Sub-library of Futurimo")
    

    class Out:
        def output(inputIO):
            print(inputIO)
    class In:
        def read(type):
            readR = input()
            if (type == "int"):
                futuRead = int(float(readR))
            elif (type == "rnd"):
                futuRead = round(int(float(readR)))
            else:
                futuRead = readR
            return futuRead
        def readp(message,type):
            readR = input(message)
            if (type == "int"):
                futuRead = int(float(readR))
            elif (type == "rnd"):
                futuRead = round(int(float(readR)))
            else:
                futuRead = readR
            return futuRead

class Rimo:
    def __init__(self):
        self.rimona = null
    def version():
        print("Rimo v1.01\nCreated by wiretakes. 2020 (C) wiretakes\n - Sub-library of Futurimo")
    class Shell:
        def start():
            rimoReq = input("rimo > ")
            


