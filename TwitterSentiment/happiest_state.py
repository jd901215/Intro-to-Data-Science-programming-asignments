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
    states_list = []

    for shortName, state in states.iteritems():
        states_list.append(state)

    for line in file:
        decoded.append(line)


    for element in decoded:
        if 'text' in element:

            text_on_tweet = element[108:element.find('source') - 2]

            coordinates_field = element[element.find("coordinates")+13:element.find("coordinates")+17]
            country_code = element[element.find("country_code")+15:element.find("country_code")+17]
            loc_by_user = element[element.find("location")+11:element.find("url",element.find("location")+10)-3]
            final_state = ''

            if coordinates_field != 'null' and country_code == "US":
                full_name = element[element.find("full_name",element.find("coordinates"))+12:element.find("country_code",element.find("coordinates"))-3]
                if 'USA' in full_name:
                    final_state =  full_name[:full_name.find(',')]
                else:
                    final_state =  states[full_name[full_name.find(',')+2:]]

            elif loc_by_user in states_list:
                final_state = loc_by_user

            if final_state != '':
                tweets.append((text_on_tweet,final_state))

    return tweets

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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    afinn = split_afinn(sent_file)
    decoded_tweets = stream2tweets(tweet_file)

    happiest_states = {}

    for tweet in decoded_tweets:
        score = score_tweet(tweet[0],afinn)
        if tweet[1] not in happiest_states:
            happiest_states[tweet[1]]=score
        else:
            happiest_states[tweet[1]]+=score

    highest_score = 0
    happiest_state = 'noone'

    for state, score in happiest_states.iteritems():
        if score>=highest_score:
            highest_score = score
            happiest_state = state

    for abbreviation, state in states.iteritems():
        if state == happiest_state:
            print abbreviation





states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}




if __name__ == '__main__':
    main()
