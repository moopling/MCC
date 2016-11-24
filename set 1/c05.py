import binascii
from math import ceil
from c02 import xor_bytes


def repeatingKeyXOR_encrypt(message, key):
    length = len(message)
    paddedKey = (ceil(length / len(key)) * key)[:length]
    return xor_bytes(message.encode('utf-8'), paddedKey.encode('utf-8'))


def main():
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    print(binascii.b2a_hex(repeatingKeyXOR_encrypt(message, key)))

if __name__ == '__main__':
    main()
