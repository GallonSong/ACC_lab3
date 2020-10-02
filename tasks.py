import json
from celery import Celery
from celery.result import AsyncResult

app = Celery('tasks')
app.config_from_object('celeryconfig')

KEY_WORDS = {"han", "hon", "den", "det", "denna", "denne", "hen"}

def get_tweets(file_name):
    tweets = []
    with open(file_name) as f:
        for line in f:
            if line.rstrip():
                tweet = json.loads(line)
                if "retweeted_status" not in tweet:
                    tweets.append(tweet["text"])
    return tweets

def get_task(task_id):
    res = tweet_task.AsyncResult(task_id, app=app)
    return res

@app.task
def test():
    return "this is a test"

@app.task
def tweet_task(file_name):
    tweets = get_tweets(file_name)
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
    mentions["total"] = len(tweets)
    return mentions
