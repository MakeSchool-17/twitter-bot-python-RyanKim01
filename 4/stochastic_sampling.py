import sys
import random
from collections import defaultdict


def histogram(textfile):
    d = defaultdict(int)
    for word in textfile:
        d[word] += 1
    return d


if __name__ == '__main__':
    argv = sys.argv[1]
    with open(argv, 'r') as words:
        collection_of_words = words.read().split()
    print("Picked word with weight is", random.choice(collection_of_words))
    print("Randomly picked word is",
          random.choice(list(histogram(collection_of_words).keys())))
