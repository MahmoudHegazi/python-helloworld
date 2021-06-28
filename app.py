from flask import Flask, jsonify, json
import json
import logging
import random
app = Flask(__name__)


@app.route("/")
def hello():
    luckynumber = random.choice([1,2,12,18,15,14,3,15,30,10,6,11,7,8])
    app.logger.info('Main request successfull')
    return "Hello World Advanced automated! Your lucky number is: {}".format(luckynumber)

@app.route('/status')
def status():
    response = app.response_class(
            response = json.dumps({"result":"Ok - healthy"}),
            status=200,
            mimetype="application/json"
            )
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
            status= 200,
            mimetype="application/json"
            )
    return response
if __name__ == "__main__":
    logging.basicConfig(filename='logging.conf',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
