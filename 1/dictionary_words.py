import random
import sys


with open('/usr/share/dict/words', 'r') as words:
    readWords = words.read().split('\n')


if __name__ == '__main__':
    number_of_words = int(sys.argv[1])
    randomWords = []
    for i in range(0, number_of_words):
        randomWords.append(random.choice(readWords))
    print(randomWords)
