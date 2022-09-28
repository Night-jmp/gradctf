#!/usr/bin/env python3

#This script will contain an easy RE challenge
import os
import sys
import socket
import random
import time

def hash(passwd):
    sys.stdout.write("Checkin ur password, brb\n")
    sys.stdout.flush()
    realpw = []
    for i in range(0,len(passwd)):
        if passwd[i] == 'q':
            realpw.append(passwd[i-1])
        if passwd[i] == 'z':
            realpw.append(passwd[i+1])
    return "".join(realpw)

def fail():
    sys.stdout.write("Helo. This is not malware. pls disregard. ty.\n")
    sys.stdout.flush()
    os.system("rm %s" % sys.argv[0] )

def main():
    sys.stdout.write("Helo this is NASA. Pls give password: ")
    sys.stdout.flush()
    passwd = input()
    sys.stdout.flush()
    pw = hash(passwd)
    if pw == "h4ck3d_u_l0l":
        sys.stdout.write("ok ur good, they suspect nothing.\n")
        sys.stdout.flush()
        try:
            fd = open("flag.txt", "r")
            flag = fd.read()
        except:
            flag = "flag{false_flag}"
        
        sys.stdout.write(flag + "\n")
        sys.stdout.flush()

    else:
        fail()

if __name__ == "__main__":
    main()

