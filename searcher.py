from pwn import *

max_offset = 0x500

for i in range(500, max_offset):
    print(i)
    f = open("./demo", "r")
    ccode = f.read()
    f.close()
    ccode = ccode.format(i)
    f = open("./exit_hijack.c", "w")
    f.write(ccode)
    f.close()
    os.system("gcc -o test exit_hijack.c")
    p = process("./test")
    try:
        msg = p.recvall()
        if b"OK" in msg:
            print(msg)
            print("find! offset=", i)
            break
    except:
        pass
    p.kill()
