"""
File:    gandalf.py
Author:  Shelby Walton
Date:    9/19/2025
Section: 30
E-mail:  w100@umbc.edu
Description:
A guessing game to determine which character 'you are' in Lord of the Rings.  
"""

Race = input("Which race are you? (human/dwarf/elf/maiar/hobbit):").lower()
if Race == "human":
    A = input("Are you the King of Gondor? (yes/no):").lower()  
    if A == "yes":
        print("You are Boromir")
    else:
        print("You are Theoden, probably")
elif Race == "dwarf":
    print("You are Gimli son of Gloin").lower()
elif Race == "elf":
    B = input("Were you in the matrix? (yes/no):").lower()
    if B == "yes":
        print("You are Elrond")
    else:
        print("You are Legolas")
elif Race == "maiar":
    C = input("Are you good or evil? (good/evil):").lower()
    if C == "good":
        print("You are Gandalf")
    else:
        evil = input("Did you forge the one ring? (yes/no):").lower()
        if evil == "yes":
            print("You are Sauron")
        else:
            print("You are Saruman")
elif Race == "hobbit":
    D = input("Did you carry the one ring? (yes/no):").lower()
    if D == "yes":
        print("You are Frodo Baggins")
    else:
        print("You are Merry or Pippin")
else:
    print("You are an Orc, sorry about that.")
    