__author__ = 'juanda'
import sys
import json
import operator
import string



def split_afinn(file):
    """
    :return: A dict with the sentiments and their scores
    """
    scores = {}  # initialize an empty dictionary

    for line in file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores


def stream2hashtags(file):
    """
    :param: A streaming JSON file
    :return: A list with the top ten hashtags
    """
    #
    hashtags = []
    hashtags_dict = {}
    decoded = []

    for line in file:
        decoded.append(line)

    for element in decoded:
        try:
            entity = json.loads(element)[u'entities']
            if u'hashtags' in entity and entity[u'hashtags']!=[]:
                    temp_hash = entity[u'hashtags'][0][u'text']
                    edited_hashtag = temp_hash.lower()
                    # exclude = set(string.punctuation)
                    # edited_hashtag = ''.join(ch for ch in lower if ch not in exclude)
                    hashtags.append(edited_hashtag)
        except KeyError:
            pass

    for hashtag in hashtags:
        if hashtag not in hashtags_dict:
            hashtags_dict[hashtag] = 1
        else:
            hashtags_dict[hashtag] += 1

    sorted_x = sorted(hashtags_dict.iteritems(), key=operator.itemgetter(1))

    return list(reversed(sorted_x[-10:]))


def score_tweet(tweet,sent_dict):
    """
    :param tweet: A string which represent one tweet
    :param sent_file: A Dict with words and their scores
    :return: Integer, the score of that tweet
    """
    score = 0
    tweet_list = tweet.split(' ')

    for word in tweet_list:
        if word in sent_dict:
            score += sent_dict[word]

    return score

def main():
    tweet_file = open(sys.argv[1])
    decoded_tweets = stream2hashtags(tweet_file)
    for e in decoded_tweets:
         print e[0],e[1]

if __name__ == '__main__':
    main()
