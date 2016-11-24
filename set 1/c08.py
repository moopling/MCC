import binascii
import sortedcontainers
from math import ceil

ciphertext_by_score = sortedcontainers.SortedListWithKey(
    key=lambda val: -val[0])

with open("08.txt", 'r') as file:
    texts = [binascii.a2b_hex(line.strip()) for line in file.readlines()]
    for text in texts:
        unique_blocks = set()
        for index in range(0, len(text), 16):
            unique_blocks.add(text[index:index + 16])
        ciphertext_by_score.add((len(unique_blocks), text),)
    print(ciphertext_by_score.pop()[1])
