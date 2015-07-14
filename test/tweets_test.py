# Insight Coding Challenge 2015 - Tweets generator and tests
# Author: S. Iyer

# -------------------------------------
from collections import defaultdict, Counter
import random
import string
import operator

# -------------------------------------
# Number of unique words in the input file
NUM_UNIQUE_WORDS = int(1000)

# Size of each word
WORD_SIZE = 5

# Characters used to create words
CHARS = string.ascii_lowercase  + string.digits + string.punctuation

# Number of lines in the input file
NUM_LINES = int(10000)

# Min and max size of one line in the file
MIN_LINE_SIZE = 1
MAX_LINE_SIZE = 40

# -------------------------------------

def word_generator():
    """ Randomly generate words for input file

    :return: None
    """
    all_words = []
    for _ in range(NUM_UNIQUE_WORDS):
        rand_word = ''.join(random.choice(CHARS) for _ in range(WORD_SIZE))
        all_words.append(rand_word)
    return all_words


def get_median(median_counter, total_items):
    """ Compute median using histogram method
    Assumption: Maximum size of line/tweet is known

    :param median_counter: Keeps a record of number of unique words seen per tweet
    :param total_items: Number of tweets processed up till now
    :return:
    """
    curr_count = 0
    left = 0
    for each_line_size in range(1, MAX_LINE_SIZE + 1):
        if median_counter[each_line_size] > 0:
            if left > 0:
                return (each_line_size + left) / 2.0
            curr_count += median_counter[each_line_size]
            if (total_items % 2 == 0) and (curr_count == total_items / 2):
                left = each_line_size
            if curr_count > (total_items/2):
                return each_line_size
    return 0


def create_files(tweets_input, ft1_output, ft2_output):
    """ Create an input test file of tweets.
        Keep a record of words and counts when they are added to the input file.
        Keep a record of running median as every tweet is created and added to this input file.
        Generate final output files for feature 1 and feature 2.

    :param tweets_input:
    :param ft1_output:
    :param ft2_output:
    :return:
    """
    # create all possible words for input file
    all_words = word_generator()

    word_counts = defaultdict(int)
    median_counter = Counter({k: 0 for k in range(1, MAX_LINE_SIZE + 1)})

    with open(tweets_input, 'w') as tweets_file:
        with open(ft2_output, 'w') as medians_file:
            for n_lines in range(1, NUM_LINES + 1):

                # add a tweet line to input/test file
                line_size = random.randint(MIN_LINE_SIZE, MAX_LINE_SIZE)
                words = [random.choice(all_words) for _ in range(line_size)]
                tweet = ' '.join(words)
                tweets_file.write(tweet + "\n")

                # Feature 1 testing: Keep a count of words added to test file
                for word in words:
                    word_counts[word] += 1

                # Feature 2 testing: compute new median via histogram method and write to file
                median_counter[len(set(words))] += 1
                medians_file.write('{0:.1f}\n'.format(get_median(median_counter, n_lines)))

        # Feature 1: write word counts to file
        with open(ft1_output, 'w') as word_counts_file:
            for word, count in sorted(word_counts.items(), key=operator.itemgetter(0)):
                word_counts_file.write('{0} {1}\n'.format(word.ljust(WORD_SIZE), str(count)))

# -------------------------------------

if __name__ == '__main__':
    test_file = 'test/tweets_random.txt'
    ft1_output_file = 'test/ft1_expected.txt'
    ft2_output_file = 'test/ft2_expected.txt'

    create_files(test_file, ft1_output_file, ft2_output_file)
# -------------------------------------
