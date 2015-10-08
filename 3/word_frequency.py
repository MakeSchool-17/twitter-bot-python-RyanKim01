from collections import defaultdict
import sys


with open('Beowulf.txt', 'r') as words:
    readWords = words.read().split()


def histogram(textfile):
    textfile = readWords
    d = defaultdict(int)
    for word in textfile:
        d[word] += 1
    return d


number_of_dictionary = len(histogram(readWords))


def unique_words(histogram):
    unique_numb = 1
    unique_word_freq = 0
    for word in histogram:
        if histogram[word] == unique_numb:
            unique_word_freq += 1
    return unique_word_freq


def frequency(word, histogram):
    return histogram[word]


def most_frequent_word(histogram):
    frequent_numb = 0
    for word in histogram:
        if histogram[word] > frequent_numb:
            frequent_numb = histogram[word]

    for word in histogram:
        if histogram[word] == frequent_numb:
            most_freq_word = word
    return most_freq_word


def average_freq(histogram):
    sum_of_freq = 0
    for word in histogram:
        sum_of_freq += histogram[word]
    average_freq_value = sum_of_freq / number_of_dictionary
    return average_freq_value


if __name__ == '__main__':
    argv = sys.argv[1]
    print(histogram(readWords))
    print("Frequency of the word you input is",
          frequency(argv, histogram(readWords)))
    print("Number of unique words is", unique_words(histogram(readWords)))
    print("Most frequent word is", most_frequent_word(histogram(readWords)))
    print("Number of different words used in the text is",
          len(histogram(readWords)))
    print("Average frequency of words in the text is",
          average_freq(histogram(readWords)))
