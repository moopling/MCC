from Crypto.Cipher import AES
from Crypto.Random import random


def encryption_oracle(plaintext: bytes) -> bytes:
    plaintext = get_random_bytes(5, 10) + plaintext + get_random_bytes(5, 10)
    iv = get_random_bytes(16)
    key = get_random_bytes(16)
    if coinflip():
        cipher = AES.AESCipher(key, AES.MODE_CBC, iv)
    else:
        cipher = AES.AESCipher(key, AES.MODE_ECB)
    return cipher.encrypt(plaintext)


def get_random_bytes(start: int, stop: int=None) -> bytes:
    if stop:
        length = random.randint(start, stop)
    else:
        length = start
    return bytes(random.getrandbits(8) for _ in range(length))


def coinflip() -> bool:
    if random.getrandbits(1):
        return True
    else:
        return False


def main() -> None:
    message = b"hello"
    encryption_oracle(message)
    pass

if __name__ == '__main__':
    main()
