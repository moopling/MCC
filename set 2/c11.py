from Crypto.Cipher import AES
from Crypto.Random import random
from c10 import my_AES


def encryption_oracle(plaintext: bytes) -> bytes:
    padded_plaintext = get_random_bytes(
        5, 10) + plaintext + get_random_bytes(5, 10)
    iv = get_random_bytes(16)
    key = get_random_bytes(16)
    cipher = my_AES(key)
    if coinflip():
        ciphertext = cipher.encrypt_ecb(padded_plaintext)
    else:
        ciphertext = cipher.encrypt_cbc(padded_plaintext, iv)
    return ciphertext


def get_random_bytes(start: int, stop: int=None) -> bytes:
    if stop:
        length = random.randint(start, stop)
    else:
        length = start
    return bytes(random.getrandbits(8) for _ in range(length))


def coinflip() -> bool:
    return bool(random.getrandbits(1))


def main() -> None:
    message = b"hello"
    encrypted_message = encryption_oracle(message)
    print(encrypted_message)

if __name__ == '__main__':
    main()
