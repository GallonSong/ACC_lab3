from glob import glob
from collections import Counter
from flask import Flask, request, jsonify
from flask import render_template
from tasks import test, tweet_task, get_task

app = Flask(__name__)

@app.route('/test')
def app_test():
    result = test.delay()
    return result.get()

@app.route('/tweet')
def tweet_index():
    total = len(glob("/home/ubuntu/ACC_lab3/data/*"))
    return render_template('index.html', total=total)

## Simple API for task 1
# def create_tasks(amount=None):
#     file_names = glob("/home/ubuntu/ACC_lab3/data/*")[:amount]
#     count = Counter({})
#     for f_n in file_names:
#         running_task = tweet_task.delay(f_n)
#         count += Counter(running_task.get())
#     return count

def create_tasks(amount=None):
    file_names = glob("/home/ubuntu/ACC_lab3/data/*")[:amount]
    task_ids = []
    for f_n in file_names:
        running_task = tweet_task.delay(f_n)
        task_ids.append(running_task.id)
    return task_ids

@app.route('/tweet/<int:amount>', methods=['GET'])
def tweet(amount):
    tasks = create_tasks(amount)
    return jsonify(tasks)

@app.route('/tweet/progress', methods=['POST'])
def tweet_progress():
    tasks = request.get_json()
    finished = 0
    for task_id in tasks:
        res = get_task(task_id)
        # print(res.status)
        if res.ready():
            finished += 1
    return jsonify(finished)

@app.route('/tweet/result', methods=['POST'])
def tweet_result():
    count = Counter({})
    tasks = request.get_json()
    for task_id in tasks:
        res = get_task(task_id)
        count += Counter(res.get())
    labels = list(dict(count).keys())
    total = dict(count)["total"]
    data = [d / total for d in dict(count).values()]
    return jsonify({"label": labels, "data": data})
