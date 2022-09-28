#!/usr/bin/python2
###
#
#   Written in python2 by: Nyt3_jmp
#   Super secure flag retreiver
#
###
import re

flag = open("flag.txt", "r").read().strip()

def get_user_input(prompt):
    # Idk why input acts strange but this fixes it!
    try:
        return input(prompt)
    except NameError as e:
        return re.findall("name '(\w+)' is not defined",str(e))[0]

if __name__ == "__main__":
    print("")
    username = get_user_input("Username: ")
    print("Welcome, " + username)
    password = get_user_input("Password: ")
    pw = open("password.txt", "r").read().strip()
    if username == "nyt3_jmp" and password == pw:
        print(flag)
