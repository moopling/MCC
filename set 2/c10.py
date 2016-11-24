from binascii import a2b_base64
from math import ceil
from typing import Iterator
from Crypto.Cipher import AES


class my_AES:

    def __init__(self, key: bytes) -> None:
        self.cipher = AES.AESCipher(key, AES.MODE_ECB)
        self.blocksize = 16

    def encrypt_ecb(self, plaintext: bytes) -> bytes:
        return self.cipher.encrypt(plaintext)

    def decrypt_ecb(self, ciphertext: bytes) -> bytes:
        return self.cipher.decrypt(ciphertext)

    def encrypt_cbc(self, plaintext: bytes, iv: bytes) -> bytes:
        blocks = self._split_blocks(plaintext)
        blocks.next()
        x = (self._xor_blocks(blocks.next(), blocks.next())
             for i in range(self._num_blocks(plaintext)))

    def decrypt_cbc(self, ciphertext: bytes, iv: bytes) -> bytes:
        pass

    def _split_blocks(self, text: bytes) -> Iterator[bytes]:
        blocks = (text[i: i + self.blocksize]
                  for i in range(self._num_blocks(text)))
        return blocks

    def _xor_blocks(self, block1: bytes, block2: bytes) -> bytes:
        return bytes(block1[i] ^ block2[i] for i in range(self.blocksize))

    def _num_blocks(self, text) -> int:
        if not len(text) % self.blocksize:
            raise ValueError("message must be a multiple of the blocksize")
        return len(text) // self.blocksize


def main() -> None:
    with open("10.txt") as file:
        base64_ciphertext = "".join([line.strip()
                                     for line in file.readlines()])
        ciphertext = a2b_base64(base64_ciphertext)

        key = b'YELLOW SUBMARINE'
        cipher = my_AES(key)

        # plaintext = cipher.(ciphertext)
        # print(plaintext)


if __name__ == '__main__':
    main()
