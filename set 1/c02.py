import binascii


def xor_hex(hexstr1, hexstr2):
    bytes1 = binascii.a2b_hex(hexstr1)
    bytes2 = binascii.a2b_hex(hexstr2)
    return binascii.b2a_hex(xor_bytes(bytes1, bytes2))


def xor_bytes(byte_array1, byte_array2):
    if len(byte_array1) != len(byte_array2):
        raise ValueError("byte array lengths did not match")
    length = len(byte_array1)
    return bytes([byte_array1[i] ^ byte_array2[i] for i in range(length)])


def main():
    hexstr1 = "1c0111001f010100061a024b53535009181c"
    hexstr2 = "686974207468652062756c6c277320657965"
    print(xor_hex(hexstr1, hexstr2))

if __name__ == '__main__':
    main()
