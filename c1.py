import binascii

def hex2b64(hexstr):
    bytestr = binascii.a2b_hex(hexstr)
    b64str = binascii.b2a_base64(bytestr)
    return b64str

def main():
    hexstr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'  
    b64str = hex2b64(hexstr)
    print(b64str)

if __name__ == '__main__':
    main()