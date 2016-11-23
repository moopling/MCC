def pad(plaintext, required_length):
    padding = required_length-len(plaintext)
    return plaintext + padding*bytes([padding])

def main():
    key = b'YELLOW SUBMARINE'
    print(pad(key, 20))

if __name__ == '__main__':
    main()