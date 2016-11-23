def pad(plaintext: bytes, required_length: int) -> bytes:
    padding = required_length - len(plaintext)
    return plaintext + padding * bytes([padding])


def main() -> None:
    key = b'YELLOW SUBMARINE'
    value = 20
    print(pad(key, value))

if __name__ == '__main__':
    main()
