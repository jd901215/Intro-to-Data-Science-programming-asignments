import sys
import json


def split_afinn(file):
    """
    :return: A dict with the sentiments and their scores
    """
    scores = {}  # initialize an empty dictionary

    for line in file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def stream2tweets(file):
    """
    :param: A streaming JSON file
    :return: A list with the
    """
    decoded = []
    tweets = []

    for line in file:
        decoded.append(line)

    for element in decoded:
        if 'text' in element:
            tweets.append(element[108:element.find('source') - 2])

    return tweets


def main():
    tweet_file = open(sys.argv[1])

    decoded_tweets = stream2tweets(tweet_file)
    total_words = 0
    words = {}
    final_frequency = []
    for tweet in decoded_tweets:
        list_tweet = tweet.split(' ')

        for word in list_tweet:
            if  word.isalpha():
                total_words += 1
                if word not in words:
                    words[word]=1
                else:
                    words[word] += 1

    for word,frequency in words.iteritems():
        final_frequency.append((word,float(frequency)/float(total_words)))

    for element in final_frequency:
        print element[0],element[1]



if __name__ == '__main__':
    main()
