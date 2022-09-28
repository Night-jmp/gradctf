fd = open("flag.txt", "r")
data = fd.read().strip()

out = open("flag.enc", "wb")
for x in data:
    out.write(bytes(chr(ord(x) ^ 0x55), 'utf-8'))

fd.close()
out.close()
