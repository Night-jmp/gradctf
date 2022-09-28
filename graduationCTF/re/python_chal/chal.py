#!/usr/bin/env python3


def check_header(header):
    if (ord(header[0]) ^ 0x2) != 0x64:
        return False
    if (ord(header[1]) << 10) != 0x1a400:
        return False
    if ord(header[2]) != 0o164:
        return False
    if (((ord(header[3]) << 8) & 0xff00) >> 8) != 115:
        return False
    if ord(header[4]) != 0b01100101:
        return False
    if header[5] != 'c':
        return False

    return True

def check_chunk_1(chunk):
    encrypted_chunk = "r2t0vv'io"
    chunk_check = []
    for index, byte in enumerate(chunk):
        chunk_check.append(chr(ord(byte) ^ index))

    if encrypted_chunk != "".join(chunk_check):
        return False

    return True

def check_chunk_2(chunk):
    encrypted_chunk = [0x61, 0xb3]
    chunk_check = []
    for index, byte in enumerate(chunk):
        if chr(encrypted_chunk[index] - 0x40) != byte:
            return False

    return True

def check_chunk_3(chunk):
    y = "ennuff!!"
    x = chunk[::-1]
    if x in y:
        if y.find(x) == 2:
            return True
    
    return False

def verify(subject):
    if len(subject) == 0x18:
        if check_header(subject[0:6]):
            if subject[6] == "{":
                body = subject[7:-1]
                chunks = body.split("_")
                if check_chunk_1(chunks[0]):
                    if check_chunk_2(chunks[1]):
                        if check_chunk_3(chunks[2]):
                            if subject[-1] == "}":
                                return "Valid flag!"
    return "Not valid!"


if __name__ == "__main__":
    print("Flag hider 5000")
    print("Written proudly by nyt3_jmp")
    print("Super secret proprietary encryption technology that no one can break, not even the NSA")
    verify_me = input("Enter your flag: ")
    print(verify(verify_me))
