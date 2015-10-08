import random
import sys


def list_words_in_random_order(argv):
    random_order = []
    chars = argv[:]
    print(chars)
    print(argv)
    for word in argv:
        rand_index = random.randrange(0, len(chars))
        random_order.append(chars[rand_index])
        chars.pop(rand_index)
    return (' '.join(random_order))


if __name__ == '__main__':
    argv = sys.argv[1:]
    new_list = list_words_in_random_order(argv)
    print(new_list)
