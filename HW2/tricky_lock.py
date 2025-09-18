"""
File:    tricky_lock.py
Author:  Shelby Walton
Date:    9/19/2025
Section: 30
E-mail:  w100@umbc.edu
Description:
    A program that simulates a tricky lock that opens with a specific sequence of inputs.
"""
x= input("What is the first number in the combination lock?")
y =input("What is the second number in the combination lock?")
p1 = input("What is the position of the first switch (up/down)?")
p2 = input("What is the position of the second switch (up/down)?")
p3 = input("What is the position of the third switch (up/down)?")
z = x + y == "36"
a = (p1 == "up" and p2 == "down" and p3 == "up") or (p1 == "up" and p2 == "up" and p3 == "down") or (p1 == "down" and p2 == "up" and p3 == "up") 
if z and a:
    print("The lock opens!")
elif z or a:
    print("THe lock clanks but does not open.")
else:
    print("The lock does not even budge, try again.")
    
   