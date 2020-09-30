from flask import Flask
from tasks import test, twitter_count

app = Flask(__name__)

@app.route('/test')
def app_test():
    result = test.delay()
    return result.get()

@app.route('/twitter')
def twitter():
    result = twitter_count.delay()
    return result.wait()
