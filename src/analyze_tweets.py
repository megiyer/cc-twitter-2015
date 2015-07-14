# Insight Coding Challenge 2015 - Tweets
# Author: S. Iyer

# Given a text file of tweets (one tweet per line), this challenge is to implement two features:
# 1. Calculate the total number of times each word has been tweeted.
# 2. Calculate the median number of unique words per tweet, and update this median as tweets come in.

# --------------------------------------
import sys
from collections import defaultdict
import operator
import heapq
# --------------------------------------

def update_median(left, right, num):
    """ Add a new element to required data structures for computing new median
        - Maintain two heaps: (1) max-heap containing numbers <= median, (2) min-heap containing numbers >= median
        - At every function call, we pick one of the heaps to store the new incoming number
        - Median will either be the top of one of these two heaps, or the average of the top elements of both heaps
        - Length of these two heaps should not differ by more than one

        :param left: max-heap that contains all elements less than or equal to the median
        :param right: min-heap that contains all elements greater than or equal to the median
        :param num: number to be inserted into one of the heaps

        :return: the new median after taking into account the new incoming number
    """

    # Insert first incoming number into left
    if len(left) == 0:
        # heapq by default creates a min heap, negate values to use it as max heap
        heapq.heappush(left, -num)
        return num

    # Insert next new number into one of the heaps (left or right)
    if num <= (-left[0]):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    # Balance heaps if difference in their size is more than one
    if len(left) - len(right) > 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) - len(left) > 1:
        heapq.heappush(left, -heapq.heappop(right))

    # Return the median
    if len(left) == len(right):
        return (-left[0] + right[0]) / 2.0
    elif len(left) > len(right):
        return -left[0]
    else:
        return right[0]

# --------------------------------------

def process_input(tweets_input, ft1_output, ft2_output):
    """ Process each line in input file and perform the two required features

    :param tweets_input: Name of the file that contains tweets
    :param ft1_output: Name of the file to output count of tweeted words
    :param ft2_output: Name of the file to output stream of medians

    :return: None
    """

    # count of words tweeted
    word_counts = defaultdict(int)
    max_word_size = 0

    # max-heap that contains all elements less than or equal to the median
    left = []
    # min-heap that contains all elements greater than or equal to the median
    right = []

    with open(ft2_output, 'w') as medians_file:
        with open(tweets_input, 'r') as tweets_file:
            for tweet in tweets_file:

                # Do nothing if empty line/tweet
                if len(tweet.strip()) == 0:
                    continue

                # Feature 2: compute new median and write to file
                n_unique_words = len(set(tweet.split()))
                tweet_median = update_median(left, right, n_unique_words)
                medians_file.write('{0:.1f}\n'.format(tweet_median))

                # Keep a record of tweeted word counts
                for word in tweet.split():
                    if len(word) > max_word_size:
                        max_word_size = len(word)
                    word_counts[word] += 1

    # Feature 1: write word counts to file
    with open(ft1_output, 'w') as word_counts_file:
        for tweeted_word, word_count in sorted(word_counts.items(), key=operator.itemgetter(0)):
            word_counts_file.write('{0} {1}\n'.format(tweeted_word.ljust(max_word_size), str(word_count)))

# --------------------------------------
if __name__ == '__main__':

    if len(sys.argv) == 4:
        # files specified
        test_file = sys.argv[1]
        ft1_output_file = sys.argv[2]
        ft2_output_file = sys.argv[3]
    else:
        # defaults used
        test_file = 'tweet_input/tweets.txt'
        ft1_output_file = 'tweet_output/ft1.txt'
        ft2_output_file = 'tweet_output/ft2.txt'

    process_input(test_file, ft1_output_file, ft2_output_file)
# --------------------------------------



