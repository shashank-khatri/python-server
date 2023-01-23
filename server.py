import json
import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def get_root():
    return 'Hello good people'

@app.route('/', methods=['POST'])
def github():
    discord_url = 'https://discord.com/api/webhooks/1065405532464238742/nrYJf0bneeJAt1gx1O7LMQME41hn67CEL6JSzfyRUsJ8k6gO_YzzL7BZ67nSF8bwFFdf'
    payload = json.loads(request.data)
    print(payload['starred_at'])
    if payload['starred_at'] == None:
         post_data = {
        'content':''+payload['sender']['login']+ ' has just unstarred your repo '+ payload['repository']['name']+'',
          }
    else:
        post_data = {
        'content':''+payload['sender']['login']+ ' has just starred your repo '+ payload['repository']['name']+'',
          }

    try:
        result = requests.post(discord_url, json = post_data)
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
         print("Payload delivered successfully, code {}.".format(result.status_code))
    return jsonify(success=True)

if __name__ == '__main__':
    app.run()