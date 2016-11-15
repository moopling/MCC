import binascii
from c2 import XORbytes
import sortedcontainers
from collections import defaultdict

letterfreq = defaultdict(int, {' ':18, 'e':10, 't':8, 'a':7, 'o':6, 'n':6})

char_scores = sortedcontainers.SortedListWithKey(key=lambda val: val[2])

def score(byte_array):
    score = 0
    for byte in byte_array.lower():
        letter = chr(byte)
        score += letterfreq[letter]
    return score

def main():
    hexstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    byte_array = binascii.a2b_hex(hexstr)
    length = len(byte_array)
    for i in range(256):
        b2 = bytes([i])*length
        XORattempt = XORbytes(byte_array, b2)
        scr = score(XORattempt)
        char_scores.add((XORattempt, i, scr),)
    print(char_scores.pop())


if __name__ == '__main__':
    main()