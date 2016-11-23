import binascii
from sortedcontainers import SortedListWithKey
from c3 import singleByteXOR_decrypt

keysize_by_score = SortedListWithKey(key=lambda val: -val[1])

bytes1 = b'this is a test'
bytes2 = b'wokka wokka!!!'
    

def hammingDistance(byte_array1, byte_array2):
    if len(byte_array1) != len(byte_array2):
        raise ValueError("byte array lengths did not match")
    length = len(byte_array1)
    hammingDist_bytes = [bin(byte_array1[i]^byte_array2[i]).count("1") for i in range(length)]
    return sum(hammingDist_bytes)

def main():
    with open("6.txt", 'r') as file:
        ciphertext = binascii.a2b_base64(file.read())
        for keysize in range(2, 41):
            score = 0
            for i in range(int(len(ciphertext)/100)):
                front_byte = ciphertext[i*keysize:(i+1)*keysize]
                back_byte  = ciphertext[(i+1)*keysize:(i+2)*keysize]
                score += hammingDistance(front_byte, back_byte)
            norm_score = score/keysize
            keysize_by_score.add((keysize, norm_score),)
        for _ in range(1):
            plaintext = [None]*len(ciphertext)
            keysize = keysize_by_score.pop()[0]
            key = [None]*keysize
            for i in range(keysize):
                cipherslice = ciphertext[i::keysize]
                temp = singleByteXOR_decrypt(cipherslice)
                plaintext[i::keysize] = temp[0]
                key[i] = temp[1]
            print(''.join(chr(c) for c in plaintext))
            print("the key was: " + ''.join(key))

if __name__ == '__main__':
    main()