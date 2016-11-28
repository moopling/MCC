from Crypto.Random import random
from c10 import my_AES
from c09 import pad


def encryption_oracle(plaintext: bytes) -> bytes:
    padded_plaintext = pad_block(get_random_bytes(
        5, 10) + plaintext + get_random_bytes(5, 10))
    key = get_random_bytes(16)
    cipher = my_AES(key)
    if coinflip():
        ciphertext = cipher.encrypt_ecb(padded_plaintext)
    else:
        iv = get_random_bytes(16)
        ciphertext = cipher.encrypt_cbc(padded_plaintext, iv)
    return ciphertext


def pad_block(unpadded: bytes, blocksize: int=16) -> bytes:
    padded = pad(unpadded, len(unpadded) + blocksize -
                 (len(unpadded) % blocksize))
    return padded


def get_random_bytes(start: int, stop: int=None) -> bytes:
    if stop:
        length = random.randint(start, stop)
    else:
        length = start
    return bytes(random.getrandbits(8) for _ in range(length))


def coinflip() -> bool:
    return bool(random.getrandbits(1))


def get_num_repeats(ciphertext: bytes, blocksize: int=16)
    unique_blocks = set()
    for index in range(0, len(ciphertext), blocksize):
        unique_blocks.add(ciphertext[index:index + blocksize])
    return len(ciphertext) - len(unique_blocks)


def main() -> None:
    message = b"hello"
    encrypted_message = encryption_oracle(message)

    print(encrypted_message)

if __name__ == '__main__':
    main()
