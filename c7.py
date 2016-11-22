from Crypto.Cipher import AES
import binascii

with open("7.txt", 'r') as file:
    b64_ciphertext = "".join([line.strip() for line in file.readlines()])
    ciphertext = binascii.a2b_base64(b64_ciphertext)
    
    key = b'YELLOW SUBMARINE'
    
    cipher = AES.AESCipher(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)