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
        unencrypted_blocks = self._split_blocks(plaintext)
        encrypted_block = iv
        ciphertext = []
        for unencrypted_block in unencrypted_blocks:
            i = self._xor_blocks(unencrypted_block, encrypted_block)
            encrypted_block = self.encrypt_ecb(i)
            ciphertext.append(encrypted_block)
        return b''.join(ciphertext)

    def decrypt_cbc(self, ciphertext: bytes, iv: bytes) -> bytes:
        encrypted_blocks = self._split_blocks(ciphertext)
        prev_encrypted_block = iv
        plaintext = []
        for encrypted_block in encrypted_blocks:
            i = self.decrypt_ecb(encrypted_block)
            unencrypted_block = self._xor_blocks(prev_encrypted_block, i)
            prev_encrypted_block = encrypted_block
            plaintext.append(unencrypted_block)
        return b''.join(plaintext)

    def _split_blocks(self, text: bytes) -> Iterator[bytes]:
        if len(text) % self.blocksize:
            raise ValueError("message must be a multiple of the blocksize")
        blocks = (text[i: i + self.blocksize]
                  for i in range(0, len(text), self.blocksize))
        return blocks

    def _xor_blocks(self, block1: bytes, block2: bytes) -> bytes:
        return bytes(block1[i] ^ block2[i] for i in range(self.blocksize))


def main() -> None:
    with open("10.txt") as file:
        base64_ciphertext = "".join([line.strip()
                                     for line in file.readlines()])
        ciphertext = a2b_base64(base64_ciphertext)

        key = b'YELLOW SUBMARINE'
        cipher = my_AES(key)
        iv = bytes(16)
        plaintext = cipher.decrypt_cbc(ciphertext, iv)
        print(plaintext)


if __name__ == '__main__':
    main()
