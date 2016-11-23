from math import ceil
from c2 import XORbytes
import binascii

def repeatingKeyXOR_encrypt(message, key):
    length = len(message)
    paddedKey = (ceil(length/len(key))*key)[:length]
    return XORbytes(message.encode('utf-8'), paddedKey.encode('utf-8'))

def main():
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    print(binascii.b2a_hex(repeatingKeyXOR_encrypt(message, key)))

if __name__ == '__main__':
    main()