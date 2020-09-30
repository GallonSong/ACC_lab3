import json
from glob import glob
from celery import Celery

app = Celery('tasks', broker='amqp://js:js@192.168.2.11/jsvhost', backend='rpc://')

file_names = glob("/home/ubuntu/ACC_lab3/data/*")
KEY_WORDS = {"han", "hon", "den", "det", "denna", "denne", "hen"}

def get_tweets():
    tweets = []
    for f_n in file_names:
        with open(f_n) as f:
            for l in f:
                if l.rstrip():
                    a = json.loads(l)
                    if "retweeted_status" not in a:
                        tweets.append(a["text"])
    return tweets

@app.task
def test():
    return "this is a test"

@app.task
def twitter_count():
    tweets = get_tweets()
    words_list = map(lambda x:x.lower().split(), tweets)
    mentions = {w: 0 for w in KEY_WORDS}
#    mention_tweets = {w:0 for w in KEY_WORDS}
    for w_l in words_list:
        intersec = set(w_l) & KEY_WORDS
        if intersec:
#            for w in intersec:
#                mention_tweets[w] += 1
            for ww in w_l:
                if ww in KEY_WORDS:
                    mentions[ww] += 1
    return mentions
