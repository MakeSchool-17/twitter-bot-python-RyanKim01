import sys
import random





if __name__ == '__main__':
    argv = sys.argv[1]
    with open(argv, 'r') as words:
        collection_of_words = words.read().split()
    print(random.choice(collection_of_words))
