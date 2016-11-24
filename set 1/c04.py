import binascii
from c03 import singleByteXOR_decrypt
from sortedcontainers import SortedListWithKey

lines_by_score = SortedListWithKey(key=lambda val: val[2])


def main():
    with open("04.txt", 'r') as file:
        for hexstr in file:
            lines_by_score.add(singleByteXOR_decrypt(hexstr.rstrip()))
    print(lines_by_score.pop()[0])

if __name__ == '__main__':
    main()
