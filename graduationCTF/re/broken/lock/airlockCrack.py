import sys

xor = []
cmd = "fitsec{cr4ck1ng_th3_h4sh3s_fun_}"

for char in cmd:
    xor.append(ord(char) ^ ord('w'))

for x in xor:
        sys.stdout.write(chr(x + 40))
