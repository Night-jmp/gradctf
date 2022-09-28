import sys
pw_hash = "a^L^PL`P\``cPoohP,/><:P->A8:-"

for c in pw_hash:
    sys.stdout.write(chr((ord(c) - 40)^ord('w')))
