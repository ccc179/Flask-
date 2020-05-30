def str_to_hex(s):
    return '\\'.join([hex(ord(c)).replace("0", "") for c in s])

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


if __name__ == '__main__':
    hex_content = str_to_hex("sdHJH8728HJKHDhjsh67")
    print(hex_content)