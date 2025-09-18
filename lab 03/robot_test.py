"""
File: Robot_test.py
Author: Shelby Walton
Date: 9/16/2025
Section: 30
E-mail: w100@umbc.edu
Description: This is a test to see if you are a robot or human.
"""


Race =input("Be you robot, or human?:")
if Race =="human":
    print("Humans must be destroyed!")
elif Race == "robot":
    Ch=input("Administer the Test! \n Which of the following would you prefer?\n A cute (puppy)\n A (flower) from your sweetie \n A large properly formatted (data file). \n Choose!:")
    if Ch =="puppy":
        print("Get the intruder! Get the humanoid!")
    elif Ch =="flower":
         print("That is acceptable, pass on mechanical friend.")
    elif Ch == "data file":
        print("Very good, you are a robot of some esteem!")