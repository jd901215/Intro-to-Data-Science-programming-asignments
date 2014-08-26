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
    unknown_words = {}
    new_sentiment = []

    for tweet in decoded_tweets:
        list_tweet = tweet.split(' ')
        score_tweet = 0

        for word in list_tweet:
            if word in afinn and word.isalpha():
                score_tweet += afinn[word]

        if score_tweet != 0:
            for word in list_tweet:
                if word not in afinn and word.isalpha() and word not in unknown_words:
                    if score_tweet > 0:
                        unknown_words[word]=[0,1]
                    if score_tweet < 0:
                        unknown_words[word]=[1,0]
                elif word not in afinn and word.isalpha() and word in unknown_words:
                    if score_tweet > 0:
                        unknown_words[word][1]+=1
                    if score_tweet < 0:
                        unknown_words[word][0]+=1

    for key,value  in unknown_words.items():
        new_sentiment.append((key, (((float(value[1]-value[0]))/float((value[1]+value[0])))*5.0)))
    for element in new_sentiment:
        print element[0],element[1]



if __name__ == '__main__':
    main()
