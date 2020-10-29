from binascii import hexlify, unhexlify
from itertools import cycle

def do_xor(message):
    key = b'F\xcc\xf9\xa5q\xf0\xff\xb1~A\xcb\x84'
    message = bytes.fromhex(message)
    return bytes(x ^ y for x, y in zip(message, cycle(key))).hex()

with open('smokeaway.jpg', 'rb') as f:
    message  = f.read()
    message = hexlify(message).decode().replace('\n', '')
f.close()

with open('smokeaway.jpg.enc', 'wb') as i:
    i.write(unhexlify(do_xor(message)))
i.close()
