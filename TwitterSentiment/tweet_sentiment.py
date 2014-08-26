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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    afinn = split_afinn(sent_file)

    decoded_tweets = stream2tweets(tweet_file)

    for tweet in decoded_tweets:
        list_tweet = tweet.split(' ')
        score = 0
        for word in list_tweet:
             if word in afinn:
                 score += afinn[word]
        print score


if __name__ == '__main__':
    main()
