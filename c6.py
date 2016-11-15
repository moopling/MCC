import binascii

def hammingDistance(byte_array1, byte_array2):
    if len(byte_array1) != len(byte_array2):
        raise ValueError("byte array lengths did not match")
    length = len(byte_array1)
    hammingDist_bytes = [bin(byte_array1[i]^byte_array2[i]).count("1") for i in range(length)]
    return sum(hammingDist_bytes)

def main():
    bytes1 = b'this is a test'
    bytes2 = b'wokka wokka!!!'
    print(hammingDistance(bytes1, bytes2))

if __name__ == '__main__':
    main()